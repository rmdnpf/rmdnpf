"""Potong latar putih figur menjadi PNG transparan (gaya gambar TIDAK diubah).
Masukan: assets/figures/src/*.png (latar putih). Keluaran: assets/figures/*.png (RGBA, dipangkas ke isi).
Latar putih yang terhubung ke tepi dihapus; lubang tertutup (antara lengan dan badan) dihapus bila putih murni dan cukup luas.
Pakai: python3 scripts/prep_figures.py"""
import glob, os
import numpy as np
from PIL import Image
from collections import deque
from scipy import ndimage

SRC, OUT = "assets/figures/src/", "assets/figures/"
SKIP = {"rachel-point"}  # latar hitam + glow: butuh versi latar putih


def cutout(path):
    a = np.array(Image.open(path).convert("RGB")).astype(np.float32)
    h, w, _ = a.shape
    mn = a.min(axis=2)
    near = mn > 238
    bg = np.zeros((h, w), bool); q = deque()
    for x in range(w):
        for y in (0, h - 1):
            if near[y, x] and not bg[y, x]: bg[y, x] = True; q.append((y, x))
    for y in range(h):
        for x in (0, w - 1):
            if near[y, x] and not bg[y, x]: bg[y, x] = True; q.append((y, x))
    while q:
        y, x = q.popleft()
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and near[ny, nx] and not bg[ny, nx]:
                bg[ny, nx] = True; q.append((ny, nx))
    # lubang tertutup: putih murni, luas
    pure = mn >= 251
    lab, n = ndimage.label(pure & ~bg)
    if n:
        sizes = ndimage.sum(pure & ~bg, lab, range(1, n + 1))
        for i, s in enumerate(sizes, 1):
            if s > 1500: bg |= lab == i
    alpha = np.where(bg, 0.0, 1.0)
    # tepi halus: piksel tepat di sebelah latar mendapat alpha parsial dari kegelapannya
    edge = ndimage.binary_dilation(bg, iterations=2) & ~bg
    soft = np.clip((255 - mn) / 70.0, 0, 1)
    alpha = np.where(edge, np.maximum(soft, 0.35), alpha)
    return a, alpha


os.makedirs(OUT, exist_ok=True)
for f in sorted(glob.glob(SRC + "*.png")):
    name = os.path.basename(f)[:-4]
    if name in SKIP:
        print("lewati", name, "(latar bukan putih)"); continue
    a, al = cutout(f)
    ys, xs = np.where(al > 0.05)
    y0, y1, x0, x1 = ys.min(), ys.max(), xs.min(), xs.max()
    rgba = np.dstack([a, al * 255])[y0:y1 + 1, x0:x1 + 1].astype(np.uint8)
    Image.fromarray(rgba, "RGBA").save(OUT + name + ".png")
    print("ok", name, rgba.shape[1], "x", rgba.shape[0])
