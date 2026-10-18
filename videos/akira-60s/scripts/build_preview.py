"""Pratinjau statis 2 scene Akira (peringatan + hook/judul). Skyline = placeholder SVG sampai aset Gemini masuk."""
import random
R = random.Random(8)
PAPER, INK, RED, DRED, GREY = "#EFE6D2", "#111111", "#D7192D", "#8E0F1E", "#9A9488"
DOTS = lambda c, s=14, r=3: f"background-image:radial-gradient({c} {r}px,transparent {r+.5}px);background-size:{s}px {s}px"
def skyline():
    x, out = -20, ""
    while x < 1100:
        w = R.randint(60, 130); h = R.randint(120, 330); y = 1700 - h
        out += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{INK}"/>'
        for wy in range(y + 18, 1690, 34):
            for wx in range(x + 12, x + w - 12, 22):
                if R.random() < .35: out += f'<rect x="{wx}" y="{wy}" width="9" height="13" fill="{PAPER}"/>'
        if R.random() < .5: out += f'<rect x="{x + w//2 - 3}" y="{y - 60}" width="6" height="60" fill="{INK}"/>'
        x += w + R.randint(-6, 10)
    return f'<svg class="abs" style="left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920">{out}<rect x="0" y="1700" width="1080" height="220" fill="{INK}"/></svg>'
def grid():
    ls = "".join(f'<line x1="0" x2="1080" y1="{y}" y2="{y}"/>' for y in range(540, 1700, 90)) + "".join(f'<line y1="540" y2="1700" x1="{x}" x2="{x}"/>' for x in range(0, 1081, 90))
    return f'<svg class="abs" style="left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920"><g stroke="{INK}" stroke-opacity=".22" stroke-width="2">{ls}</g></svg>'
def radar(cx, cy):
    c = "".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{INK}" stroke-width="3" stroke-opacity=".5"/>' for r in (140, 280, 420))
    wedge = f'<path d="M{cx} {cy} L{cx+440} {cy-150} A465 465 0 0 1 {cx+360} {cy-290} Z" fill="{RED}" fill-opacity=".28"/>'
    return f'<svg class="abs" style="left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920">{c}{wedge}<line x1="{cx-440}" x2="{cx+440}" y1="{cy}" y2="{cy}" stroke="{INK}" stroke-opacity=".5" stroke-width="2"/><line y1="{cy-440}" y2="{cy+440}" x1="{cx}" x2="{cx}" stroke="{INK}" stroke-opacity=".5" stroke-width="2"/></svg>'
route = f'<svg class="abs" style="left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920"><polyline points="60,1560 230,1420 360,1450 470,1280 640,1260 760,1100 900,1070" fill="none" stroke="{RED}" stroke-width="12" stroke-linejoin="round" stroke-linecap="round"/>' + "".join(f'<circle cx="{x}" cy="{y}" r="16" fill="{PAPER}" stroke="{RED}" stroke-width="8"/>' for x, y in [(60,1560),(360,1450),(640,1260),(900,1070)]) + '</svg>'
def alt(p=.12):
    y0, y1 = 1300, 640; y = y1 + (y0 - y1) * (1 - p)
    return (f'<svg class="abs" style="left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920"><rect x="1018" y="{y1}" width="22" height="{y0-y1}" fill="none" stroke="{INK}" stroke-width="4"/>'
            f'<rect x="1018" y="{y}" width="22" height="{y0-y}" fill="{RED}"/><text x="1029" y="{y1-26}" text-anchor="middle" font-family="League Gothic" font-size="40" fill="{INK}">KUASA</text>'
            f'<text x="1029" y="{y0+54}" text-anchor="middle" font-family="League Gothic" font-size="40" fill="{INK}">KENDALI</text></svg>')
hazard = lambda y: f'<div class="abs" style="left:0;top:{y}px;width:1080px;height:70px;background:repeating-linear-gradient(-45deg,{INK} 0 40px,{RED} 40px 80px)"></div>'
timer = lambda t, c=INK: f'<div class="abs center disp" style="top:70px;font-size:230px;color:{c};letter-spacing:.02em"><span style="display:inline-block;padding:0 26px;border:10px solid {c}">{t}</span></div>'
sub = lambda t: f'<div class="sub"><span>{t}</span></div>'

A = (f'<div class="abs" style="inset:0;{DOTS(INK+"22",18,3)}"></div>' + hazard(0) + hazard(1850) + timer("00:60") +
     f'<div class="abs center disp" style="top:470px;font-size:190px;color:{INK};letter-spacing:.06em">PERINGATAN</div>'
     f'<div class="abs" style="left:-40px;right:-40px;top:700px;height:420px;background:{RED};transform:rotate(-4deg)"></div>'
     f'<div class="abs" style="left:-40px;right:-40px;top:700px;height:420px;transform:rotate(-4deg);{DOTS(DRED,16,4)};opacity:.55"></div>'
     f'<div class="abs center disp" style="top:740px;font-size:380px;color:{PAPER};transform:rotate(-4deg);text-shadow:10px 10px 0 {INK}">SPOILER</div>'
     f'<div class="abs center" style="top:1250px;font-size:56px;font-weight:900;color:{INK};padding:0 90px">Film ini dibahas sampai twist.<br>Lanjut dengan risiko sendiri.</div>')
B = (grid() + radar(300, 1200) + route + skyline() +
     f'<div class="abs" style="left:-60px;top:330px;width:1200px;height:470px;background:{RED};transform:skewY(-4deg)"></div>'
     f'<div class="abs" style="left:-60px;top:330px;width:1200px;height:470px;transform:skewY(-4deg);{DOTS(DRED,16,4)};opacity:.5"></div>'
     f'<div class="abs center disp" style="top:300px;font-size:520px;color:{PAPER};text-shadow:12px 12px 0 {INK};letter-spacing:.02em">AKIRA</div>'
     f'<div class="abs disp" style="left:60px;top:850px;font-size:150px;letter-spacing:.06em;color:{INK};line-height:.9">1988</div><div class="abs disp" style="left:60px;top:990px;font-size:62px;letter-spacing:.1em;color:{PAPER};background:{INK};padding:8px 22px">KATSUHIRO OTOMO</div>'
     + timer("00:57") +
     '<img class="abs" src="assets/art/kaneda-standing.png" style="left:420px;top:790px;height:920px;width:auto;filter:drop-shadow(14px 0 0 #111)">'
     + alt(.14) + sub("Enam puluh detik untuk memahami film ini."))
CSS = f'''*{{margin:0;padding:0;box-sizing:border-box}}html,body{{margin:0;background:{PAPER}}}
#root{{position:relative;width:100%;height:100%;overflow:hidden;background:{PAPER};color:{INK};font-family:Inter,sans-serif}}
.scene{{position:absolute;inset:0;overflow:hidden;background:{PAPER}}}.abs{{position:absolute}}.center{{left:0;right:0;text-align:center}}
.disp{{font-family:"League Gothic",sans-serif;text-transform:uppercase;line-height:.92}}
.sub{{position:absolute;left:50px;right:50px;top:1740px;display:flex;justify-content:center}}
.sub span{{display:inline-block;padding:14px 30px;background:{INK};color:{PAPER};text-align:center;font-weight:900;font-size:52px;line-height:1.2;max-width:960px}}'''
html = f'''<!doctype html><html lang="id"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/><title>Akira pratinjau</title>
<script src="assets/gsap.min.js"></script><style>{CSS}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="8" data-width="1080" data-height="1920">
<section id="a" class="scene clip" data-start="0" data-duration="2.5" data-track-index="1">{A}</section>
<section id="b" class="scene clip" data-start="2.5" data-duration="5.5" data-track-index="1">{B}</section></div>
<script>window.__timelines=window.__timelines||{{}};window.__timelines["main"]=gsap.timeline({{paused:true}});</script></body></html>'''
open("index.html", "w").write(html); print("ok")
