#!/usr/bin/env python3
"""Bangun index.html: adegan 1–3 (Menghitung mundur, Kartu terbuka, Dua dunia)."""
import os, json, shutil, wave
import numpy as np
from PIL import Image
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); N = f"{R}/assets/new"
META = json.load(open(f"{N}/meta.json"))
PS, POX = 1.25, -100
FLOOR_T = 1437                     # kaki Tom (lantai depan)  -> y plat 1150
FLOOR_S = 1156                     # kaki Summer (dekat sekat) -> y plat 925
KD, KL = 0.657, 0.337              # skala meja Tom / Summer (world px per px aset), dari perspektif plat (horizon y plat ~590)
DUR = 20.6
def dur(f): w = wave.open(f); return round(w.getnframes() / w.getframerate(), 2)
def sil(name):
    a = np.array(Image.open(f"{N}/{name}.png")); a[..., :3] = 0; Image.fromarray(a, "RGBA").save(f"{N}/{name}-sil.png")
for n in ("desk", "lean"): sil(n)
md, ml = META["desk"], META["lean"]
dw, dh = round(md["w"] * KD), round(md["h"] * KD); dl = 460 - dw // 2; dt = FLOOR_T - dh
lw, lh = round(ml["w"] * KL), round(ml["h"] * KL); ll = 856 - lw; lt = FLOOR_S - lh
def cast(name, l, t, w, h): return (f'<img class="cast" src="assets/new/{name}-sil.png" style="left:{l}px;top:{t}px;width:{w}px;height:{h}px;'
                                   f'transform-origin:50% 100%;transform:scaleY(-.3) skewX(35deg)" alt="">')
sheets = ""
NUMS = [500, 431, 372, 310, 250, 190, 140, 96, 60, 31, 9, 1]
for i in reversed(range(len(NUMS))):
    sheets += f'<div id="sh{i}" class="sheet"><i>HARI</i><b>{NUMS[i]}</b></div>'
def L(d, cls="sk2"): return f'<path class="{cls}" pathLength="1" d="{d}"/>'
sk2 = (L("M60 620 L60 330 L120 330 L120 250 L190 250 L190 190 L260 190 L260 330 L320 330 L320 620") + L("M60 620 L440 620")
       + "".join(L(f"M{x} 330 L{x} 620") for x in (150, 230)) + L("M120 250 L260 250") + L("M190 190 L190 130 L225 130 L225 190"))
audio = [("vo1", "assets/vo/01.wav", 0.4, 2, 1.0, ' data-audio-group="voiceover"'), ("vo2", "assets/vo/02.wav", 5.56, 2, 1.0, ' data-audio-group="voiceover"'),
         ("vo3", "assets/vo/03.wav", 11.84, 2, 1.0, ' data-audio-group="voiceover"'), ("bgm", "assets/bgm.wav", 0, 3, .35, "")]
sfx = [("whoosh", 1.95, 4), ("pop", 2.55, 5), ("ding", 6.1, 6), ("chime", 7.2, 7), ("whoosh", 11.1, 8), ("whoosh", 18.7, 9), ("stamp", 19.7, 10)]
ticks = [0.5 + i * 0.12 for i in range(11)]
parts = []
for a, s, st, tr, v, g in audio:
    d = DUR if a == "bgm" else dur(f"{R}/{s}")
    parts.append(f' <audio id="{a}" src="{s}" data-start="{st}" data-duration="{d}" data-track-index="{tr}" data-volume="{v}"{g}></audio>')
for j, (n, st, tr) in enumerate(sfx):
    parts.append(f' <audio id="sx{j}" src="assets/sfx/{n}.wav" data-start="{st}" data-duration="{dur(f"{R}/assets/sfx/{n}.wav")}" data-track-index="{tr}" data-volume=".5"></audio>')
for j, t in enumerate(ticks):
    parts.append(f' <audio id="tk{j}" src="assets/sfx/tick.wav" data-start="{t:.2f}" data-duration="0.06" data-track-index="11" data-volume=".45"></audio>')
audio_html = "\n".join(parts)
CSS = open(f"{R}/scripts/style.css").read(); JS = open(f"{R}/scripts/timeline.js").read()
html = f'''<!doctype html>
<html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=1080, height=1920">
<title>Opening Prototype</title>
<script src="assets/gsap.min.js"></script>
<style>{CSS}</style></head><body>
<div id="root" data-composition-id="opening" data-width="1080" data-height="1920" data-start="0" data-duration="{DUR}">
 <div id="stage" class="clip" data-start="0" data-duration="{DUR}" data-track-index="0">
  <div id="in" class="layer">
   <div id="world" class="layer">
    <img id="plate" class="plate" src="assets/new/plate.jpg" style="left:{POX}px;top:0;width:{round(1024*PS)}px;height:{round(1536*PS)}px" alt="">
    <div id="nightov" class="layer"></div>
    <div id="lamp" style="left:90px;top:860px;width:760px;height:520px;opacity:.0"></div>
    <div id="sumg" style="position:absolute;left:0;top:0;width:0;height:0">
     <div class="ground" style="left:{ll-20}px;top:{FLOOR_S-14}px;width:{lw+80}px;height:34px"></div>
     {cast("lean", ll, lt, lw, lh)}
     <img id="lean" class="fig" src="assets/new/lean.png" style="left:{ll}px;top:{lt}px;width:{lw}px;height:{lh}px;opacity:0" alt="">
    </div>
    <div id="deskg" style="position:absolute;left:0;top:0;width:0;height:0">
     <div class="ground" style="left:{dl+30}px;top:{FLOOR_T-22}px;width:{dw-40}px;height:48px"></div>
     {cast("desk", dl, dt, dw, dh)}
     <img id="desk" class="fig" src="assets/new/desk.png" style="left:{dl}px;top:{dt}px;width:{dw}px;height:{dh}px" alt="">
    </div>
    <div id="bluecreep"></div>
    <div id="lline" style="position:absolute;left:560px;top:1255px;width:480px;height:5px;transform:rotate(-14deg);transform-origin:0 0;opacity:0;background:linear-gradient(90deg,rgba(255,226,170,0),rgba(255,226,170,.95),rgba(255,226,170,0));box-shadow:0 0 18px 4px rgba(255,214,140,.6)"></div>
    <div id="card3" class="cardspr" style="left:{460-130}px;top:1010px"><i style="position:absolute;left:24px;top:40px;width:150px;height:5px;background:#c8bba0;border-radius:3px"></i><i style="position:absolute;left:24px;top:70px;width:190px;height:5px;background:#c8bba0;border-radius:3px"></i><i style="position:absolute;left:24px;top:100px;width:110px;height:5px;background:#c8bba0;border-radius:3px"></i><i style="position:absolute;right:20px;bottom:18px;width:34px;height:34px;border-radius:50%;background:#b8333d;opacity:.8"></i></div>
    {sheets}
    <div id="c1" class="cardspr" style="left:{470-130}px;top:{1090-90}px"><span id="c1t">ini bukan<br>kisah cinta</span></div>
   </div>
   <div id="s2" class="layer"><div id="wrap2">
     <div id="wood"></div>
     <div class="s2i" style="left:70px;top:1330px;width:380px;height:280px;background:#f3e9d4;border:2px solid #d9c3a0;transform:rotate(-8deg);box-shadow:0 12px 20px rgba(0,0,0,.4)"><svg width="380" height="280" viewBox="0 0 380 280"><path d="M40 240 L40 120 L90 120 L90 70 L150 70 L150 40 L200 40 L200 120 L260 120 L260 240 Z M40 240 L340 240" fill="none" stroke="#8a8178" stroke-width="2"/></svg></div>
     <div class="s2i" style="left:820px;top:1370px;width:170px;height:170px;border-radius:50%;background:radial-gradient(circle,#2a211c 0 52%,#3f6aa0 53% 58%,#dbe8f4 59% 72%,#a9c6e3 73%);box-shadow:0 12px 20px rgba(0,0,0,.4)"></div>
     <div class="s2i" style="left:600px;top:1480px;width:300px;height:16px;border-radius:8px;background:linear-gradient(90deg,#2a211c 0 82%,#e3a43c 83%);transform:rotate(22deg);box-shadow:0 8px 12px rgba(0,0,0,.35)"></div>
     <div class="s2i" style="left:90px;top:230px;width:240px;height:170px;background:#efe3cf;border:2px solid #d9c3a0;transform:rotate(7deg);box-shadow:0 10px 18px rgba(0,0,0,.4)"></div>
     <div class="s2i" style="left:760px;top:250px;width:220px;height:150px;background:#dbe8f4;border:2px solid #a9c6e3;transform:rotate(-10deg);box-shadow:0 10px 18px rgba(0,0,0,.4)"></div>
     <div id="cardw"><div id="cardg" style="position:absolute;left:0;top:0;width:1080px;height:1920px">
       <div id="pr" class="pg"><svg id="sk2" width="490" height="680" viewBox="0 0 490 680">{sk2}</svg></div>
       <div id="pl" class="pg"><div class="ft" style="position:absolute;inset:0;backface-visibility:hidden"><div id="ttl">(500) Days of Summer</div><div id="yr">2009</div><div id="dir">MARC WEBB</div></div>
        <div class="bk" style="position:absolute;inset:0;transform:rotateY(180deg);backface-visibility:hidden;background:linear-gradient(135deg,#2a5a8f,#1d3a63);display:flex;align-items:center;justify-content:center"><em style="font-style:normal;font-family:'League Gothic',sans-serif;font-size:130px;color:#ffffff;letter-spacing:4px">500</em></div></div>
     </div></div>
   </div></div>
   <div class="layer grade"></div><div class="layer vign"></div><div id="leak" class="layer"></div><div id="white" class="layer"></div><div id="pagetear" class="layer"></div>
  </div>
  <div id="subgrad"></div><div id="sub"></div>
 </div>
{audio_html}
</div>
<script>{JS}</script>
</body></html>'''
open(f"{R}/index.html", "w").write(html); print("ok", len(html), dict(dl=dl, dt=dt, dw=dw, dh=dh, ll=ll, lt=lt, lw=lw, lh=lh))
