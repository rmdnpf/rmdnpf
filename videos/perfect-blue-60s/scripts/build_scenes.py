"""Generator index.html Perfect Blue (pose statis tiap frame; animasi ditambahkan di tahap build)."""
import random, math
R = random.Random(5)
NAVY, PANEL, BLUE, PINK, RED, PAPER = "#0b1230", "#141c46", "#2f5bff", "#ff5fa2", "#e5233b", "#f2f0ff"

import subprocess, json, os
def vodur(n):
    f = f"assets/vo/{n:02d}.wav"
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]).decode()) if os.path.exists(f) else [4.6, 6.8, 7.5, 8.5, 9.0, 7.4, 9.8][n - 1]
DUR = [vodur(n) for n in range(1, 8)]
INTRO, GAP, TAIL = 2.2, 0.4, 1.7
LS = {}; t = INTRO
for n in range(1, 8):
    LS[n] = round(t, 2); t += DUR[n - 1] + GAP
LEND = round(LS[7] + DUR[6], 2); TOTAL = round(LEND + TAIL, 2)
# batas scene = tengah jeda antar baris
bounds = [0, INTRO] + [round(LS[n] - GAP / 2 + 0.0, 2) for n in range(2, 8)] + [round(LS[7] - GAP / 2, 2)]
ST = {"f1": 0, "f2": INTRO, "f3": round(LS[2] - 0.2, 2), "f4": round(LS[3] - 0.2, 2), "f5": round(LS[4] - 0.2, 2), "f6": round(LS[5] - 0.2, 2), "f7": round(LS[6] - 0.2, 2), "f8": round(LS[7] - 0.2, 2)}
order = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8"]
SCENES = [(k, ST[k], round((ST[order[i + 1]] if i < 7 else TOTAL) - ST[k], 2)) for i, k in enumerate(order)]

CURSOR = f'<svg class="cursor" width="64" height="90" viewBox="0 0 34 50"><path d="M2 2 L2 40 L12 31 L19 47 L26 44 L19 28 L33 28 Z" fill="{PAPER}" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/></svg>'

def win(id_, x, y, w, h, title, body, bar=BLUE, extra=""):
    return (f'<div id="{id_}" class="win" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;{extra}">'
            f'<div class="bar" style="background:linear-gradient(90deg,{bar},{BLUE}aa)"><span>{title}</span>'
            f'<span class="ctl"><i></i><i></i><i style="background:{PINK}"></i></span></div>'
            f'<div class="body">{body}</div></div>')

def icon(kind, x, y, rot, s=1.0):
    shapes = {
        "file": f'<path d="M6 4 H30 L42 16 V54 H6 Z" fill="{PAPER}" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/><path d="M30 4 V16 H42" fill="none" stroke="{NAVY}" stroke-width="4"/><path d="M14 30 H34 M14 40 H34" stroke="{BLUE}" stroke-width="4"/>',
        "folder": f'<path d="M4 14 H20 L26 20 H48 V50 H4 Z" fill="{PINK}" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/>',
        "disk": f'<path d="M4 4 H40 L48 12 V50 H4 Z" fill="{BLUE}" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/><rect x="12" y="4" width="22" height="16" fill="{PAPER}" stroke="{NAVY}" stroke-width="3"/><rect x="12" y="32" width="28" height="18" fill="{NAVY}"/>',
    }[kind]
    return f'<svg class="abs icon" style="left:{x}px;top:{y}px" width="{int(60*s)}" height="{int(60*s)}" viewBox="0 0 52 56">{shapes}</svg>'

def star(x, y, s, op=0.9):
    return (f'<svg class="abs" style="left:{x}px;top:{y}px;opacity:{op}" width="{s}" height="{s}" viewBox="-50 -50 100 100">'
            f'<path d="M0 -50 L7 -7 L50 0 L7 7 L0 50 L-7 7 L-50 0 L-7 -7 Z" fill="#fff"/></svg>')

def person(cx, base, scale, fill, stroke, arms=True, op=1):
    h = 300 * scale
    head = 36 * scale
    arm = (f'<path d="M{cx-34*scale} {base-h*0.62} L{cx-120*scale} {base-h*0.9} M{cx+34*scale} {base-h*0.62} L{cx+120*scale} {base-h*0.95}" stroke="{stroke}" stroke-width="{16*scale}" stroke-linecap="round" fill="none"/>' if arms else "")
    return (f'<g opacity="{op}">{arm}<path d="M{cx-44*scale} {base-h*0.66} Q{cx} {base-h*0.72} {cx+44*scale} {base-h*0.66} L{cx+84*scale} {base} L{cx-84*scale} {base} Z" fill="{fill}" stroke="{stroke}" stroke-width="5"/>'
            f'<circle cx="{cx}" cy="{base-h*0.82}" r="{head}" fill="{fill}" stroke="{stroke}" stroke-width="5"/></g>')


def tsp(text):
    return "".join(f'<span class="ch">{c}</span>' if c != " " else " " for c in text)

def cur(id_, style):
    return CURSOR.replace('class="cursor"', f'id="{id_}" class="cursor abs" style="{style}"')

# ================= F1 =================
f1 = f"""
<div class="grid"></div>
<div class="abs mono" style="left:60px;top:150px;font-size:32px;opacity:.75">● REC &nbsp; PERFECT_BLUE.TAPE &nbsp; 00:00:01</div>
<div class="abs mono" style="right:60px;top:150px;font-size:32px;opacity:.75;color:{PINK}">CH 03</div>
{win("f1-win", 110, 600, 860, 740, "SYSTEM_ALERT.EXE",
 f'<div class="row"><svg width="150" height="150" viewBox="0 0 100 100"><path d="M50 8 L94 88 H6 Z" fill="{RED}" stroke="{NAVY}" stroke-width="6" stroke-linejoin="round"/><rect x="45" y="34" width="10" height="28" fill="{PAPER}"/><rect x="45" y="68" width="10" height="10" fill="{PAPER}"/></svg>'
 f'<div id="f1-title" class="display ghost" style="font-size:150px;color:{RED}">PERINGATAN:<br>SPOILER</div></div>'
 f'<p class="mono" style="font-size:36px;margin:22px 0 0">Video ini membuka twist dan akhir cerita film.</p>'
 f'<div class="btns"><span id="f1-btn" class="btn" style="background:{BLUE};color:{PAPER}">LANJUT</span><span class="btn">KELUAR</span></div>', bar=RED)}
{cur("f1-cursor", "left:280px;top:1020px")}
"""

# ================= F2 =================
f2 = f"""
<div class="abs" style="inset:0;background:radial-gradient(ellipse 70% 40% at 50% 28%,{PINK}55,transparent 70%)"></div>
<div id="f2-world" class="abs" style="inset:0">
 <div class="abs" style="left:40px;top:230px;width:1000px;height:700px;border:16px solid #2a3170;border-radius:70px;background:{PANEL}"></div>
 <img id="f2-eye" class="abs" src="assets/figures/eye-blue.png" style="left:70px;top:345px;width:940px;height:auto">
 <div id="f2-c1" class="abs mono chip" style="left:70px;top:150px">[ NAMA: ??? ]</div>
 <div id="f2-c2" class="abs mono chip" style="right:70px;top:150px;color:{PINK};border-color:{PINK}">[ PERAN: ??? ]</div>
 <div id="f2-c3" class="abs mono chip" style="left:110px;top:970px;color:{BLUE};background:{PAPER}">[ DIRI: ??? ]</div>
</div>
<div class="abs display center" style="top:1070px;font-size:200px"><div id="f2-h1">SIAPA</div><div id="f2-h2">DIRIMU</div><div id="f2-h3" style="color:{PINK}">SEBENARNYA?</div></div>
"""

# ================= F3 =================
segs = "".join(f'<i class="seg" style="background:{PINK}"></i>' for _ in range(15)) + "".join('<i class="seg" style="background:#c9c5ef"></i>' for _ in range(4))
f3 = f"""
<div class="grid"></div>
{icon("file", 70, 300, 0, 1.5).replace('class="abs icon"', 'id="f3-ic0" class="abs icon"')}{icon("folder", 880, 330, 0, 1.6).replace('class="abs icon"', 'id="f3-ic1" class="abs icon"')}{icon("disk", 840, 1180, 0, 1.5).replace('class="abs icon"', 'id="f3-ic2" class="abs icon"')}{icon("file", 120, 1230, 0, 1.4).replace('class="abs icon"', 'id="f3-ic3" class="abs icon"')}{icon("disk", 460, 250, 0, 1.2).replace('class="abs icon"', 'id="f3-ic4" class="abs icon"')}{icon("folder", 600, 1320, 0, 1.3).replace('class="abs icon"', 'id="f3-ic5" class="abs icon"')}
{win("f3-win", 90, 500, 900, 760, "perfect_blue.avi",
 f'<div class="display" style="font-size:210px;line-height:.9;color:{NAVY}"><div id="f3-t1">{tsp("PERFECT")}</div><div id="f3-t2" style="color:{BLUE}">{tsp("BLUE")}<span class="caret" id="f3-caret"></span></div></div>'
 f'<p class="mono" style="font-size:42px;margin:12px 0 18px;font-weight:700"><span id="f3-yr">{tsp("1997")}</span><span id="f3-dir"> {tsp("· SATOSHI KON")}</span></p>'
 f'<div class="load"><div class="segs">{segs}</div></div><p id="f3-pct" class="mono" style="font-size:30px;margin:10px 0 0">MEMUAT… 0%</p>')}
{cur("f3-cursor", "left:760px;top:1040px")}
"""

# ================= F4 =================
beams = ""
for i, ax in enumerate([170, 400, 620, 810]):
    beams += f'<polygon points="{ax},0 {ax-110 + i*18},700 {ax+110 + i*18},700" fill="url(#beam)"/>'
crowd = ""
for i in range(16):
    x = 30 + i * 62 + R.randint(-10, 10); y = 612 + R.randint(-14, 14)
    crowd += f'<circle cx="{x}" cy="{y+26}" r="26" fill="{NAVY}"/><rect x="{x-8}" y="{y-120}" width="14" height="110" rx="7" fill="{[PINK,BLUE,PAPER][i%3]}" transform="rotate({R.randint(-18,18)} {x} {y})"/>'
stage = f"""<svg id="f4-stage" class="abs" style="left:40px;top:500px" width="1000" height="720" viewBox="0 0 1000 700">
 <defs><linearGradient id="bg4" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a0f4a"/><stop offset="1" stop-color="{PINK}"/></linearGradient>
 <linearGradient id="beam" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".55"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>
 <rect width="1000" height="700" rx="26" fill="url(#bg4)" stroke="{PAPER}" stroke-width="8"/>
 <g id="f4-beams">{beams}</g>
 <ellipse cx="500" cy="520" rx="470" ry="74" fill="{NAVY}" opacity=".55"/>
 <image id="f4-idolL" href="assets/figures/idol-long.png" x="40" y="130" width="{int(560*484/1416)}" height="560" opacity=".62"/>
 <image id="f4-idolR" href="assets/figures/idol-twin.png" x="700" y="150" width="{int(540*444/1356)}" height="540" opacity=".62"/>
 <image id="f4-mima" href="assets/figures/mima-mic.png" x="300" y="30" width="400" height="600"/>
 <g id="f4-crowd">{crowd}</g>
 <path id="f4-curL" d="M0 0 H90 Q60 300 70 700 H0 Z" fill="{RED}" opacity=".9"/>
 <path id="f4-curR" d="M1000 0 H910 Q940 300 930 700 H1000 Z" fill="{RED}" opacity=".9"/>
</svg>"""
f4 = f"""
<div class="abs" style="inset:0;background:radial-gradient(ellipse 80% 30% at 50% 30%,{PINK}44,transparent 70%)"></div>
<div id="f4-title" class="abs display center" style="top:110px;font-size:260px;color:{PINK};text-shadow:8px 0 {BLUE}">MIMA</div>
<div id="f4-sub" class="abs mono center" style="top:372px;font-size:40px;font-weight:700">IDOLA POP → AKTRIS</div>
{stage}<div id="f4-s0">{star(150,560,120)}</div><div id="f4-s1">{star(840,700,90,.8)}</div><div id="f4-s2">{star(560,600,70,.7)}</div>
<div id="f4-dot" class="abs" style="left:584px;top:560px;width:60px;height:60px"><div class="ring" id="f4-ring"></div><div class="dotc"></div></div>
{win("f4-win", 150, 1250, 780, 380, "CHAM!.exe",
 f'<div class="display" style="font-size:96px;line-height:1">Keluar dari grup?</div><div class="btns"><span id="f4-ya" class="btn" style="background:{PINK};color:{NAVY}">YA</span><span class="btn">TIDAK</span></div>')}
{cur("f4-cursor", "left:410px;top:1500px")}
"""

# ================= F5 =================
entries = [("12 MEI", "Hari ini aku pulang larut. Lampu kota terasa dingin."),
           ("14 MEI", "Mereka bilang aku berubah. Aku tidak merasa begitu."),
           ("17 MEI", "Seseorang tahu semua yang kulakukan.")]
ent = "".join(f'<div class="entry" id="f5-e{i}"><b style="color:{BLUE}">{tsp(d)}</b><p>{tsp(t)}</p></div>' for i, (d, t) in enumerate(entries))
cmts = "".join(f'<div class="cmt" id="f5-c{i}"><i style="background:{c}"></i><span>{t}</span></div>' for i, (c, t) in enumerate([(PINK, "Aku selalu melihatmu."), (BLUE, "Mima, ini kau yang asli?")]))
f5 = f"""
<div class="grid"></div>
{win("f5-win", 50, 220, 980, 1220, "mima_room.htm — Mima's Room",
 f'<div class="addr mono">http://mima-room.jp/diary</div>'
 f'<div class="head display" style="background:{PINK};color:{NAVY}">MIMA\'S ROOM</div>'
 f'<div class="counter mono"><span>PENGUNJUNG</span>{"".join(f"<i id=f5-d{k}>0</i>" for k in range(5))}</div>{ent}<div class="cmts">{cmts}</div>')}
<div id="f5-t1" class="toast" style="top:520px;right:20px;background:{RED}"><span class="mono">⚠ ADA YANG MENGAWASI</span></div>
<div id="f5-t2" class="toast" style="top:640px;right:20px;background:{NAVY};border:5px solid {RED}"><span class="mono" style="color:{RED}">● 1 ORANG TEWAS</span></div>
<img id="f5-eye" class="abs" src="assets/figures/eye-red.png" style="left:770px;top:1190px;width:240px;height:auto">
<div id="f5-bar1" class="abs" style="left:50px;top:760px;width:980px;height:22px;background:{PINK};mix-blend-mode:screen;opacity:0"></div>
<div id="f5-bar2" class="abs" style="left:50px;top:1010px;width:980px;height:16px;background:{BLUE};mix-blend-mode:screen;opacity:0"></div>
<div id="f5-red" class="abs" style="inset:0;background:{RED};mix-blend-mode:multiply;opacity:0"></div>
"""

# ================= F6 =================
frames = ""
sizes = [(960, 1280), (780, 1040), (620, 830), (470, 630), (340, 450)]
for i, (w, h) in enumerate(sizes):
    col = [BLUE, PINK][i % 2]
    frames += f'<div id="f6-n{i}" class="abs nest" style="left:{540-w//2}px;top:{860-h//2}px;width:{w}px;height:{h}px;border:10px solid {col};background:{[PANEL,NAVY][i%2]}"></div>'
fig = f"""<img id="f6-blue" class="abs" src="assets/figures/mima-side-blue.png" style="left:380px;top:420px;height:900px;width:auto;opacity:0">
<img id="f6-pink" class="abs" src="assets/figures/mima-stand-pink.png" style="left:250px;top:400px;height:920px;width:auto;opacity:0">"""
lines = ""
for k in range(9):
    a_ = k * 40 + R.randint(-14, 14); pts = [(700, 460)]
    for j in range(1, 5):
        pts.append((pts[-1][0] + math.cos(math.radians(a_ + R.randint(-18, 18))) * (90 + j * 28), pts[-1][1] + math.sin(math.radians(a_ + R.randint(-18, 18))) * (90 + j * 28)))
    lines += '<polyline class="crk" points="' + " ".join(f"{x:.0f},{y:.0f}" for x, y in pts) + f'" fill="none" stroke="{PAPER}" stroke-width="{R.choice([3,4,5])}" stroke-linecap="round"/>'
shards = "".join(f'<polygon class="shard" points="{x},{y} {x+70},{y+30} {x+20},{y+90}" fill="{PAPER}" fill-opacity=".14" stroke="{PAPER}" stroke-width="3"/>' for x, y in [(790, 330), (880, 520), (610, 340), (820, 700), (150, 1180), (260, 1340)])
f6 = f"""
<div class="grid"></div>
<div id="f6-world" class="abs" style="inset:0">{frames}{fig}</div>
<div id="f6-tag1" class="abs tag" style="left:70px;top:210px;background:{PINK};color:{NAVY}">PERAN</div>
<div id="f6-tag2" class="abs tag" style="right:70px;top:1370px;background:{BLUE};color:{PAPER}">DIRI</div>
<svg class="abs" style="left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920"><g id="f6-cracks">{lines}</g><g id="f6-shards">{shards}</g></svg>
<div id="f6-msg" class="abs mono center" style="top:1500px;font-size:36px;color:{PINK}">{tsp("[ realitas.exe berhenti merespons ]")}</div>
"""

# ================= F7 =================
mirror = f"""<svg id="f7-mirror" class="abs" style="left:190px;top:260px" width="700" height="980" viewBox="0 0 700 980">
 <path d="M30 960 V330 C30 130 160 30 350 30 C540 30 670 130 670 330 V960 Z" fill="{PINK}" stroke="{PAPER}" stroke-width="16"/>
 <path d="M70 940 V334 C70 160 180 72 350 72 C520 72 630 160 630 334 V940 Z" fill="{BLUE}" opacity=".85"/>
 <image id="f7-idol" href="assets/figures/rumi-idol-pink.png" x="56" y="110" width="640" height="850" opacity="0" preserveAspectRatio="xMidYMax meet"/>
 <image id="f7-mgr" href="assets/figures/rumi-mgr-paper.png" x="40" y="96" width="620" height="864" opacity="0" preserveAspectRatio="xMidYMax meet"/>
 <path d="M520 120 L610 60 L580 200Z" fill="{PAPER}" fill-opacity=".22"/>
</svg>"""
f7 = f"""
<div class="abs" style="inset:0;background:radial-gradient(ellipse 80% 40% at 50% 35%,{PINK}55,transparent 70%)"></div>
<div id="f7-p1" class="abs" style="left:-80px;top:-60px;width:360px;height:360px;background:{PAPER};opacity:.12;transform:rotate(18deg)"></div>
<div id="f7-p2" class="abs" style="right:-100px;top:-50px;width:380px;height:300px;background:{BLUE};opacity:.35;transform:rotate(-22deg)"></div>
<div id="f7-p3" class="abs" style="left:-90px;bottom:-60px;width:340px;height:300px;background:{PINK};opacity:.3;transform:rotate(-16deg)"></div>
{mirror}
<div id="f7-tag" class="abs tag" style="left:190px;top:1180px;background:{PAPER};color:{NAVY};font-size:38px">RUMI — MANAJER</div>
<div id="f7-q" class="abs display center" style="top:1290px;font-size:150px">{tsp("MIMA YANG ASLI?")}</div>
<div id="f7-strike" class="abs" style="left:170px;top:1378px;width:740px;height:14px;background:{RED};transform:rotate(-3deg);transform-origin:left center"></div>
"""

# ================= F8 =================
f8 = f"""
<div class="grid" style="opacity:.5"></div>
<img id="f8-gh1" class="abs" src="assets/figures/mima-stand-pink.png" style="left:150px;top:880px;height:900px;width:auto;opacity:0">
<img id="f8-gh2" class="abs" src="assets/figures/rumi-mgr-paper.png" style="left:470px;top:900px;height:880px;width:auto;opacity:0">
{win("f8-win", 90, 440, 900, 460, "identitas.txt",
 f'<div class="mono" style="font-size:44px;color:#59608f;height:60px;margin-bottom:10px">{tsp("identitas di era layar")}</div>'
 f'<div class="mono" style="font-size:88px;font-weight:700;line-height:1.1;color:{NAVY}">{tsp("aku yang asli.")}<span class="caret" id="f8-caret" style="height:80px;width:46px"></span></div>')}
<div id="f8-line" class="abs" style="left:150px;top:1010px;width:780px;height:5px;background:{PINK};transform-origin:left center"></div>
<div id="f8-title" class="abs display center" style="top:1040px;font-size:230px">PERFECT BLUE</div>
<div id="f8-year" class="abs display center" style="top:1280px;font-size:140px;color:{BLUE}">(1997)</div>
"""

CSS = f'''
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{margin:0;background:{NAVY}}}
#root{{position:relative;width:100%;height:100%;overflow:hidden;background:{NAVY};color:{PAPER};font-family:Inter,sans-serif}}
.scene{{position:absolute;inset:0;overflow:hidden;background:{NAVY}}}
.abs{{position:absolute}} .center{{left:0;right:0;text-align:center}}
.display{{font-family:"League Gothic",sans-serif;text-transform:uppercase;line-height:.92;letter-spacing:.01em}}
.mono{{font-family:"Space Mono",monospace}}
.grid{{position:absolute;inset:0;background-image:linear-gradient({BLUE}22 2px,transparent 2px),linear-gradient(90deg,{BLUE}22 2px,transparent 2px);background-size:90px 90px}}
.scan{{position:absolute;inset:0;pointer-events:none;background:repeating-linear-gradient(0deg,rgba(0,0,0,.2) 0 2px,transparent 2px 5px)}}
.vig{{position:absolute;inset:0;pointer-events:none;background:radial-gradient(ellipse at center,transparent 55%,rgba(0,0,0,.6))}}
.win{{position:absolute;background:{PAPER};border:6px solid {PAPER};color:{NAVY};box-shadow:14px 14px 0 {BLUE}88;font-family:"Space Mono",monospace;overflow:hidden}}
.win .bar{{height:74px;display:flex;align-items:center;justify-content:space-between;padding:0 24px;color:{PAPER};font-weight:700;font-size:30px}}
.win .ctl i{{display:inline-block;width:26px;height:26px;margin-left:10px;background:{PAPER};border:3px solid {NAVY}}}
.win .body{{padding:34px 40px}}
.row{{display:flex;align-items:center;gap:26px}}
.ghost{{text-shadow:7px 0 {PINK},-7px 0 {BLUE}}}
.btns{{display:flex;gap:26px;margin-top:34px}}
.btn{{display:inline-block;padding:16px 38px;border:5px solid {NAVY};font-weight:700;font-size:38px;background:{PAPER}}}
.chip{{padding:10px 22px;border:4px solid {PAPER};font-size:32px;font-weight:700;background:{NAVY}}}
.tag{{padding:8px 26px;font-family:"Space Mono",monospace;font-weight:700;font-size:44px;letter-spacing:.1em}}
.load{{border:5px solid {NAVY};padding:8px;background:#fff}} .segs{{display:flex;gap:8px}} .segs i{{display:block;flex:1;height:44px}}
.caret{{display:inline-block;width:40px;height:150px;background:{PINK};margin-left:10px;vertical-align:-10px}}
.addr{{border:4px solid {NAVY};padding:10px 18px;font-size:30px;margin-bottom:18px}}
.head{{font-size:130px;padding:6px 26px;line-height:1.0;margin-bottom:18px}}
.counter{{display:flex;align-items:center;gap:8px;font-size:30px;font-weight:700;margin-bottom:22px}} .counter span{{margin-right:14px}}
.counter i{{font-style:normal;background:{NAVY};color:{PINK};padding:6px 14px;font-size:42px}}
.entry{{margin-bottom:20px;font-size:34px}} .entry p{{margin-top:4px;line-height:1.25}}
.cmts{{margin-top:22px;border-top:4px solid {NAVY};padding-top:16px}} .cmt{{display:flex;align-items:center;gap:16px;margin:10px 0;font-size:32px}} .cmt i{{display:block;width:44px;height:44px;border:3px solid {NAVY}}}
.ch{{opacity:0}}
.nest{{}}
.dotc{{position:absolute;inset:8px;border-radius:50%;background:{RED};border:4px solid {PAPER};box-shadow:0 0 30px {RED}}}
.ring{{position:absolute;inset:0;border-radius:50%;border:5px solid {PAPER};opacity:0}}
.toast{{position:absolute;padding:20px 28px;font-size:34px;font-weight:700;color:{PAPER};box-shadow:10px 10px 0 #0006}}
'''

def scene(id_, start, dur, inner):
    return (f'<section id="{id_}" class="scene clip" data-start="{start}" data-duration="{dur}" data-track-index="1">'
            f'{inner}<div class="scan"></div><div class="vig"></div></section>')

body = "\n      ".join(scene(i, st, d, h) for (i, st, d), h in zip(SCENES, [f1, f2, f3, f4, f5, f6, f7, f8]))
audio = "\n      ".join(f'<audio id="vo{n:02d}" src="assets/vo/{n:02d}.wav" data-start="{LS[n]}" data-track-index="7" data-volume="1"></audio>' for n in range(1, 8))
if os.path.exists("assets/bgm.wav"):
    audio += f'\n      <audio id="bgm" src="assets/bgm.wav" data-start="0" data-duration="{TOTAL}" data-track-index="8" data-volume="0.5"></audio>'
sfx = json.load(open("assets/sfx/sfx.json")) if os.path.exists("assets/sfx/sfx.json") else []
for i, (name, t_) in enumerate(sfx):
    audio += f'\n      <audio id="sfx{i:02d}" src="assets/sfx/{name}.wav" data-start="{t_}" data-track-index="9" data-volume="0.8"></audio>'

JS = open("scripts/timeline.js").read().replace("__ST__", json.dumps(ST)).replace("__LS__", json.dumps(LS)).replace("__TOTAL__", str(TOTAL)).replace("__LEND__", str(LEND))
html = f"""<!doctype html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>Perfect Blue — Lapisan Realitas</title>
    <script src="assets/gsap.min.js"></script>
    <style>{CSS}</style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1080" data-height="1920">
      {body}
      <div id="flash" class="abs" style="inset:0;background:#fff;opacity:0;mix-blend-mode:screen;pointer-events:none"></div>
      {audio}
    </div>
    <script>
{JS}
    </script>
  </body>
</html>
"""
open("index.html", "w").write(html)
print("ok", len(html) // 1024, "KB · total", TOTAL, "s · LS", LS)
