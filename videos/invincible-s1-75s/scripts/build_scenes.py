"""Generator index.html Invincible S1 — tahap sketsa: pose statis tiap frame (animasi menyusul setelah disetujui)."""
import os, subprocess, math, random
R = random.Random(4)
NAVY, YEL, RED, CREAM = "#0B1230", "#F2C230", "#B3202A", "#E9DCC3"
NOM = [8, 7, 7, 9, 9, 9, 8, 9, 8, 8]     # durasi nominal bila VO belum ada

def vodur(n):
    f = f"assets/vo/{n:02d}.wav"
    if os.path.exists(f):
        return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))
    return NOM[n - 1] - 0.6
D = [vodur(n) for n in range(1, 11)]
HAS_VO = all(os.path.exists(f"assets/vo/{n:02d}.wav") for n in range(1, 11))
GAP = 0.4
LS, t = {}, 0.3
for n in range(1, 11): LS[n] = round(t, 2); t += D[n - 1] + GAP
TOTAL = round(LS[10] + D[9] + 2.0, 2)
ST = {n: (0 if n == 1 else round(LS[n] - GAP / 2, 2)) for n in range(1, 11)}
DUR = {n: round((ST[n + 1] if n < 10 else TOTAL) - ST[n], 2) for n in range(1, 11)}

SUB = {1: "Seorang ayah yang menjadi pahlawan paling kuat di Bumi.", 2: "Invincible, serial animasi karya Robert Kirkman.", 3: "Mark Grayson, remaja tujuh belas tahun.",
       4: "Mark ingin mengikuti jejak sang ayah.", 5: "Seluruh Guardians of the Globe terbunuh.", 6: "Kisah asal-usul Omni-Man ternyata bohong.",
       7: "Ia berasal dari Viltrum.", 8: "Mark menolak. Ayah dan anak bertarung.", 9: "Pesannya sederhana dan menyakitkan.", 10: "Memilih siapa dirinya, bukan siapa ayahnya."}

def img(src, style, id_="", cls=""):
    i = f' id="{id_}"' if id_ else ""
    return f'<img{i} class="abs {cls}" src="assets/art/{src}.png" style="{style}">'
def wide_bg(src, left, extra="", id_=""):          # latar landscape: tinggi 1920, bisa di-pan horizontal
    return img(src, f"left:{left}px;top:0;height:1920px;width:auto;max-width:none;{extra}", id_, "bg")
def tall_bg(src, extra="", id_=""):
    return img(src, f"left:-30px;top:-20px;width:1140px;height:1960px;object-fit:cover;{extra}", id_, "bg")
def alt(p, label, color=YEL, pid=""):
    """altimeter vertikal di tepi kanan; p = 0 (bawah) .. 1 (atas)"""
    y0, y1 = 1380, 260; y = y1 + (y0 - y1) * (1 - p)
    ticks = "".join(f'<line x1="1040" x2="{1056 if i % 5 else 1070}" y1="{y1 + i * (y0 - y1) / 20}" y2="{y1 + i * (y0 - y1) / 20}" stroke="{CREAM}" stroke-opacity=".55" stroke-width="3"/>' for i in range(21))
    return (f'<svg id="{pid}" class="abs" style="left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920">'
            f'<line x1="1048" x2="1048" y1="{y1}" y2="{y0}" stroke="{CREAM}" stroke-opacity=".5" stroke-width="3"/>{ticks}'
            f'<g class="alt-mark"><path d="M1030 {y} L1006 {y-14} L1006 {y+14} Z" fill="{color}"/><rect x="800" y="{y-28}" width="198" height="56" fill="#0B1230" fill-opacity=".85" stroke="{color}" stroke-width="3"/>'
            f'<text x="899" y="{y+13}" text-anchor="middle" font-family="League Gothic, sans-serif" font-size="46" letter-spacing="2" fill="{color}">{label}</text></g></svg>')
def frame_svg(x, y, w, h, color=CREAM, extra=""):
    return (f'<svg class="abs" style="left:{x-26}px;top:{y-26}px" width="{w+52}" height="{h+52}" viewBox="0 0 {w+52} {h+52}">'
            f'<rect x="8" y="8" width="{w+36}" height="{h+36}" rx="6" fill="none" stroke="{color}" stroke-width="14"/>'
            f'<rect x="26" y="26" width="{w}" height="{h}" fill="none" stroke="{color}" stroke-opacity=".55" stroke-width="3"/>{extra}</svg>')
def cracks(cx, cy, n=9, r0=60, r1=520, seed=1, color=CREAM, wd=4):
    rr = random.Random(seed); out = ""
    for k in range(n):
        a = k * 360 / n + rr.uniform(-12, 12); pts = [(cx, cy)]
        for j in range(1, 5):
            rad = r0 + (r1 - r0) * j / 4; pts.append((cx + math.cos(math.radians(a + rr.uniform(-14, 14))) * rad, cy + math.sin(math.radians(a + rr.uniform(-14, 14))) * rad))
        out += '<polyline class="crk" points="' + " ".join(f"{x:.0f},{y:.0f}" for x, y in pts) + f'" fill="none" stroke="{color}" stroke-width="{rr.choice([wd-1, wd, wd+2])}" stroke-linecap="round"/>'
    return out
def particles(n, color=CREAM, y0=0, y1=1500, op=.6):
    return "".join(f'<i class="abs pt" style="left:{R.randint(20,1000)}px;top:{R.randint(y0,y1)}px;width:{(s:=R.choice([4,6,8]))}px;height:{s}px;background:{color};opacity:{op*R.uniform(.4,1):.2f}"></i>' for _ in range(n))
def tagchip(text, x, y, color=YEL, size=46):
    return f'<div class="abs chip" style="left:{x}px;top:{y}px;border-color:{color};color:{color};font-size:{size}px">{text}</div>'
def sub(n): return f'<div class="sub"><span>{SUB[n]}</span></div>' if not HAS_VO else ""


# dinding bingkai: bukaan bingkai tengah di photo-wall.png (1536x1024) = (653,313)-(915,638); pusatnya diselaraskan ke layar
WS = 2.44; WCX, WCY = 784, 475.5; WL = round(540 - WCX * WS); WT = round(840 - WCY * WS)
FX0, FY0 = round(WL + 653 * WS), round(WT + 313 * WS); FW, FH = round(262 * WS), round(325 * WS)
def wall_framed(extra="", id_=""):
    return img("photo-wall", f"left:{WL}px;top:{WT}px;width:{round(1536*WS)}px;height:auto;max-width:none;{extra}", id_, "bg")
def in_frame(inner, id_="", cls=""):
    return f'<div id="{id_}" class="abs {cls}" style="left:{FX0}px;top:{FY0}px;width:{FW}px;height:{FH}px;overflow:hidden">{inner}</div>'

F = {}
# 1 Hook
F[1] = (wall_framed("filter:brightness(.7)", "f1-bg") + particles(20) +
        in_frame('<img id="f1-photo" src="assets/art/family-photo.png" style="width:100%;height:100%;object-fit:cover;display:block">', "f1-fwrap") +
        f'<svg id="f1-crack" class="abs" style="left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920"><g stroke="{CREAM}" stroke-width="4" fill="none" stroke-linecap="round"><polyline class="crk" points="{FX0+FW},{FY0} {FX0+FW-70},{FY0+90} {FX0+FW-40},{FY0+170}"/><polyline class="crk" points="{FX0+FW-70},{FY0+90} {FX0+FW-150},{FY0+110}"/></g></svg>' +
        '<div id="f1-warn" class="abs warn">⚠ SPOILER</div>' + alt(.03, "0 M", pid="f1-alt") + sub(1))
# 2 Judul
F[2] = (wide_bg("photo-wall", -900, "filter:brightness(.8)", "f2-bg") + particles(24) +
        '<div id="f2-title" class="abs center disp" style="top:620px;font-size:330px;color:#E9DCC3;text-shadow:0 6px 40px #000c">INVINCIBLE</div>'
        f'<div id="f2-line" class="abs" style="left:140px;top:950px;width:800px;height:14px;background:{YEL}"></div>'
        f'<div id="f2-sub" class="abs center disp" style="top:990px;font-size:90px;letter-spacing:.2em;color:{YEL}">SEASON 1 · 2021</div>' + alt(.06, "0 M", pid="f2-alt") + sub(2))
# 3 Mark
F[3] = (tall_bg("mark-standing", "", "f3-bg") + tagchip("MARK GRAYSON", 90, 1250, YEL, 64) +
        '<div class="abs mono" style="left:96px;top:1340px;font-size:34px;letter-spacing:.12em;color:#E9DCC3;text-shadow:0 2px 12px #000">17 TAHUN · PUTRA OMNI-MAN</div>' + alt(.14, "100 M", pid="f3-alt") + sub(3))
# 4 Terbang
speed = "".join(f'<line x1="{x}" y1="{y}" x2="{x+8}" y2="{y+R.randint(160,360)}" stroke="{CREAM}" stroke-opacity=".28" stroke-width="3"/>' for x, y in [(R.randint(40,980), R.randint(0,1400)) for _ in range(18)])
F[4] = (tall_bg(os.environ.get("SKY4","sky-day"), "", "f4-bg") +
        f'<svg class="abs" style="left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920">{speed}</svg>' +
        img("mark-flying", "left:30px;top:760px;height:760px;width:auto", "f4-mark") + img("omni-flying", "left:310px;top:200px;height:1180px;width:auto", "f4-omni") +
        alt(.4, "2.000 M", pid="f4-alt") + sub(4))
# 5 Guardians tewas
F[5] = (wide_bg("city-wreck", -900, "filter:brightness(.8)", "f5-bg") + '<div id="f5-red" class="abs" style="inset:0;background:radial-gradient(ellipse at 50% 80%,#B3202A66,transparent 70%)"></div>' +
        img("guardians-group", "left:-90px;top:640px;width:1260px;height:auto;filter:brightness(.45) saturate(.7);transform:rotate(-7deg)", "f5-guard") +
        img("omni-standing", "left:150px;top:470px;height:1080px;width:auto;filter:drop-shadow(0 0 40px #B3202A)", "f5-omni") + particles(30, "#f25a4a", 200, 1400, .7) +
        alt(.5, "—", RED, "f5-alt") + sub(5))
# 6 Foto pecah
LEFT = "polygon(0 0,56% 0,61% 18%,54% 40%,61% 66%,55% 100%,0 100%)"; RIGHT = "polygon(56% 0,100% 0,100% 100%,55% 100%,61% 66%,54% 40%,61% 18%)"
F[6] = (wall_framed("filter:brightness(.5)", "f6-bg") +
        in_frame('<img id="f6-left" class="abs" src="assets/art/family-photo.png" style="left:0;top:0;width:100%;height:100%;object-fit:cover;clip-path:' + LEFT + '">', "f6-fwrapL") +
        f'<div id="f6-fwrapR" class="abs" style="left:{FX0}px;top:{FY0}px;width:{FW}px;height:{FH}px"><img id="f6-right" class="abs" src="assets/art/family-photo.png" style="left:34px;top:-18px;width:100%;height:100%;object-fit:cover;clip-path:{RIGHT};filter:brightness(.35) saturate(.7)"></div>' +
        f'<svg id="f6-cracks" class="abs" style="left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920"><g>{cracks(FX0 + round(FW*.58), FY0 + round(FH*.42), 8, 30, 360, 6, CREAM, 5)}</g>'
        + "".join(f'<polygon class="shard" points="{x},{y} {x+60},{y+24} {x+18},{y+76}" fill="{CREAM}" fill-opacity=".18" stroke="{CREAM}" stroke-width="3"/>' for x, y in [(FX0+30, FY0+FH+30), (FX0+FW-120, FY0+FH+60), (FX0+200, FY0-60), (FX0+FW+20, FY0+FH-120)]) + '</svg>' +
        alt(.7, "30.000 M", pid="f6-alt") + sub(6))
# 7 Viltrum# 7 Viltrum
fleet = "".join(f'<path class="ship" d="M{x} {y} L{x+34} {y+64} L{x} {y+46} L{x-34} {y+64} Z" fill="#0B1230" stroke="{RED}" stroke-width="3"/>' for x, y in [(270, 700), (400, 640), (540, 760), (680, 640), (810, 700), (470, 860), (610, 880)])
F[7] = (tall_bg("space-bg", "", "f7-bg") +
        f'<svg class="abs" style="left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920"><g id="f7-sym" transform="translate(540 380)"><circle r="190" fill="none" stroke="{RED}" stroke-width="10"/><circle r="150" fill="{RED}" fill-opacity=".14" stroke="{RED}" stroke-width="4" stroke-dasharray="14 10"/><path d="M-90 -80 L0 90 L90 -80 L50 -80 L0 20 L-50 -80 Z" fill="{RED}"/></g>{fleet}</svg>' +
        f'<div id="f7-name" class="abs center disp" style="top:620px;font-size:110px;letter-spacing:.3em;color:{RED};text-shadow:0 0 30px #000">VILTRUM</div>' + alt(.9, "100 KM", pid="f7-alt") + sub(7))
# 8 Pertarungan
F[8] = (tall_bg("sky-day", "filter:brightness(.8) hue-rotate(10deg)", "f8-bg") +
        f'<svg class="abs" style="left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920"><g id="f8-wave" fill="none" stroke="{YEL}" stroke-width="6"><circle cx="420" cy="860" r="110" stroke-opacity=".9"/><circle cx="420" cy="860" r="190" stroke-opacity=".55"/><circle cx="420" cy="860" r="280" stroke-opacity=".3"/></g></svg>' +
        img("omni-flying", "left:440px;top:90px;height:980px;width:auto", "f8-omni") + img("mark-flying", "left:20px;top:980px;height:640px;width:auto;transform:rotate(150deg)", "f8-mark") +
        f'<svg id="f8-tear" class="abs" style="left:560px;top:760px" width="50" height="80" viewBox="0 0 50 80"><path d="M25 4 C25 4 4 40 4 54 A21 21 0 0 0 46 54 C46 40 25 4 25 4Z" fill="#9fb4ff" stroke="{CREAM}" stroke-width="3"/></svg>' +
        alt(.6, "ANGKASA", pid="f8-alt") + sub(8))
# 9 Tafsiran
F[9] = (wall_framed("filter:brightness(.55)", "f9-bg") +
        in_frame('<img id="f9-omni" class="abs" src="assets/art/omni-standing.png" style="left:' + str(round(FW*0.42)) + 'px;top:40px;height:' + str(round(FH*0.95)) + 'px;width:auto"><img id="f9-mark" class="abs" src="assets/art/mark-standing2.png" style="left:-40px;top:150px;height:' + str(round(FH*0.78)) + 'px;width:auto">', "f9-fwrap") +
        f'<svg id="f9-crack" class="abs" style="left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920"><g>{cracks(FX0 + round(FW*.46), FY0 + round(FH*.5), 5, 20, 260, 12, CREAM, 4)}</g></svg>' +
        '<div class="abs theory"><span>TAFSIRAN</span></div><div class="abs tframe"></div>' + sub(9))
# 10 Penutup# 10 Penutup
F[10] = (tall_bg("mark-standing", "filter:brightness(.7);top:250px", "f10-bg") +
         f'<div id="f10-title" class="abs center disp" style="top:90px;font-size:190px;color:{YEL};text-shadow:0 6px 40px #000">SIAPA DIRIMU?</div>' + alt(.14, "100 M", pid="f10-alt") +
         '<div class="abs theory" style="top:1100px;opacity:0"><span>TAFSIRAN</span></div>' + sub(10))

CSS = f'''
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{margin:0;background:{NAVY}}}
#root{{position:relative;width:100%;height:100%;overflow:hidden;background:{NAVY};color:{CREAM};font-family:Inter,sans-serif}}
.scene{{position:absolute;inset:0;overflow:hidden;background:{NAVY}}}
.abs{{position:absolute}} .center{{left:0;right:0;text-align:center}}
.disp{{font-family:"League Gothic",sans-serif;text-transform:uppercase;line-height:.92;letter-spacing:.01em}}
.mono{{font-family:Inter,sans-serif;font-weight:700}}
.vig{{position:absolute;inset:0;pointer-events:none;background:radial-gradient(ellipse at 50% 45%,transparent 55%,rgba(0,0,0,.6))}}
.pt{{border-radius:50%}}
.warn{{left:50%;margin-left:-150px;width:300px;top:70px;text-align:center;padding:8px 0;border:3px solid {RED};color:#f3b5ac;background:#14080acc;font-family:"League Gothic",sans-serif;font-size:44px;letter-spacing:.2em}}
.chip{{padding:8px 26px;border:4px solid;background:#0B1230d9;font-family:"League Gothic",sans-serif;letter-spacing:.06em}}
.sub{{position:absolute;left:60px;right:60px;top:1500px;display:flex;justify-content:center}}
.sub span{{display:inline-block;padding:14px 30px;border-radius:14px;background:rgba(11,18,48,.82);color:{CREAM};text-align:center;font-weight:900;font-size:50px;line-height:1.2;max-width:960px}}
.theory{{left:0;right:0;top:120px;text-align:center}}
.theory span{{display:inline-block;padding:8px 30px;border:3px dashed {CREAM};background:#0B1230cc;font-family:"League Gothic",sans-serif;font-size:56px;letter-spacing:.2em}}
.tframe{{left:34px;right:34px;top:34px;bottom:34px;border:3px dashed {CREAM};opacity:.55;pointer-events:none}}
'''
def scene(n):
    return f'<section id="f{n}" class="scene clip" data-start="{ST[n]}" data-duration="{DUR[n]}" data-track-index="1">{F[n]}<div class="vig"></div></section>'
body = "\n      ".join(scene(n) for n in range(1, 11))
audio = "\n      ".join(f'<audio id="vo{n:02d}" src="assets/vo/{n:02d}.wav" data-start="{LS[n]}" data-track-index="7" data-volume="1"></audio>' for n in range(1, 11) if os.path.exists(f"assets/vo/{n:02d}.wav"))
html = f"""<!doctype html>
<html lang="id"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<title>Invincible Season 1</title>
<script src="assets/gsap.min.js"></script><style>{CSS}</style></head>
<body><div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1080" data-height="1920">
      {body}
      {audio}
</div><script>window.__timelines=window.__timelines||{{}};window.__timelines["main"]=gsap.timeline({{paused:true}});</script></body></html>
"""
open("index.html", "w").write(html)
import json; json.dump({"LS": LS, "ST": ST, "DUR": DUR, "TOTAL": TOTAL, "D": D}, open("scripts/timing.json", "w"))
print("ok", TOTAL, "s", {n: (ST[n], DUR[n]) for n in range(1, 11)})
