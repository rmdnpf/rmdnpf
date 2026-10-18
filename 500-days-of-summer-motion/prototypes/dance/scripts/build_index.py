#!/usr/bin/env python3
"""Bangun index.html adegan 5 (Tom menari di kota siang hari)."""
import os, json, shutil, wave
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); N = f"{R}/assets/new"
META = json.load(open(f"{N}/meta.json"))
K = 0.6                      # skala pose (world px per px kanvas): Tom berdiri ~812 px, konsisten dengan perspektif plat
GX, GY = 540, 1380           # titik pijak penari (dunia)
PS, POX, POY = 1.8, -470, -829   # skala plat, offset: horizon ~y818, lantai kaki y1380 (Tom 812 px)
PW, PH = round(1024 * PS), round(1536 * PS)
POSES = ["strut", "jump", "land", "point"]
DUR = 6.6

def dur(f): w = wave.open(f); return round(w.getnframes() / w.getframerate(), 2)

def fig(name):
    m = META[name]; w, h = round(1024 * K), round(1536 * K)
    return (f'<img id="d-{name}" class="fig" src="assets/new/{name}.png" style="left:{-round(m["cx"]*K)}px;top:{-round(m["bottom"]*K)}px;width:{w}px;height:{h}px" alt="">')
def cast(name):
    m = META[name]; w, h = round(1024 * K), round(1536 * K)
    ox, oy = round(m["cx"] * K), round(m["bottom"] * K)
    shutil.copy(f"{N}/{name}-sil.png", f"{N}/c-{name}.png")
    return (f'<img id="c-{name}" class="cast" src="assets/new/c-{name}.png" style="left:{-ox}px;top:{-oy}px;width:{w}px;height:{h}px;'
            f'transform-origin:{ox}px {oy}px;transform:scaleY(-.3) skewX(35deg)" alt="">')

dancer = "".join(fig(n) for n in POSES)
casts = "".join(cast(n) for n in ("strut", "land", "point"))

CROWD = [(90, 1235, .62, 0), (250, 1195, .5, 1), (830, 1195, .5, 0), (990, 1235, .62, 1), (420, 1150, .38, 1), (670, 1150, .38, 0)]
crowd = ""
for i, (x, y, sc, flip) in enumerate(CROWD):
    imgs = ""
    for p in ("strut", "land", "point"):
        m = META[p]; shutil.copy(f"{N}/{p}-sil.png", f"{N}/cr{i}-{p}.png")
        w, h = round(1024 * K * sc), round(1536 * K * sc)
        imgs += f'<img id="cr{i}-{p}" class="sil" src="assets/new/cr{i}-{p}.png" style="left:{-round(m["cx"]*K*sc)}px;top:{-round(m["bottom"]*K*sc)}px;width:{w}px;height:{h}px" alt="">'
    gw = round(380 * sc)
    crowd += (f'<div id="cr{i}" class="crowd" data-flip="{flip}" style="left:{x}px;top:{y}px">'
              f'<div class="ground" style="left:{-gw//2}px;top:-14px;width:{gw}px;height:{round(40*sc)}px;opacity:.55"></div>{imgs}</div>')
for i, (x, y, sc, flip) in enumerate(CROWD):
    shutil.copy(f"{N}/strut-sil.png", f"{N}/fg{i}.png") if i < 1 else None

px_tip = (GX + (META["point"]["topx"] - META["point"]["cx"]) * K, GY - (META["point"]["bottom"] - META["point"]["topy"]) * K)
CFG = dict(GX=GX, GY=GY, K=K, hand=[round(px_tip[0]), round(px_tip[1])], sc=[c[2] for c in CROWD])
bird = ('<svg id="bird" class="bird" viewBox="0 0 120 80" width="96" height="64" style="left:-48px;top:-60px"><g>'
        '<polygon points="30,44 2,34 6,52" fill="#2a5db0"/><ellipse cx="58" cy="44" rx="30" ry="19" fill="#3b7dd8"/>'
        '<ellipse cx="62" cy="52" rx="20" ry="10" fill="#a9c6e3"/><circle cx="88" cy="32" r="13" fill="#3b7dd8"/>'
        '<polygon points="99,30 114,34 99,38" fill="#e3a43c"/><circle cx="92" cy="29" r="2.4" fill="#16243a"/>'
        '<path id="bwing" d="M50 40 Q36 8 78 22 Q70 44 50 44Z" fill="#2a5db0" style="transform-origin:52px 42px"/>'
        '<path d="M56 62 L54 74 M66 62 L66 74" stroke="#e3a43c" stroke-width="3" stroke-linecap="round"/></g></svg>')

# sketsa arsitektur pada menara tengah (koordinat tampilan plat)
def L(d): return f'<path class="sk" pathLength="1" style="stroke-dasharray:1;stroke-dashoffset:1" d="{d}"/>'
sx0, sx1, sy0, sy1 = 1035, 1179, 702, 1584
sk = L(f"M{sx0} {sy1} L{sx0} {sy0} L{sx1} {sy0} L{sx1} {sy1}") + "".join(L(f"M{sx0} {y} L{sx1} {y}") for y in range(sy0 + 70, sy1, 70))
sk += "".join(L(f"M{x} {sy0} L{x} {sy1}") for x in (1071, 1107, 1143)) + L(f"M{sx0} {sy1} L{sx1} {sy0}")
sketch = (f'<svg id="sketch" style="position:absolute;left:{POX}px;top:{POY}px" width="{PW}" height="{PH}" viewBox="0 0 {PW} {PH}">'
          f'<rect id="skfill" x="{sx0}" y="{sy0}" width="{sx1-sx0}" height="{sy1-sy0}" fill="rgba(63,106,160,.28)" opacity="0"/>{sk}</svg>')

shutil.copy(f"{N}/strut-sil.png", f"{N}/fgs.png")
audio = [("vo6", "assets/vo/06.wav", 0.05, dur(f"{R}/assets/vo/06.wav"), 2, 1.0, ' data-audio-group="voiceover"'),
         ("bgm", "assets/bgm.wav", 0, DUR, 3, .35, ""),
         ("sx1", "assets/sfx/whoosh.wav", 1.75, dur(f"{R}/assets/sfx/whoosh.wav"), 4, .5, ""),
         ("sx2", "assets/sfx/pop.wav", 2.88, dur(f"{R}/assets/sfx/pop.wav"), 5, .6, ""),
         ("sx3", "assets/sfx/ding.wav", 4.0, dur(f"{R}/assets/sfx/ding.wav"), 6, .5, ""),
         ("sx4", "assets/sfx/whoosh.wav", 4.55, dur(f"{R}/assets/sfx/whoosh.wav"), 7, .4, "")]
audio_html = "\n".join(f' <audio id="{a}" src="{s}" data-start="{st}" data-duration="{d}" data-track-index="{tr}" data-volume="{v}"{g}></audio>' for a, s, st, d, tr, v, g in audio)

CSS = open(f"{R}/scripts/style.css").read(); JS = "const CFG=" + json.dumps(CFG) + ";\n" + open(f"{R}/scripts/timeline.js").read()
html = f'''<!doctype html>
<html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=1080, height=1920">
<title>Dance Prototype</title>
<script src="assets/gsap.min.js"></script>
<style>{CSS}</style></head><body>
<div id="root" data-composition-id="dance" data-width="1080" data-height="1920" data-start="0" data-duration="{DUR}">
 <div id="stage" class="clip" data-start="0" data-duration="{DUR}" data-track-index="0">
  <div id="in">
   <div id="bg" class="layer"><div id="bgs" class="layer"><img class="plate" src="assets/new/plate.jpg" style="left:{POX}px;top:{POY}px;width:{PW}px;height:{PH}px" alt="">{sketch}</div></div>
   <div id="world" class="layer">
    {crowd}
    <div id="pt" class="pt" style="left:{GX}px;top:{GY}px">
      <div id="dground" class="ground" style="left:-210px;top:-18px;width:420px;height:56px"></div>
      <div id="dcast" class="pt">{casts}</div>
      <div id="dancer" class="pt" style="transform-origin:0 0">{dancer}</div>
    </div>
    <div id="birdw" style="position:absolute;left:0;top:0;width:0;height:0">{bird}</div>
   </div>
   <img id="fgs" class="fgs" src="assets/new/fgs.png" style="left:0;top:0;width:768px;height:1152px" alt="">
   <div class="layer grade"></div><div class="layer vign"></div><div id="flash" class="layer flash"></div>
  </div>
  <div id="freeze"></div>
  <div id="subgrad"></div><div id="sub"></div>
 </div>
{audio_html}
</div>
<script>{JS}</script>
</body></html>'''
open(f"{R}/index.html", "w").write(html); print("ok", len(html), CFG["hand"])
