#!/usr/bin/env python3
"""Kunci magenta -> RGBA (dipotong ke bbox) + plat 2x. Sumber di assets/new/src/ tidak diubah."""
import json, numpy as np
from PIL import Image
from scipy import ndimage
S, O = "assets/new/src/", "assets/new/"
meta = {}
def key(name, out):
    im = np.array(Image.open(S + name + ".png").convert("RGB")).astype(np.float32)
    m = np.minimum(im[..., 0], im[..., 2]) - im[..., 1]
    al0 = np.clip(1 - (m - 40) / 160.0, 0, 1); solid = al0 > 0.5
    lab, n = ndimage.label(solid)
    if n > 1:
        sz = ndimage.sum(solid, lab, range(1, n + 1)); solid = np.isin(lab, [i + 1 for i, s in enumerate(sz) if s > 400])
    solid = ndimage.binary_erosion(solid, iterations=1)
    interior = ndimage.binary_erosion(solid, iterations=3)
    _, (iy, ix) = ndimage.distance_transform_edt(~interior, return_indices=True)
    rgb = im.copy(); e = ~interior; rgb[e] = im[iy[e], ix[e]]
    sp = np.maximum(0, np.minimum(rgb[..., 0], rgb[..., 2]) - rgb[..., 1]); rgb[..., 0] -= sp; rgb[..., 2] -= sp
    rgb = np.clip(rgb, 0, 255)
    al = np.clip(ndimage.gaussian_filter(solid.astype(np.float32), 0.7) * 1.1 - 0.03, 0, 1)
    ys, xs = np.where(al > 0.05); y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    img = np.dstack([rgb, al * 255]).astype(np.uint8)[y0:y1, x0:x1]
    Image.fromarray(img, "RGBA").save(O + out + ".png")
    meta[out] = dict(w=int(x1 - x0), h=int(y1 - y0), ox=int(x0), oy=int(y0))
    a = img.astype(float); aa = a[..., 3] / 255; mm = np.minimum(a[..., 0], a[..., 2]) - a[..., 1]
    print(out, meta[out], "sisa magenta", int(((mm > 40) & (aa > 0.05)).sum()))
for n, o in (("tom-desk-new", "desk"), ("tom-draw-new", "draw"), ("rachel-new", "rachel"), ("summer-lean-new", "lean")): key(n, o)
Image.open(S + "P1.png").convert("RGB").resize((2048, 3072), Image.LANCZOS).save(O + "plate.jpg", quality=92)
json.dump(meta, open(O + "meta.json", "w"), indent=1)
