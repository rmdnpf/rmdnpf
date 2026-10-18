"""Recolor the (navy) backgrounds with gradient maps -> assets/art/color/bg-*.png (palet serial: langit biru, senja, merah, interior hangat)."""
from PIL import Image
import numpy as np
MAPS = {
    'sky-day':   ('bg-sky',        [(0, (22, 70, 150)), (.45, (64, 142, 224)), (.8, (160, 208, 245)), (1, (252, 253, 255))]),
    'sky-day2':  ('bg-sky-dusk',   [(0, (70, 22, 18)), (.35, (190, 70, 36)), (.7, (244, 150, 48)), (1, (255, 222, 120))]),
    'city-night':('bg-city-night', [(0, (22, 18, 46)), (.4, (76, 48, 92)), (.75, (200, 112, 90)), (1, (255, 224, 150))]),
    'city-wreck':('bg-city-wreck', [(0, (18, 12, 16)), (.4, (78, 30, 30)), (.7, (190, 62, 40)), (1, (255, 176, 96))]),
    'photo-wall':('bg-wall',       [(0, (46, 32, 28)), (.5, (140, 100, 76)), (1, (238, 216, 182))]),
}
def gmap(im, stops):
    L = np.array(im.convert('L')).astype(float) / 255; xs = [s[0] for s in stops]
    ch = [np.interp(L, xs, [s[1][c] for s in stops]) for c in range(3)]
    return Image.fromarray(np.dstack(ch).astype(np.uint8))
for src, (out, stops) in MAPS.items():
    gmap(Image.open(f'assets/art/{src.rstrip("2")}.png'), stops).save(f'assets/art/color/{out}.png')
    print(out)
