"""Bangun index.html dari scripts/index.src.html:
1) ganti makro [[fig id=.. name=.. x=.. y=.. h=.. cls=.. allow=1]] dengan <img> ukuran persis (lebar dihitung dari PNG),
2) segarkan jadwal VO (make_timing.py) dan blok audio (add_audio.py).
Pakai: python3 scripts/build_index.py"""
import re, shutil, subprocess, sys
from PIL import Image, ImageOps

used = {}

src = open("scripts/index.src.html").read()

def fig(m):
    kv = dict(re.findall(r"(\w+)=(\S+)", m.group(1)))
    name = kv["name"]
    used[name] = used.get(name, 0) + 1
    if used[name] > 1:   # gambar yang dipakai lagi disalin agar tiap <img> punya sumber unik
        dup = f"{name}-{used[name]}"
        shutil.copyfile(f"assets/figures/{name}.png", f"assets/figures/{dup}.png")
        kv["name"] = dup
    if kv.get("flip"):   # cermin horizontal (berhadapan)
        flipped = f"{kv['name']}-flip"
        ImageOps.mirror(Image.open(f"assets/figures/{kv['name']}.png")).save(f"assets/figures/{flipped}.png")
        kv["name"] = flipped
    w0, h0 = Image.open(f"assets/figures/{kv['name']}.png").size
    h = float(kv["h"]); w = round(h * w0 / h0)
    cls = "fig" + (" " + kv["cls"] if "cls" in kv else "")
    allow = ' data-layout-allow-overflow' if kv.get("allow") else ""
    return (f'<img id="{kv["id"]}" class="{cls}"{allow} src="assets/figures/{kv["name"]}.png" alt="" '
            f'style="left:{kv["x"]}px;top:{kv["y"]}px;width:{w}px;height:{round(h)}px">')

out = re.sub(r"\[\[fig ([^\]]+)\]\]", fig, src)
open("index.html", "w").write(out)
for script in ("scripts/make_timing.py", "scripts/add_audio.py"):
    subprocess.run([sys.executable, script], check=True, stdout=subprocess.DEVNULL)
print("index.html dibangun")
