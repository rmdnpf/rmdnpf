"""Siapkan siluet dari Gemini: hapus latar putih -> PNG transparan, plus versi warna palet."""
import numpy as np
from PIL import Image
from collections import deque

def cutout(path):
    im = Image.open(path).convert("RGB"); a = np.array(im).astype(np.float32)
    h, w, _ = a.shape
    near_white = a.min(axis=2) > 236
    bg = np.zeros((h, w), bool); q = deque()
    for x in range(w):
        for y in (0, h - 1):
            if near_white[y, x] and not bg[y, x]: bg[y, x] = True; q.append((y, x))
    for y in range(h):
        for x in (0, w - 1):
            if near_white[y, x] and not bg[y, x]: bg[y, x] = True; q.append((y, x))
    while q:
        y, x = q.popleft()
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and near_white[ny, nx] and not bg[ny, nx]:
                bg[ny, nx] = True; q.append((ny, nx))
    # tepi halus: piksel dekat latar dapat alpha parsial dari kegelapannya
    alpha = np.where(bg, 0.0, 1.0)
    edge = np.zeros_like(bg)
    for dy in range(-2, 3):
        for dx in range(-2, 3):
            edge |= np.roll(np.roll(bg, dy, 0), dx, 1)
    soft = np.clip((255 - a.min(axis=2)) / 200.0, 0, 1)
    alpha = np.where(edge & ~bg, np.maximum(soft, 0.0), alpha)
    return a, alpha

def hexrgb(h): h = h.lstrip("#"); return np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)], np.float32)

def save(a, alpha, out, body=None, rim=None, scale=1):
    lum = a.mean(axis=2)
    if body is not None:
        lo, hi = 38.0, 190.0
        t = np.clip((lum - lo) / (hi - lo), 0, 1)[..., None]
        rgb = hexrgb(body) * (1 - t) + hexrgb(rim) * t
    else:
        rgb = a
    img = np.dstack([rgb, alpha * 255]).astype(np.uint8)
    im = Image.fromarray(img, "RGBA")
    if scale != 1: im = im.resize((im.width * scale, im.height * scale), Image.LANCZOS)
    im.save(out)

PAL = {"navy": ("#0b1230", "#7f94ff"), "pink": ("#ff5fa2", "#ffd6ea"), "blue": ("#2f5bff", "#cfe0ff")}
NEED = {"mima-mic": [], "mima-stand": ["pink"], "mima-side": ["blue"], "idol-long": ["pink"], "idol-twin": []}
src = "assets/figures/src/"
for name in ["mima-mic", "mima-stand", "mima-side"]:
    a, al = cutout(src + name + ".png")
    save(a, al, f"assets/figures/{name}.png")
    for k in NEED[name]: save(a, al, f"assets/figures/{name}-{k}.png", *PAL[k])
a, al = cutout(src + "idol-duo.png")
h, w = al.shape; cut = w // 2 + 20
for nm, sl in (("idol-long", slice(0, cut)), ("idol-twin", slice(cut, w))):
    aa, ll = a[:, sl], al[:, sl]
    ys, xs = np.where(ll > 0.05); y0, y1, x0, x1 = ys.min(), ys.max(), xs.min(), xs.max()
    aa, ll = aa[y0:y1 + 1, x0:x1 + 1], ll[y0:y1 + 1, x0:x1 + 1]
    save(aa, ll, f"assets/figures/{nm}.png")
    for k in NEED[nm]: save(aa, ll, f"assets/figures/{nm}-{k}.png", *PAL[k])
for name in ["crowd"]:
    a, al = cutout(src + name + ".png")
    ys, xs = np.where(al > 0.05); y0, y1, x0, x1 = ys.min(), ys.max(), xs.min(), xs.max()
    save(a[y0:y1 + 1, x0:x1 + 1], al[y0:y1 + 1, x0:x1 + 1], f"assets/figures/{name}.png")
for name in ["rumi-mgr", "rumi-idol"]:
    a, al = cutout(src + name + ".png")
    ys, xs = np.where(al > 0.05); y0, y1, x0, x1 = ys.min(), ys.max(), xs.min(), xs.max()
    aa, ll = a[y0:y1 + 1, x0:x1 + 1], al[y0:y1 + 1, x0:x1 + 1]
    save(aa, ll, f"assets/figures/{name}.png")
    for k in ("pink", "paper"): save(aa, ll, f"assets/figures/{name}-{k}.png", *({**PAL, "paper": ("#f2f0ff", "#8fa0ff")}[k]))
for name in ["eye-blue", "eye-red", "mima-stand2"]:
    a, al = cutout(src + name + ".png")
    # rapikan: potong ke kotak isi
    ys, xs = np.where(al > 0.05); y0, y1, x0, x1 = ys.min(), ys.max(), xs.min(), xs.max()
    save(a[y0:y1 + 1, x0:x1 + 1], al[y0:y1 + 1, x0:x1 + 1], f"assets/figures/{name}.png")
print("ok")
