#!/usr/bin/env python3
"""Bangun index.html adegan 7 (Kembali menggambar). VO 07 belum final: tanpa VO, subtitle draf, hanya musik/SFX."""
import os, json, shutil, wave
import numpy as np
from PIL import Image
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); N = f"{R}/assets/new"
META = json.load(open(f"{N}/meta.json"))
DUR = 4.7
FLOOR = 1260                      # kaki (perspektif plat: Tom lebih kecil, lebih jauh agar Tom + Rachel muat satu bingkai)
KT = 0.49; KR = 0.406             # skala Tom (gambar) dan Rachel (0,85x Tom)
TL = 518                          # kiri meja gambar Tom (dunia)
ROT = 14                          # condong Rachel (derajat, searah jarum jam) saat menjangkau bahu
def dur(f): w = wave.open(f); return round(w.getnframes() / w.getframerate(), 2)
def sil(name):
    a = np.array(Image.open(f"{N}/{name}.png")); a[..., :3] = 0; Image.fromarray(a, "RGBA").save(f"{N}/{name}-sil.png")
for n in ("draw", "rachel"): sil(n)
md, mr = META["draw"], META["rachel"]
tw, th = round(md["w"] * KT), round(md["h"] * KT); tt = FLOOR - th
rw, rh = round(mr["w"] * KR), round(mr["h"] * KR); rt = FLOOR - rh
# titik pijak Rachel (tengah kaki) dan ujung tangan pada kanvas terpotong
hand_c = (919, 151); feet_c = (244, 1431)
dx, dy = (hand_c[0] - feet_c[0]) * KR, (hand_c[1] - feet_c[1]) * KR
import math
c, s = math.cos(math.radians(ROT)), math.sin(math.radians(ROT))
hx_rel, hy_rel = dx * c - dy * s, dx * s + dy * c
hand_target_x = TL + 30                      # punggung atas Tom
rfeet_x = hand_target_x - hx_rel
rl = round(rfeet_x - feet_c[0] * KR)
def cast(name, l, t, w, h, ox):
    return (f'<img class="cast" src="assets/new/{name}-sil.png" style="left:{l}px;top:{t}px;width:{w}px;height:{h}px;'
            f'transform-origin:{ox}px {h}px;transform:scaleY(-.3) skewX(35deg)" alt="">')
def L(d): return f'<path class="sk" pathLength="1" d="{d}"/>'
bld = (L("M20 120 L20 70 L50 70 L50 45 L80 45 L80 25 L105 25 L105 45 L135 45 L135 70 L170 70 L170 120") + L("M10 120 L190 120")
       + "".join(L(f"M{x} 70 L{x} 120") for x in (80, 110, 140)))
boardx, boardy = TL + 850 * KT, (FLOOR - th) + 395 * KT
sheets = "".join(f'<div id="sh{i}" class="sheet" style="left:{round(boardx)-75}px;top:{round(boardy)-55}px"><svg width="150" height="110" viewBox="0 0 200 130" style="position:absolute;left:0;top:0">{bld.replace("sk","sks")}</svg></div>' for i in range(3))
photos = "".join(f'<div id="ph{i}" class="ph" style="left:{x}px;top:{y}px;transform:rotate({r}deg)"><u></u></div>' for i, (x, y, r) in enumerate([(104, 262, -4), (290, 250, 3), (140, 420, 2), (310, 430, -3), (222, 566, -2)]))
pages = "".join(f'<div id="pg{i}" class="pg" style="left:{x}px;top:{y}px;transform:rotate({r}deg)"><u></u></div>' for i, (x, y, r) in enumerate([(104, 262, -4), (290, 250, 3), (140, 420, 2), (310, 430, -3), (222, 566, -2)]))
audio = [("bgm", "assets/bgm.wav", 0, DUR, 3, .35)]
sfx = [("whoosh", 0.3, 4), ("ding", 2.0, 5), ("whoosh", 2.4, 6), ("pop", 3.4, 7), ("pop", 3.8, 8), ("pop", 4.2, 9)]
parts = [f' <audio id="bgm" src="assets/bgm.wav" data-start="0" data-duration="{DUR}" data-track-index="3" data-volume=".35"></audio>']
for j, (n, st, tr) in enumerate(sfx):
    parts.append(f' <audio id="sx{j}" src="assets/sfx/{n}.wav" data-start="{st}" data-duration="{dur(f"{R}/assets/sfx/{n}.wav")}" data-track-index="{tr}" data-volume=".5"></audio>')
audio_html = "\n".join(parts)
# lampu dan papan gambar (koordinat dunia dari kanvas terpotong tom-draw)
lampx, lampy = TL + 759 * KT, tt + 116 * KT
boardx, boardy = TL + 850 * KT, tt + 395 * KT
CFG = dict(rotate=ROT, board=[round(boardx), round(boardy)], lamp=[round(lampx), round(lampy)], rfeet=[round(rfeet_x), FLOOR])
CSS = open(f"{R}/scripts/style.css").read(); JS = "const CFG=" + json.dumps(CFG) + ";\n" + open(f"{R}/scripts/timeline.js").read()
html = f'''<!doctype html>
<html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=1080, height=1920">
<title>Draw Prototype</title>
<script src="assets/gsap.min.js"></script>
<style>{CSS}</style></head><body>
<div id="root" data-composition-id="draw" data-width="1080" data-height="1920" data-start="0" data-duration="{DUR}">
 <div id="stage" class="clip" data-start="0" data-duration="{DUR}" data-track-index="0">
  <div id="in" class="layer">
   <div id="world" class="layer">
    <img class="plate" src="assets/new/plate.jpg" style="left:-100px;top:0;width:1280px;height:1920px" alt="">
    <div id="nightov" class="layer"></div>
    <div class="glow" style="left:{round(lampx)-260}px;top:{round(lampy)-120}px;width:520px;height:620px"></div>
    <div class="glow" style="left:{TL}px;top:{tt+60}px;width:620px;height:420px;opacity:.5"></div>
    {photos}{pages}
    <div id="rg" style="position:absolute;left:0;top:0;width:0;height:0">
     <div class="ground" style="left:{round(rfeet_x)-110}px;top:{FLOOR-14}px;width:220px;height:34px"></div>
     {cast("rachel", rl, rt, rw, rh, round(feet_c[0]*KR))}
     <img id="rach" class="fig" src="assets/new/rachel.png" style="left:{rl}px;top:{rt}px;width:{rw}px;height:{rh}px;transform-origin:{round(feet_c[0]*KR)}px {rh}px" alt="">
    </div>
    <div id="tg" style="position:absolute;left:0;top:0;width:0;height:0">
     <div class="ground" style="left:{TL+30}px;top:{FLOOR-16}px;width:{tw-40}px;height:38px"></div>
     {cast("draw", TL, tt, tw, th, tw//2)}
     <img id="tom" class="fig" src="assets/new/draw.png" style="left:{TL}px;top:{tt}px;width:{tw}px;height:{th}px" alt="">
    </div>
    <div id="sktop" style="left:{round(boardx)-100}px;top:{round(boardy)-70}px;width:200px;height:130px;transform:rotate(-17deg)"><svg width="200" height="130" viewBox="0 0 200 130">{bld}</svg></div>
    <div id="folder"></div>
    {sheets}
   </div>
   <div class="layer" id="doorw"><div id="door"></div></div>
   <div class="layer grade"></div><div class="layer vign"></div>
   <div id="lab">RACHEL · ADIK TOM</div>
  </div>
  <div id="subgrad"></div><div id="sub"></div>
 </div>
{audio_html}
</div>
<script>{JS}</script>
</body></html>'''
open(f"{R}/index.html", "w").write(html); print("ok", len(html), CFG)
