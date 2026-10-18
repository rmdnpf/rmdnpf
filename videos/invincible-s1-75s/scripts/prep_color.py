"""Key white backgrounds from the colored (flat) character art -> assets/art/color/*.png"""
from PIL import Image
import numpy as np
from scipy import ndimage as ndi
import glob, os

SRC = 'assets/art/color/src'
OUT = 'assets/art/color'

def key(path, thr=14, min_bg=1500, multi=False):
    a = np.array(Image.open(path).convert('RGB')).astype(int)
    bg = (255 - a.min(axis=2)) < thr
    lab, n = ndi.label(bg)
    sizes = ndi.sum(bg, lab, range(1, n + 1))
    bgm = np.isin(lab, [i + 1 for i, s in enumerate(sizes) if s > min_bg])
    fg = ~bgm
    lab2, n2 = ndi.label(fg)
    s2 = ndi.sum(fg, lab2, range(1, n2 + 1))
    if multi:
        fg = np.isin(lab2, [i + 1 for i, s in enumerate(s2) if s > 3000])
    else:
        fg = lab2 == (1 + int(np.argmax(s2)))
    alpha = np.clip((ndi.gaussian_filter(fg.astype(float), 0.8) - 0.25) / 0.5, 0, 1)
    return Image.fromarray(np.dstack([a.astype(np.uint8), (alpha * 255).astype(np.uint8)]), 'RGBA')

for p in sorted(glob.glob(SRC + '/*.png')):
    name = os.path.basename(p)
    o = key(p, multi=(name == 'guardians-group.png'))
    o.save(os.path.join(OUT, name))
    print(name, o.size, o.getbbox())
