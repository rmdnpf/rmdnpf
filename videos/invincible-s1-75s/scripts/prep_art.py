"""Siapkan aset Gemini Invincible: tokoh berlatar navy -> PNG transparan (kunci warna per baris); latar disalin apa adanya."""
import numpy as np, shutil
from PIL import Image, ImageFilter
from scipy import ndimage as ndi
SRC, OUT = "assets/art/src/", "assets/art/"
CUT = {"mark-flying": 22, "omni-standing": 22, "omni-flying": 22, "guardians-group": 20}
COPY = ["mark-standing", "family-photo", "city-night", "sky-day", "city-wreck", "space-bg", "photo-wall"]

def cutout(name, tol, const=False, pockets=False):
    im = Image.open(SRC + name + ".png").convert("RGB"); a = np.array(im).astype(np.float32); h, w, _ = a.shape
    edge = np.concatenate([a[:, :8], a[:, -8:]], axis=1)            # kolom tepi kiri-kanan
    bg = np.median(edge, axis=1)[:, None, :]                          # estimasi latar per baris
    if const: bg = np.median(a[:20].reshape(-1, 3), axis=0)[None, None, :]
    d = np.sqrt(((a - bg) ** 2).sum(axis=2))
    cand = d < tol
    lab, n = ndi.label(cand)
    border = np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]])); border = border[border > 0]
    bgm = np.isin(lab, border)
    if pockets:
        sizes = ndi.sum(cand, lab, range(1, n + 1)); big = [i + 1 for i, s_ in enumerate(sizes) if s_ > 1500]
        bgm |= np.isin(lab, big)
    alpha = (~bgm).astype(np.uint8) * 255
    lab2, n2 = ndi.label(alpha > 0)
    if n2 > 1:
        sz = ndi.sum(alpha > 0, lab2, range(1, n2 + 1)); keep = [i + 1 for i, s in enumerate(sz) if s >= 0.003 * h * w]
        alpha = np.where(np.isin(lab2, keep), alpha, 0).astype(np.uint8)
    alpha = ndi.binary_fill_holes(alpha > 0).astype(np.uint8) * 255 if name != "guardians-group" else alpha
    al = Image.fromarray(alpha).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.0))
    out = im.convert("RGBA"); out.putalpha(al)
    ys, xs = np.where(np.array(al) > 8); out = out.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))
    out.save(OUT + name + ".png"); return out.size

print("mark-flying", cutout("mark-flying", 22)); print("omni-standing", cutout("omni-standing", 22)); print("omni-flying", cutout("omni-flying", 22, const=True, pockets=True)); print("guardians-group", cutout("guardians-group", 22, const=True))
for n in COPY: shutil.copy(SRC + n + ".png", OUT + n + ".png")
print("ok")
