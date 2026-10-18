"""Generator index.html Elden Ring — tahap sketsa: pose statis tiap frame (animasi menyusul setelah disetujui)."""
import subprocess, os, math, random
R = random.Random(9)
GOLD, CREAM, CHAR, CRIM, NIGHT = "#C4A35A", "#E9DCC3", "#292B30", "#8A3434", "#24334A"
def vodur(n):
    f = f"assets/vo/{n:02d}.wav"
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))
D = [vodur(n) for n in range(1, 12)]
GAP, INTRO, TAIL = 0.4, 0.0, 2.0
LS, t = {}, 0.3
for n in range(1, 12): LS[n] = round(t, 2); t += D[n - 1] + GAP
TOTAL = round(LS[11] + D[10] + TAIL, 2)
ST = {n: (0 if n == 1 else round(LS[n] - GAP / 2, 2)) for n in range(1, 12)}
DUR = {n: round((ST[n + 1] if n < 11 else TOTAL) - ST[n], 2) for n in range(1, 12)}

SUB = {1: "Ia seorang dewi, ratu yang abadi.", 2: "Dulu, Lands Between diatur oleh Elden Ring dan Pohon Erdtree.", 3: "Lalu datang Night of Black Knives.",
       4: "Dalangnya adalah Ranni, sang Penyihir Rembulan.", 5: "Marika mengangkat palunya dan menghancurkan Elden Ring.", 6: "Para demigod berebut kekuasaan.",
       7: "Tapi sang ratu tak meninggalkan penjelasan.", 8: "Teori pertama: duka.", 9: "Teori kedua: pemberontakan.", 10: "Teori ketiga: rencana.", 11: "Mana yang benar?"}

def img(src, style, id_="", cls=""):
    i = f' id="{id_}"' if id_ else ""
    return f'<img{i} class="abs {cls}" src="assets/art/{src}.png" style="{style}">'
def bg(src, extra=""):
    return img(src, f"left:-70px;top:-40px;width:1220px;height:2000px;object-fit:cover;{extra}", cls="bg")
def tag(n, text, color):
    return f'<div class="abs theory"><span style="border-color:{color};color:{color}">{text}</span></div><div class="abs tframe" style="border-color:{color}"></div>'
def sub(n): return ''
def glow(x, y, r, color, op=.6, id_=''): return f'<div {"id=\""+id_+"\" " if id_ else ""}class="abs" style="left:{x-r}px;top:{y-r}px;width:{2*r}px;height:{2*r}px;border-radius:50%;background:radial-gradient(circle,{color},transparent 70%);opacity:{op}"></div>'
def particles(n, color=GOLD, y0=0, y1=1900, op=.7):
    return "".join(f'<i class="abs pt" style="left:{R.randint(20,1050)}px;top:{R.randint(y0,y1)}px;width:{(s:=R.choice([4,6,9]))}px;height:{s}px;background:{color};opacity:{op*R.uniform(.4,1):.2f}"></i>' for _ in range(n))

# ---------- shards untuk cincin pecah (clip-path poligon dari satu gambar) ----------
def shards(x, y, size, spread=1.0):
    cx = cy = 50; pieces = []
    pts = [(50, 50)]; k = 12
    for i in range(k):
        a0 = i * 360 / k + R.uniform(-8, 8); a1 = (i + 1) * 360 / k + R.uniform(-8, 8)
        r0, r1 = R.uniform(55, 62), R.uniform(55, 62)
        poly = [(50, 50), (50 + 70 * math.cos(math.radians(a0)), 50 + 70 * math.sin(math.radians(a0))), (50 + 70 * math.cos(math.radians((a0 + a1) / 2)), 50 + 75 * math.sin(math.radians((a0 + a1) / 2))), (50 + 70 * math.cos(math.radians(a1)), 50 + 70 * math.sin(math.radians(a1)))]
        mid = math.radians((a0 + a1) / 2); dx, dy = math.cos(mid) * R.uniform(14, 46) * spread, math.sin(mid) * R.uniform(14, 46) * spread
        rot = R.uniform(-14, 14) * spread
        clip = "polygon(" + ",".join(f"{px:.1f}% {py:.1f}%" for px, py in poly) + ")"
        pieces.append(f'<img class="abs shard" data-dx="{dx:.1f}" data-dy="{dy:.1f}" data-rot="{rot:.1f}" src="assets/art/elden-ring.png" style="left:{x+dx}px;top:{y+dy}px;width:{size}px;height:{size}px;clip-path:{clip};filter:drop-shadow(0 0 14px {GOLD}aa)">')
    return "".join(pieces)

F = {}
# 1 Hook
F[1] = (bg("erdtree-crown") + glow(540, 640, 520, GOLD, .55, 'f1-glow') +
        img("elden-ring", "left:190px;top:270px;width:700px;height:auto;filter:drop-shadow(0 0 40px #C4A35Acc)", "f1-ring") +
        img("marika-throne", "left:-60px;top:380px;height:1560px;width:auto;filter:drop-shadow(0 10px 40px #000a)", "f1-marika") + particles(40) +
        '<div id="f1-title" class="abs center cin" style="top:110px;font-size:70px;line-height:1.15;letter-spacing:.04em;color:#fff6dc;text-shadow:0 0 6px #000,0 4px 30px #000;padding:0 50px">Mengapa Ratu Marika<br>Menghancurkan<br><span style="color:#fff6dc;text-decoration:underline;text-decoration-color:#8A3434;text-underline-offset:10px">Elden Ring?</span></div>'
        '<div id="f1-warn" class="abs warn">⚠ SPOILER LORE</div>' + sub(1))
# 2 Golden Order
F[2] = (bg("bg-hall") + glow(540, 760, 480, GOLD, .5) +
        img("elden-ring", "left:240px;top:220px;width:600px;height:auto;opacity:.85;filter:drop-shadow(0 0 30px #C4A35Acc)", "f2-ring") +
        img("marika-throne", "left:140px;top:430px;height:1150px;width:auto;filter:drop-shadow(0 10px 30px #000a)", "f2-marika") + particles(50) +
        '<div class="abs center" style="top:104px"><span class="cin chap pill">GOLDEN ORDER</span></div>' + sub(2))
# 3 Night of Black Knives
F[3] = (bg("bg-night") + glow(540, 760, 380, "#E9DCC3", .22) +
        img("godwyn", "left:90px;top:420px;height:1180px;width:auto;filter:saturate(.75) brightness(.85) drop-shadow(0 10px 40px #000)", "f3-godwyn") +
        glow(560, 760, 200, GOLD, .55, 'f3-soul') +
        "".join(f'<div class="abs blade" style="left:{x}px;top:{y}px;transform:rotate({r}deg)"></div>' for x, y, r in [(-40, 470, 24), (700, 330, -28), (760, 760, -16)]) + particles(40, GOLD, 0, 1200, .5) +
        '<div class="abs center" style="top:104px"><span class="cin chap pill" style="color:#b9cdea">NIGHT OF BLACK KNIVES</span></div>' + sub(3))
# 4 Ranni
F[4] = (bg("bg-moon") +
        img("ranni", "left:-160px;top:610px;height:1180px;width:auto;filter:drop-shadow(0 10px 40px #000)", "f4-ranni") +
        img("two-fingers", "left:590px;top:-100px;width:480px;height:auto;filter:brightness(.85) drop-shadow(0 20px 60px #000)", "f4-fingers") + particles(30, "#cfe0ff", 0, 1300, .6) +
        '<div class="abs center" style="top:1330px"><span class="cin chap pill" style="color:#cfe0ff;font-size:44px">RANNI · TWO FINGERS</span></div>' + sub(4))
# 5 Shattering
F[5] = (bg("bg-hall", "filter:brightness(.55) saturate(.7)") + glow(540, 480, 560, CRIM, .45, 'f5-glow') +
        shards(180, 120, 720, 1.0) +
        '<svg class="abs" style="left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920"><g id="f5-cracks" stroke="#fff3c4" stroke-linecap="round" fill="none">' + "".join(f'<polyline class="crk" stroke-width="{R.choice([3,4,6])}" points="540,480 ' + " ".join(f"{540+math.cos(math.radians(a))*r+R.uniform(-30,30):.0f},{480+math.sin(math.radians(a))*r+R.uniform(-30,30):.0f}" for r in (110, 230, 360, 520)) + '"/>' for a in range(0, 360, 30)) + '</g></svg>' +
        img("marika-hammer", "left:-20px;top:420px;height:1500px;width:auto;filter:drop-shadow(0 10px 40px #000a)", "f5-marika") + particles(70, GOLD, 100, 1500, .9) +
        '<div class="abs center" style="top:104px"><span class="cin chap pill" style="color:#f3dfa6">THE SHATTERING</span></div>' + sub(5))
# 6 Perang demigod
pts = [(300, 560), (780, 520), (520, 760), (230, 900), (840, 880), (560, 1060)]
mapsvg = ('<svg class="abs" style="left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920">'
          f'<path id="f6-land" d="M140 560 Q260 420 520 470 Q820 430 940 640 Q1000 860 870 1040 Q700 1180 500 1160 Q240 1170 150 980 Q80 780 140 560Z" fill="#E9DCC31a" stroke="{CREAM}" stroke-opacity=".5" stroke-width="3" stroke-dasharray="14 10"/>'
          f'<path d="M520 600 L520 1060 M300 770 L780 770 M300 560 L840 880" stroke="{GOLD}" stroke-opacity=".25" stroke-width="2"/>'
          + "".join(f'<g class="dotg"><circle class="dglow" cx="{x}" cy="{y}" r="46" fill="#8A3434" fill-opacity=".35"/><circle class="dcore" cx="{x}" cy="{y}" r="16" fill="#e0523f"/><circle class="dring" cx="{x}" cy="{y}" r="30" fill="none" stroke="#e0523f" stroke-width="3" opacity=".6"/></g>' for x, y in pts)
          + f'<circle cx="540" cy="790" r="26" fill="none" stroke="{GOLD}" stroke-width="4"/><path d="M540 764 L540 700 M515 730 L565 730" stroke="{GOLD}" stroke-width="4"/></svg>')
F[6] = (bg("bg-battlefield", "filter:brightness(.8)") + mapsvg + particles(60, "#ff7a55", 300, 1500, .8) +
        '<div class="abs center" style="top:104px"><span class="cin chap pill" style="color:#f0a590">LANDS BETWEEN</span></div>' + sub(6))
# 7 Pertanyaan tanpa jawaban
F[7] = (bg("erdtree-roots", "filter:brightness(.75)") +
        img("marika-throne", "left:100px;top:210px;height:1000px;width:auto;filter:brightness(.62) saturate(.75) drop-shadow(0 10px 40px #000);mask-image:linear-gradient(180deg,#000 62%,transparent 98%);-webkit-mask-image:linear-gradient(180deg,#000 62%,transparent 98%)", "f7-marika") +
        glow(250, 1160, 120, "#E8A33C", .8, 'f7-g1') + glow(540, 1230, 120, "#C0392B", .8, 'f7-g2') + glow(830, 1160, 120, "#4C7DBE", .8, 'f7-g3') +
        '<div id="f7-t1" class="abs tl" style="left:150px;top:1230px;color:#E8A33C">DUKA</div><div id="f7-t2" class="abs tl" style="left:430px;top:1300px;color:#e0584a">BEBAS</div><div id="f7-t3" class="abs tl" style="left:710px;top:1230px;color:#7fa8e0">RENCANA</div>' +
        '<div class="abs center" style="top:104px"><span class="cin chap pill" style="font-size:42px">TANPA JAWABAN RESMI</span></div>' + sub(7))
# 8 Teori 1: Duka
F[8] = (bg("bg-hall", "filter:brightness(.5) saturate(.6) sepia(.3)") + glow(540, 900, 520, "#E8A33C", .3) +
        img("marika-throne", "left:-40px;top:330px;height:1200px;width:auto;filter:brightness(.9) drop-shadow(0 10px 40px #000)", "f8-marika") +
        img("godwyn", "left:520px;top:520px;height:900px;width:auto;opacity:.35;filter:blur(2px) saturate(.5)", "f8-godwyn") + particles(70, "#d9c39a", 0, 1500, .5) +
        tag(8, "TEORI 1 · DUKA", "#E8A33C") + sub(8))
# 9 Teori 2: Pemberontakan
chains = "".join(f'<path class="chain" d="{d}" fill="none" stroke="{GOLD}" stroke-width="7" stroke-dasharray="22 9" stroke-linecap="round" opacity=".9"/>' for d in ["M634 385 Q640 600 735 790", "M940 515 Q900 660 770 800", "M780 330 Q760 560 750 780"])
F[9] = (bg("bg-battlefield", "filter:brightness(.85)") +
        img("two-fingers", "left:590px;top:-190px;width:470px;height:auto;filter:brightness(.9) drop-shadow(0 20px 60px #000)", "f9-fingers") +
        f'<svg class="abs" style="left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920">{chains}</svg>' +
        img("marika-hammer", "left:-10px;top:440px;height:1450px;width:auto;filter:drop-shadow(0 10px 40px #000a)", "f9-marika") + particles(60, "#ff8a60", 200, 1500, .8) +
        tag(9, "TEORI 2 · PEMBERONTAKAN", "#e0584a") + sub(9))
# 10 Teori 3: Rencana
F[10] = (bg("erdtree-roots", "filter:brightness(.8) hue-rotate(-8deg)") + glow(540, 1050, 420, "#E9DCC3", .25) +
         f'<svg class="abs" style="left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920"><path id="f10-path" d="M540 1600 Q480 1300 560 1000 Q620 700 540 380" fill="none" stroke="{CREAM}" stroke-width="5" stroke-dasharray="4 14" stroke-linecap="round" opacity=".9"/>' + "".join(f'<circle cx="{x}" cy="{y}" r="12" fill="{GOLD}"/>' for x, y in [(560, 1000), (540, 380), (500, 1300)]) + '</svg>' +
         img("tarnished", "left:210px;top:830px;height:900px;width:auto;filter:drop-shadow(0 10px 40px #000)", "f10-tarn") + particles(60, "#cfe0ff", 0, 1500, .6) +
         tag(10, "TEORI 3 · RENCANA", "#7fa8e0") + sub(10))
# 11 Penutup
F[11] = (bg("erdtree-roots", "filter:brightness(.55) saturate(.8)") + glow(540, 420, 520, GOLD, .4) +
         shards(210, 70, 660, .45) +
         img("tarnished", "left:330px;top:1000px;height:780px;width:auto;filter:drop-shadow(0 10px 40px #000)", "f11-tarn") + particles(60) +
         '<div id="f11-title" class="abs center cin" style="top:740px;font-size:104px;line-height:1.1;text-shadow:0 4px 30px #000d">Mana yang<br><span style="color:#C4A35A">benar?</span></div>' + sub(11))

CSS = f'''
@font-face{{font-family:"Cinzel";font-weight:400;src:url(assets/fonts/cinzel-latin-400-normal.woff2) format("woff2")}}
@font-face{{font-family:"Cinzel";font-weight:700;src:url(assets/fonts/cinzel-latin-700-normal.woff2) format("woff2")}}
@font-face{{font-family:"Cinzel";font-weight:900;src:url(assets/fonts/cinzel-latin-900-normal.woff2) format("woff2")}}
@font-face{{font-family:"Inter";font-weight:700;src:url(assets/fonts/inter-latin-700-normal.woff2) format("woff2")}}
@font-face{{font-family:"Inter";font-weight:900;src:url(assets/fonts/inter-latin-900-normal.woff2) format("woff2")}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{margin:0;background:{CHAR}}}
#root{{position:relative;width:100%;height:100%;overflow:hidden;background:{CHAR};color:{CREAM};font-family:Inter,sans-serif}}
.scene{{position:absolute;inset:0;overflow:hidden;background:{CHAR}}}
.abs{{position:absolute}} .center{{left:0;right:0;text-align:center}}
.cin{{font-family:Cinzel,serif;font-weight:900;text-transform:uppercase}}
.chap{{font-size:50px;letter-spacing:.14em;color:#f3dfa6;text-shadow:0 2px 10px #000}}
.chap{{display:block}}
.vig{{position:absolute;inset:0;pointer-events:none;background:radial-gradient(ellipse at 50% 45%,transparent 50%,rgba(0,0,0,.65))}}
.pt{{border-radius:50%;box-shadow:0 0 10px currentColor}}
.warn{{left:50%;margin-left:-190px;width:380px;text-align:center;top:36px;padding:8px 0;border:3px solid {CRIM};color:#e9b0a8;background:#1a0d0dcc;font-family:Cinzel,serif;font-weight:700;font-size:30px;letter-spacing:.14em}}
.sub{{position:absolute;left:60px;right:60px;top:1500px;display:flex;justify-content:center}}
.sub span{{display:inline-block;padding:14px 30px;border-radius:14px;background:rgba(14,14,18,.8);color:{CREAM};text-align:center;font-weight:900;font-size:50px;line-height:1.2;max-width:960px}}
.blade{{width:560px;height:14px;background:linear-gradient(90deg,transparent,#0a0a10,#5b1a1a);box-shadow:0 0 30px #8A3434}}
.pill{{display:inline-block;padding:10px 30px;background:rgba(10,10,14,.72);border:2px solid #C4A35A66}}
.tl{{font-family:Cinzel,serif;font-weight:900;font-size:44px;letter-spacing:.08em;text-shadow:0 3px 20px #000}}
.theory{{left:0;right:0;top:104px;text-align:center}}
.theory span{{display:inline-block;padding:10px 30px;border:3px solid;background:#0c0c10cc;font-family:Cinzel,serif;font-weight:900;font-size:44px;letter-spacing:.1em}}
.tframe{{left:34px;right:34px;top:34px;bottom:34px;border:3px dashed;opacity:.75;pointer-events:none;border-radius:6px}}
'''
def scene(n):
    inner = F[n].replace('class="abs bg"', f'id="f{n}-bg" class="abs bg"', 1)
    return (f'<section id="f{n}" class="scene clip" data-start="{ST[n]}" data-duration="{DUR[n]}" data-track-index="1">{inner}<div class="vig"></div></section>')

TXT = {1: "Ia seorang dewi, ratu yang abadi. Namun suatu hari, Marika sendiri yang menghancurkan Elden Ring, sumber tatanan dunianya. Mengapa?",
 2: "Dulu, Lands Between diatur oleh Elden Ring dan Pohon Erdtree yang bersinar emas. Itulah Golden Order, dan Marika memerintah di puncaknya.",
 3: "Lalu datang Night of Black Knives. Bilah para pembunuh yang dikuatkan Rune of Death merenggut jiwa Godwyn, putra Marika.",
 4: "Dalangnya adalah Ranni, sang Penyihir Rembulan, yang ingin bebas dari kendali Two Fingers, utusan Greater Will.",
 5: "Tak lama kemudian, Marika mengangkat palunya dan menghancurkan Elden Ring. Pecahannya menjadi Great Rune.",
 6: "Para demigod, keturunan Marika, berebut kekuasaan, dan dunia tenggelam dalam perang yang disebut Shattering.",
 7: "Tapi sang ratu tak meninggalkan penjelasan. Game pun tak pernah menjawabnya. Yang tersisa hanya teori.",
 8: "Teori pertama: duka. Ia kehilangan putranya, dan tak sanggup menjaga tatanan yang gagal melindungi Godwyn.",
 9: "Teori kedua: pemberontakan. Marika muak menjadi alat Greater Will, lalu menghancurkan Elden Ring demi kebebasan.",
 10: "Teori ketiga: rencana. Kehancuran itu hanya awal, agar para Tarnished datang dan menentukan tatanan yang baru.",
 11: "Mana yang benar? Mungkin ketiganya, mungkin tak satu pun. Di antara reruntuhan, para Tarnished masih mencari jawabannya."}
import re
def phrases(text):
    raw = [p.strip() for p in re.findall(r"[^.,?:!]+[.,?:!]?", text) if p.strip()]
    out = []
    for p in raw:                                  # gabung frasa sangat pendek ke tetangga
        if out and len(out[-1]) < 22: out[-1] += " " + p
        else: out.append(p)
    return out
SUBS = []
for n in range(1, 12):
    ph = phrases(TXT[n]); tot = sum(len(p) for p in ph); tt = LS[n]
    for p in ph:
        d = D[n - 1] * len(p) / tot
        SUBS.append((round(tt, 2), round(d + (0.2 if p is ph[-1] else 0.05), 2), p)); tt += d
subhtml = "\n      ".join(f'<div class="sub clip" id="sub{i:02d}" data-start="{a}" data-duration="{d}" data-track-index="5"><span id="u{i:02d}">{p}</span></div>' for i, (a, d, p) in enumerate(SUBS, 1))
body = "\n      ".join(scene(n) for n in range(1, 12))
audio = "\n      ".join(f'<audio id="vo{n:02d}" src="assets/vo/{n:02d}.wav" data-start="{LS[n]}" data-track-index="7" data-volume="1"></audio>' for n in range(1, 12))
import json
if os.path.exists("assets/bgm.wav"): audio += f'\n      <audio id="bgm" src="assets/bgm.wav" data-start="0" data-duration="{TOTAL}" data-track-index="8" data-volume="0.55"></audio>'
sfx = json.load(open("assets/sfx/sfx.json")) if os.path.exists("assets/sfx/sfx.json") else []
for i, (nm, t_) in enumerate(sfx): audio += f'\n      <audio id="sfx{i:02d}" src="assets/sfx/{nm}.wav" data-start="{t_}" data-track-index="9" data-volume="0.85"></audio>'
JS = open("scripts/timeline.js").read().replace("__TIMING__", json.dumps({"LS": LS, "ST": ST, "DUR": DUR, "TOTAL": TOTAL, "D": D}))
html = f"""<!doctype html>
<html lang="id"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<title>Mengapa Ratu Marika Menghancurkan Elden Ring</title>
<script src="assets/gsap.min.js"></script><style>{CSS}</style></head>
<body><div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1080" data-height="1920">
      {body}
      {subhtml}
      {audio}
</div><script>{JS}</script></body></html>
"""
open("index.html", "w").write(html)
print("ok", TOTAL, "s", {n: (ST[n], DUR[n]) for n in range(1, 12)})
open("scripts/timing.json", "w").write(__import__("json").dumps({"LS": LS, "ST": ST, "DUR": DUR, "TOTAL": TOTAL, "D": D}))
