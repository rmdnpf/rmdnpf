#!/usr/bin/env python3
"""Kunci magenta -> RGBA untuk aset baru (sumber di assets/new/src/, tidak diubah). Hasil di assets/new/."""
import json, numpy as np
from PIL import Image
from scipy import ndimage
S, O = "assets/new/src/", "assets/new/"
meta = {}
def key(name, out, crop=True, soft=False, flip=False, xmax=None, thr=40):
    im = np.array(Image.open(S + name + ".png").convert("RGB")).astype(np.float32)
    if xmax: im = im[:, :xmax]
    h, w, _ = im.shape
    m = np.minimum(im[..., 0], im[..., 2]) - im[..., 1]
    if soft:
        al = np.clip((255 - m) / 275.0, 0, 1)
        al = np.where(m < 20, 1, al)
        M = np.array([255, 0, 255], np.float32)
        a3 = np.maximum(al, 1e-3)[..., None]
        rgb = np.clip((im - (1 - a3) * M) / a3, 0, 255)
    else:
        al0 = np.clip(1 - (m - thr) / 160.0, 0, 1)
        solid = al0 > 0.5
        lab, n = ndimage.label(solid)                       # buang bintik kecil
        if n > 1:
            sz = ndimage.sum(solid, lab, range(1, n + 1)); keep = [i + 1 for i, s in enumerate(sz) if s > 400]
            solid = np.isin(lab, keep)
        solid = ndimage.binary_erosion(solid, iterations=1)
        interior = ndimage.binary_erosion(solid, iterations=3)
        _, (iy, ix) = ndimage.distance_transform_edt(~interior, return_indices=True)
        rgb = im.copy(); e = ~interior; rgb[e] = im[iy[e], ix[e]]   # semua piksel di luar bagian dalam (termasuk pita blur) ambil warna terdekat
        al = np.clip(ndimage.gaussian_filter(solid.astype(np.float32), 0.7) * 1.1 - 0.03, 0, 1)
    sp = np.maximum(0, np.minimum(rgb[..., 0], rgb[..., 2]) - rgb[..., 1]); rgb = rgb.copy(); rgb[..., 0] -= sp; rgb[..., 2] -= sp   # despill magenta
    rgb = np.clip(rgb, 0, 255)
    img = np.dstack([rgb, al * 255]).astype(np.uint8)
    ox = oy = 0
    if crop:
        ys, xs = np.where(al > 0.05); y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
        img = img[y0:y1, x0:x1]; ox, oy = int(x0), int(y0)
    pil = Image.fromarray(img, "RGBA")
    if flip: pil = pil.transpose(Image.FLIP_LEFT_RIGHT)
    pil.save(O + out + ".png"); meta[out] = dict(w=pil.width, h=pil.height, ox=ox, oy=oy)
    print(out, pil.size, "offset", ox, oy)
key("summer-greet", "greet")
key("hug-warm", "hug-warm")
key("hug-stiff", "hug-stiff")
key("hand-insert", "hand", crop=False)
key("hand-insert-ring", "hand-ring", crop=False)
key("P3-fg", "fg-plant", crop=False, soft=True, flip=True, xmax=360)
bg = Image.open(S + "P3-bg.png").convert("RGB"); bg.resize((2048, 3072), Image.LANCZOS).save(O + "bg.jpg", quality=92)
for n, o in (("hand", "hand2x"), ("hand-ring", "hand-ring2x")):   # sisipan tangan: JPG 2x, area magenta (di luar tampilan) diisi gelap
    a = Image.open(O + n + ".png"); bgc = Image.new("RGBA", a.size, (30, 22, 18, 255)); bgc.alpha_composite(a)
    bgc.convert("RGB").resize((a.width * 2, a.height * 2), Image.LANCZOS).save(O + o + ".jpg", quality=93)
json.dump(meta, open(O + "meta.json", "w"), indent=1)
# validasi tepi: sisa magenta pada piksel tepi
for n in ("greet", "hug-warm", "hug-stiff", "hand", "hand-ring"):
    a = np.array(Image.open(O + n + ".png")).astype(float); al = a[..., 3] / 255
    mm = np.minimum(a[..., 0], a[..., 2]) - a[..., 1]; edge = (al > 0.05) & (al < 0.95)
    print(n, "sisa magenta pada tepi:", int(((mm > 40) & (al > 0.05)).sum()), "px; tepi semi:", int(edge.sum()))
