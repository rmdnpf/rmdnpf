#!/usr/bin/env python3
"""Bangun index.html (v2: aset ilustrasi). Dua panel dibuat dari SATU fungsi panel(); kamera & timing dari satu timeline.js."""
import shutil, os, json
import numpy as np
from PIL import Image
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
N = f"{R}/assets/new"; FIGDIR = f"{R}/assets/fig"
FLOOR = 1160                      # y lantai dunia (hasil perspektif plat: Tom 940 px tinggi, kaki di lantai kayu tengah-bawah)
TOM_H, SUM_H = 940, 874
KH = 1.45                          # skala sisipan tangan
RING_SRC = (574, 529)              # pusat cincin pada sumber hand (px)
RING_WORLD = (540, 790)

def info(path):
    a = np.array(Image.open(path)); al = a[..., 3] > 128
    ys, xs = np.where(al); h, w = a.shape[:2]
    bot = al[h - 50:]; bx = np.where(bot.any(0))[0]
    return w, h, bx

def foot_center(path, which="all"):
    w, h, _ = info(path); a = np.array(Image.open(path))[..., 3] > 128
    rows = a[h - 40:]; xs = np.where(rows.any(0))[0]
    if which == "left":                       # klaster paling kiri (kaki Tom pada gambar pelukan)
        gaps = np.where(np.diff(xs) > 25)[0]; xs = xs[: gaps[0] + 1] if len(gaps) else xs
    return float(xs.mean())

def img(side, name, srcpath, cx, k, extra="", cls="", anchor="all"):
    dst = f"{side}-{name}.png"; shutil.copy(srcpath, f"{N}/{dst}")
    w, h, _ = info(srcpath); ax = foot_center(srcpath, anchor)
    W, H = round(w * k), round(h * k); left = round(cx - ax * k); top = FLOOR - H
    return (f'<img id="{side}-{name}" class="fig {cls}" src="assets/new/{dst}" style="left:{left}px;top:{top}px;width:{W}px;height:{H}px;{extra}" alt="">', left, top, W, H)

def shadow(side, name, srcpath, cx, k, anchor="all"):
    dst = f"{side}-{name}-sh.png"; shutil.copy(srcpath, f"{N}/{dst}")
    w, h, _ = info(srcpath); ax = foot_center(srcpath, anchor)
    W, H = round(w * k), round(h * k); left = round(cx - ax * k); top = FLOOR - H
    ew = round(W * 0.62)
    return (f'<div id="{side}-shg-{name}" class="shg"><div class="ct" style="left:{round(cx)-ew//2}px;top:{FLOOR-22}px;width:{ew}px;height:44px"></div>'
            f'<img class="cast" src="assets/new/{dst}" style="left:{left}px;top:{FLOOR-H}px;width:{W}px;height:{H}px" alt=""></div>')

def hw(path): im = Image.open(path); return im.size

def panel(side, warm):
    tomp = f"{FIGDIR}/tom-stand.png"
    grp = f"{N}/greet.png"; hugp = f"{N}/{'hug-warm' if warm else 'hug-stiff'}.png"
    kt = TOM_H / hw(tomp)[1]; ks = SUM_H / hw(grp)[1]; kh = TOM_H / hw(hugp)[1]
    TOMX, SUMX, HUGX = 620, 880, 640
    tom = img(side, "tom", tomp, TOMX, kt, cls="tom")[0]
    sm = img(side, "sum", grp, SUMX, ks, cls="sum")[0]
    hg = img(side, "hug", hugp, HUGX, kh, cls="hug", anchor="left")[0]
    shs = shadow(side, "tom", tomp, TOMX, kt) + shadow(side, "sum", grp, SUMX, ks) + shadow(side, "hug", hugp, HUGX, kh, "left")
    shutil.copy(f"{N}/bg.jpg", f"{N}/{side}-bg.jpg")
    handsrc = "hand2x.jpg" if warm else "hand-ring2x.jpg"; shutil.copy(f"{N}/{handsrc}", f"{N}/{side}-hand.jpg")
    hw_, hh_ = 1182 * KH, 1330 * KH
    hl, ht = RING_WORLD[0] - RING_SRC[0] * KH, RING_WORLD[1] - RING_SRC[1] * KH
    shutil.copy(f"{N}/fg-plant.png", f"{N}/{side}-fg.png")
    bk = ""
    if warm:
        import random
        rnd = random.Random(11)
        bk = "".join(f'<div class="bk" style="left:{rnd.randint(520,1000)}px;top:{rnd.randint(250,1000)}px;width:{(s:=rnd.randint(40,100))}px;height:{s}px"></div>' for _ in range(14))
    ringx, ringy = RING_WORLD
    ring = ""
    if not warm:
        ring = (f'<svg id="{side}-glint" class="glint" viewBox="-100 -100 200 200" width="200" height="200" style="left:{ringx+4-100}px;top:{ringy-18-100}px">'
                '<defs><radialGradient id="gl"><stop offset="0" stop-color="#fff6d8" stop-opacity=".95"/><stop offset=".35" stop-color="#ffe49a" stop-opacity=".45"/><stop offset="1" stop-color="#ffd070" stop-opacity="0"/></radialGradient></defs>'
                '<circle r="60" fill="url(#gl)"/><path d="M0 -78 L5 -5 L78 0 L5 5 L0 78 L-5 5 L-78 0 L-5 -5Z" fill="#fff8e0" opacity=".9"/></svg>')
    return f'''
  <div id="{side}" class="panel {'warm' if warm else 'cool'}">
   <div id="{side}-in" class="layer">
    <div id="{side}-bg" class="layer"><div class="ceil"></div><img class="plate" src="assets/new/{side}-bg.jpg" style="left:-100px;top:0;width:1280px;height:1920px" alt=""></div>
    <div id="{side}-world" class="layer">
      <div id="{side}-glow" class="glow" style="left:{SUMX-260}px;top:{FLOOR-SUM_H-80}px;width:520px;height:{SUM_H+160}px"></div>
      {shs}{tom}{sm}{hg}
    </div>
    <div id="{side}-handw" class="layer handw">
      <img id="{side}-handimg" class="handimg" src="assets/new/{side}-hand.jpg" style="left:{hl:.0f}px;top:{ht:.0f}px;width:{hw_:.0f}px;height:{hh_:.0f}px" alt="">
      {ring}
    </div>
    <div id="{side}-fgw" class="layer"><img class="fgp" src="assets/new/{side}-fg.png" style="left:1000px;top:0;width:450px;height:1920px" alt=""></div>
    <div class="layer bokehs">{bk}</div>
    <div class="layer grade"></div>
    <div id="{side}-flash" class="layer flash"></div>
   </div>
   <div class="layer vign"></div>
   <div class="label">{'EKSPEKTASI' if warm else 'KENYATAAN'}</div>
  </div>'''

CSS = open(f"{R}/scripts/style.css").read(); JS = open(f"{R}/scripts/timeline.js").read()
html = f'''<!doctype html>
<html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=1080, height=1920">
<title>EVR Prototype v2</title>
<script src="assets/gsap.min.js"></script>
<style>{CSS}</style></head><body>
<div id="root" data-composition-id="evr" data-width="1080" data-height="1920" data-start="0" data-duration="9.5">
 <div id="stage" class="clip" data-start="0" data-duration="9.5" data-track-index="0">
{panel("L", True)}{panel("R", False)}
  <div id="split"></div>
  <div id="topgrad"></div>
  <div id="subgrad"></div>
  <div id="sub"></div>
 </div>
 <audio id="vo5" src="assets/vo/05.wav" data-start="0.05" data-duration="9.36" data-track-index="2" data-audio-group="voiceover" data-volume="1"></audio>
 <audio id="bgm" src="assets/bgm.wav" data-start="0" data-duration="9.5" data-track-index="3" data-volume="0.35"></audio>
 <audio id="sx1" src="assets/sfx/whoosh.wav" data-start="1.85" data-duration="0.7" data-track-index="4" data-volume="0.5"></audio>
 <audio id="sx2" src="assets/sfx/tick.wav" data-start="3.85" data-duration="0.06" data-track-index="5" data-volume="0.5"></audio>
 <audio id="sx3" src="assets/sfx/ding.wav" data-start="6.5" data-duration="1.4" data-track-index="6" data-volume="0.55"></audio>
 <audio id="sx4" src="assets/sfx/whoosh.wav" data-start="7.45" data-duration="0.7" data-track-index="7" data-volume="0.4"></audio>
</div>
<script>{JS}</script>
</body></html>'''
open(f"{R}/index.html", "w").write(html); print("ok", len(html))
