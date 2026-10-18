"""Siapkan aset Gemini: hapus pola kotak-kotak 'transparan' palsu -> PNG alpha sungguhan; latar 9:16 disalin apa adanya."""
import numpy as np, shutil, os
from PIL import Image, ImageFilter
from collections import deque
from scipy import ndimage as ndi

SRC, OUT = "assets/art/src/", "assets/art/"
CHARS = ["marika-hammer", "godwyn", "ranni", "two-fingers", "tarnished", "elden-ring"]
BGS = ["erdtree-crown", "erdtree-trunk", "erdtree-roots", "bg-hall", "bg-night", "bg-moon", "bg-battlefield"]

def levels(a):
    h, w, _ = a.shape; band = np.concatenate([a[:14].reshape(-1, 3), a[-14:].reshape(-1, 3), a[:, :14].reshape(-1, 3), a[:, -14:].reshape(-1, 3)])
    band = band[(band.max(1) - band.min(1)) <= 10]; g = band.mean(1)
    hist, edges = np.histogram(g, bins=64, range=(0, 256)); order = np.argsort(hist)[::-1]
    L1 = edges[order[0]] + 2; L2 = None
    for o in order[1:]:
        c = edges[o] + 2
        if abs(c - L1) >= 30: L2 = c; break
    return (max(L1, L2), min(L1, L2)) if L2 is not None else (L1, L1 - 60)

def decheck(name):
    im = Image.open(SRC + name + ".png").convert("RGB"); a = np.array(im).astype(np.int16)
    hi, lo = levels(a); g = a.mean(2)
    neutral = (a.max(2) - a.min(2)) <= 10
    cand = neutral & (g >= lo - 14) & (g <= hi + 14)
    lab, n = ndi.label(cand)
    h, w = cand.shape
    border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    bg = np.isin(lab, list(border))
    # kantong tertutup: hapus bila berisi pola kotak-kotak (kedua level hadir, hampir semuanya dalam rentang)
    idx = [k for k in range(1, n + 1) if k not in border]
    if idx:
        sizes = ndi.sum(cand, lab, idx)
        for k, sz in zip(idx, sizes):
            if sz < 25: continue
            m = lab == k; gm = g[m]
            has_hi = (np.abs(gm - hi) <= 12).mean() >= 0.08; has_lo = (np.abs(gm - lo) <= 12).mean() >= 0.08
            if has_hi and has_lo: bg |= m
    alpha = (~bg).astype(np.uint8) * 255
    lab2, n2 = ndi.label(alpha > 0)
    if n2 > 1:
        s2 = ndi.sum(alpha > 0, lab2, range(1, n2 + 1)); keep = np.isin(lab2, [i + 1 for i, s in enumerate(s2) if s >= 0.002 * h * w])
        alpha = np.where(keep, alpha, 0).astype(np.uint8)
    al = Image.fromarray(alpha).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.8))
    out = im.convert("RGBA"); out.putalpha(al)
    ys, xs = np.where(np.array(al) > 8); out = out.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))
    out.save(OUT + name + ".png")
    return out.size, (round(float(hi)), round(float(lo)))

for n in CHARS: print(n, decheck(n))
shutil.copy(SRC + "marika-throne.png", OUT + "marika-throne.png")
for n in BGS: shutil.copy(SRC + n + ".png", OUT + n + ".png")
print("ok")
