#!/usr/bin/env python3
"""Bangun prototypes/evr/index.html. Dua panel dibuat dari SATU fungsi panel() dan satu fungsi timeline,
sehingga kamera, blocking, dan timing identik secara konstruksi."""
import shutil, os
from PIL import Image
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = f"{R}/assets/fig"
FLOOR = 1500
TOM_H, SUM_H = 800, 745

def fig(side, name, src, x, h, cls=""):
    dst = f"{side}-{name}.png"            # salinan terpisah per panel (hindari duplicate media)
    shutil.copy(f"{FIG}/{src}.png", f"{FIG}/{dst}")
    w0, h0 = Image.open(f"{FIG}/{dst}").size
    w = round(w0 * h / h0)
    return (f'<img id="{side}-{name}" class="fig {cls}" src="assets/fig/{dst}" '
            f'style="left:{x - w//2}px;top:{FLOOR - h}px;width:{w}px;height:{h}px" alt="">'), w

def panel(side, warm):
    f = {}
    tom, tw = fig(side, "tom", "tom-stand", 410, TOM_H, "tom")
    sl, _ = fig(side, "sum-lean", "summer-lean-flip", 670, SUM_H, "sum")
    st, _ = fig(side, "sum-twirl", "summer-twirl-flip", 670, SUM_H + 20, "sum")
    sh = ""
    if warm:
        d1, _ = fig(side, "dance-a", "tom-dance", 285, 690, "dsh")
        d2, _ = fig(side, "dance-b", "tom-stand", 285, 800, "dsh")
        sh = d1 + d2
    guests = "".join(f'<div class="guest" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"></div>'
                     for x, y, w, h in [(360,900,120,600),(500,860,110,640),(850,930,130,570),(960,890,120,610),(300,950,100,550)])
    bokeh = ""
    if warm:
        import random
        rnd = random.Random(7)
        bokeh = "".join(f'<div class="bk" style="left:{rnd.randint(250,830)}px;top:{rnd.randint(250,900)}px;'
                        f'width:{(s:=rnd.randint(36,90))}px;height:{s}px"></div>' for _ in range(14))
    lights = "".join(f'<i class="bulb" style="left:{x}px;top:{300 + int(60*((x-540)/540)**2*-1)+60}px"></i>' for x in range(260, 840, 48))
    return f'''
  <div id="{side}" class="panel {'warm' if warm else 'cool'}">
   <div id="{side}-in" class="layer">
    <div id="{side}-bg" class="layer bg">
      <div class="wall"></div><div class="door"></div><div class="sky"></div>
      <div class="skyline"></div><div class="rail"></div>
      <div class="floor"></div>
      <div class="shaft s1"></div><div class="shaft s2"></div>
      {lights}
      <div id="{side}-guests" class="layer">{guests}</div>
      {sh}
    </div>
    <div id="{side}-world" class="layer world">
      <div id="{side}-shT" class="cshadow" style="left:{410-120}px;top:{FLOOR-26}px;width:240px;height:48px"></div>
      <div id="{side}-shS" class="cshadow" style="left:{670-110}px;top:{FLOOR-24}px;width:220px;height:44px"></div>
      {tom}{sl}{st}
      <div id="{side}-fg" class="layer"><div class="plant"></div></div>
      <svg id="{side}-hand" class="hand" viewBox="0 0 400 520" width="480" height="624" style="left:300px;top:{960-312}px">
        <defs><linearGradient id="{side}-sk" x1="0" x2="1"><stop offset="0" stop-color="#f0c9a4"/><stop offset="1" stop-color="#d9a77c"/></linearGradient></defs>
        <path d="M0 520 L40 300 Q60 230 120 220 L300 220 Q360 230 360 290 L400 520Z" fill="#1c1714"/>
        <g fill="url(#{side}-sk)">
          <rect x="90" y="40" width="46" height="230" rx="23" transform="rotate(-8 113 270)"/>
          <rect x="150" y="10" width="50" height="260" rx="25"/>
          <rect x="212" y="30" width="48" height="240" rx="24"/>
          <rect x="270" y="80" width="42" height="190" rx="21" transform="rotate(8 291 270)"/>
          <path d="M80 250 Q80 330 150 345 L290 345 Q330 330 320 250Z"/>
          <rect x="28" y="190" width="44" height="150" rx="22" transform="rotate(-35 50 340)"/>
        </g>
        <g class="ring" fill="none"><ellipse cx="236" cy="236" rx="34" ry="12" stroke="#e9b84a" stroke-width="12"/>
          <circle cx="236" cy="219" r="12" fill="#fff6d0"/></g>
        <path class="glint" d="M236 170 L244 212 L286 220 L244 228 L236 270 L228 228 L186 220 L228 212Z" fill="#fff6d0" opacity="0" style="filter:blur(1px)"/>
      </svg>
    </div>
    <div class="layer bokehs">{bokeh}</div>
    <div class="layer grade"></div>
   </div>
    <div class="layer vign"></div>
    <div class="label">{'EKSPEKTASI' if warm else 'KENYATAAN'}</div>
  </div>'''

CSS = open(f"{R}/scripts/style.css").read()
JS = open(f"{R}/scripts/timeline.js").read()
html = f'''<!doctype html>
<html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=1080, height=1920">
<title>EVR Prototype</title>
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
open(f"{R}/index.html", "w").write(html)
print("ok", len(html))
