"""Gambar karakter statis gaya tinta (tahap 1, revisi 2). Deterministik (seed tetap).
Menulis index.html berisi satu ilustrasi (bukan rig/SVG modular)."""
import math, random

R = random.Random(11)
INK, PAPER, WHITE = "#161513", "#f4eee2", "#fbf7ee"

def cr(pts, closed=False, n=14):
    P = list(pts)
    if closed: P = [P[-1]] + P + [P[0], P[1]]
    else: P = [P[0]] + P + [P[-1]]
    out = []
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        for k in range(n):
            t = k / n; t2, t3 = t * t, t * t * t
            out.append(tuple(0.5 * ((2 * p1[j]) + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t2 + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t3) for j in (0, 1)))
    if not closed: out.append(P[-2])
    return out

def wob(pts, amp):
    return [(x + R.uniform(-amp, amp), y + R.uniform(-amp, amp)) for x, y in pts]

def noise(ph):
    a, b, c = R.uniform(2, 4), R.uniform(5, 9), R.uniform(0, 6.28)
    return lambda s: 0.5 * math.sin(a * s * 6.28 + ph) + 0.3 * math.sin(b * s * 6.28 + c)

def d(poly):
    return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in poly) + " Z"

def stroke(pts, w, t0=0.25, t1=0.25, amp=1.2, var=0.28, tip=0.12):
    """garis tinta bervariasi ketebalannya, mengecil di ujung."""
    c = cr(wob(pts, amp)); n = len(c); nz = noise(R.uniform(0, 6.28))
    L, R_ = [], []
    for i, (x, y) in enumerate(c):
        a = c[max(i - 1, 0)]; b = c[min(i + 1, n - 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]; ln = math.hypot(dx, dy) or 1
        nx, ny = -dy / ln, dx / ln; s = i / (n - 1)
        prof = min(1, s / t0 if t0 else 1) * min(1, (1 - s) / t1 if t1 else 1)
        prof = math.sin(prof * math.pi / 2)
        ww = max(w * (tip + (1 - tip) * prof) * (1 + var * nz(s)), 0.6) / 2
        L.append((x + nx * ww + R.uniform(-.5, .5), y + ny * ww + R.uniform(-.5, .5)))
        R_.append((x - nx * ww + R.uniform(-.5, .5), y - ny * ww + R.uniform(-.5, .5)))
    return d(L + R_[::-1])

def blob(pts, amp=1.5, n=12):
    return d(cr(wob(pts, amp), closed=True, n=n))

def lock(pts, w, **k):
    return stroke(pts, w, t0=0.18, t1=0.9, var=0.12, tip=0.02, **k)

parts = []
def add(p, fill=INK): parts.append(f'<path d="{p}" fill="{fill}"/>')

# ================= BADAN =================
parts.append('<g transform="translate(0 -46)">')
hoodL = [(454,1030),(420,1050),(408,1088),(428,1128)]
hoodR = [(682,1030),(716,1048),(728,1086),(706,1124)]
parts.append(f'<path d="{d(cr(hoodL+[(476,1100),(470,1058)],closed=True,n=8))}" fill="{WHITE}"/>')
parts.append(f'<path d="{d(cr(hoodR+[(664,1096),(668,1056)],closed=True,n=8))}" fill="{WHITE}"/>')
add(stroke(hoodL, 9, t0=.1, t1=.25, amp=0.6))
add(stroke(hoodR, 9, t0=.1, t1=.25, amp=0.6))
add(stroke([(436,1062),(424,1090)], 3.4, amp=.5)); add(stroke([(700,1060),(712,1088)], 3.4, amp=.5))

# leher (di bawah rahang, agak pendek dan tebal; kiri-kanan tidak identik)
neck = [(466,956),(460,1040),(446,1092),(424,1140),(560,1156),(700,1132),(676,1086),(660,1030),(654,956)]
parts.append(f'<path d="{blob(neck,1.2)}" fill="{WHITE}"/>')
add(stroke([(466,985),(461,1040),(448,1092),(426,1138)], 7, t0=.1, amp=1.2))
add(stroke([(655,982),(660,1034),(676,1086),(700,1130)], 8, t0=.1, amp=1.2))
# arsir bayangan di bawah dagu
add(stroke([(486,1030),(520,1046),(560,1050)], 3.2, amp=.8))
add(stroke([(480,1052),(520,1070),(570,1074)], 3, amp=.8))
add(stroke([(476,1076),(520,1092),(580,1094)], 2.6, amp=.8))

# badan hoodie (isian krem dari garis luar yang sama, tanpa garis bawah)
outL = [(426,1138),(350,1152),(266,1192),(190,1252),(142,1340),(122,1450),(116,1566)]
outR = [(702,1134),(776,1152),(862,1192),(940,1252),(990,1340),(1010,1450),(1014,1572)]
fillpoly = cr(outL, n=10) + cr(outR, n=10)[::-1]
parts.append(f'<path d="{d(fillpoly)}" fill="{WHITE}"/>')
# kaos hitam di dalam kerah
tee = [(452,1134),(560,1154),(672,1128),(692,1152),(632,1198),(562,1210),(498,1194),(440,1152)]
add(blob(tee, 1.0, 10))
# garis luar badan kiri-kanan
add(stroke([(426,1138),(350,1152),(266,1192),(190,1252),(142,1340),(122,1450),(116,1566)], 9, t0=.04, t1=.3, amp=1.6))
add(stroke([(702,1134),(776,1152),(862,1192),(940,1252),(990,1340),(1010,1450),(1014,1572)], 9, t0=.04, t1=.3, amp=1.6))
# bibir kerah (rim tudung) — tebal-tipis
add(stroke([(428,1122),(446,1172),(500,1208),(566,1220),(638,1202),(690,1158),(706,1118)], 13, t0=.15, t1=.15, amp=1.4, var=.35))
# tali hoodie + ujung tali
add(stroke([(502,1214),(494,1300),(500,1360),(492,1420)], 7, t0=.08, t1=.1, amp=1.5))
add(stroke([(640,1204),(650,1296),(642,1356),(650,1412)], 7, t0=.08, t1=.1, amp=1.5))
add(blob([(486,1418),(498,1414),(502,1440),(490,1446)], .8, 6)); add(blob([(644,1410),(656,1408),(660,1434),(648,1438)], .8, 6))
# jahitan bahu & lipatan kain
add(stroke([(360,1176),(304,1262),(272,1362),(266,1458)], 6, t0=.08, t1=.25, amp=1.8))
add(stroke([(774,1172),(830,1262),(862,1362),(870,1456)], 6, t0=.08, t1=.25, amp=1.8))
add(stroke([(176,1332),(214,1352),(246,1404)], 4, amp=1.2)); add(stroke([(954,1330),(914,1352),(884,1406)], 4, amp=1.2))
add(stroke([(452,1292),(436,1340)], 4, amp=1)); add(stroke([(706,1286),(724,1330)], 4, amp=1))
add(stroke([(330,1230),(318,1262)], 3, amp=.8)); add(stroke([(812,1228),(826,1258)], 3, amp=.8))
# garis potong gambar di bawah (goresan longgar, putus-putus)
add(stroke([(122,1566),(300,1574),(470,1562)], 5, t0=.2, t1=.3, amp=2))
add(stroke([(520,1564),(700,1572),(880,1562),(1010,1570)], 5, t0=.2, t1=.3, amp=2))

parts.append('</g>')
# ================= TELINGA =================
earL = [(332,694),(300,688),(278,722),(284,768),(310,792),(340,782)]
earR = [(784,702),(816,696),(836,732),(828,776),(802,796),(778,782)]
parts.append(f'<path d="{blob(earL,1.2)}" fill="{WHITE}"/>'); parts.append(f'<path d="{blob(earR,1.2)}" fill="{WHITE}"/>')
add(stroke([(334,694),(302,688),(279,722),(285,768),(311,792),(342,782)], 6.5, t0=.1, t1=.12, amp=1.2))
add(stroke([(782,702),(816,696),(838,732),(829,778),(803,797),(776,783)], 6.5, t0=.1, t1=.12, amp=1.2))
add(stroke([(308,716),(298,740),(306,764),(322,772)], 3.6, amp=.8)); add(stroke([(806,724),(816,746),(808,768),(794,774)], 3.6, amp=.8))

# ================= WAJAH =================
face = [(330,560),(318,650),(326,760),(366,872),(432,948),(512,994),(570,1006),(632,994),(706,942),(762,852),(790,742),(788,640),(748,560),(662,502),(530,484),(410,502),(330,560)]
parts.append(f'<path d="{blob(face[:-1],1.4)}" fill="{WHITE}"/>')
# garis wajah: tebal di rahang/dagu (sisi bayangan), tipis di dahi
add(stroke([(322,640),(326,760),(366,872),(432,948),(512,994),(570,1006)], 9, t0=.1, t1=.1, amp=1.5, var=.3))
add(stroke([(566,1006),(632,994),(706,942),(762,852),(790,742),(788,650)], 11, t0=.1, t1=.15, amp=1.5, var=.3))
# bercak pipi
add(stroke([(386,790),(394,806)], 4, amp=.5)); add(stroke([(402,804),(409,820)], 3.5, amp=.5)); add(stroke([(722,796),(728,812)], 3.8, amp=.5))
# hidung
add(stroke([(560,732),(570,772),(556,798),(538,808),(552,816),(578,808)], 6.5, t0=.12, t1=.2, amp=1.2, var=.3))
# mulut sederhana (netral, tersenyum tipis) — mudah diganti variasi nanti
add(stroke([(486,884),(530,902),(586,900),(632,874)], 8, t0=.2, t1=.25, amp=1.2))
add(stroke([(632,874),(642,866)], 4, t0=.1, t1=.4, amp=.5))

# ================= MATA & ALIS =================
def eye(cx, cy, rx, ry, rot):
    pts = []
    for k in range(10):
        a = k / 10 * 6.283; r = 1 + R.uniform(-.06, .06)
        x, y = rx * r * math.cos(a), ry * r * math.sin(a)
        pts.append((cx + x * math.cos(rot) - y * math.sin(rot), cy + x * math.sin(rot) + y * math.cos(rot)))
    return blob(pts, .6, 8)
add(eye(452, 704, 20, 29, -.07)); add(eye(648, 694, 21, 30, .05))
parts.append('<circle cx="460" cy="692" r="6" fill="#fbf7ee"/><circle cx="657" cy="682" r="6.5" fill="#fbf7ee"/>')
# kelopak atas (ada tarikan ke luar), kelopak bawah tipis
add(stroke([(414,682),(436,660),(470,656),(498,676)], 9, t0=.25, t1=.35, amp=1.2, var=.35))
add(stroke([(604,672),(630,650),(668,648),(694,666)], 9.5, t0=.25, t1=.35, amp=1.2, var=.35))
add(stroke([(430,742),(452,750),(476,744)], 3, t0=.4, t1=.4, amp=.8)); add(stroke([(626,732),(650,740),(674,734)], 3, t0=.4, t1=.4, amp=.8))
# alis: kanan sedikit lebih naik -> ekspresi tertarik
add(stroke([(402,650),(436,624),(484,618),(518,636)], 15, t0=.3, t1=.35, amp=1.5, var=.4))
add(stroke([(598,628),(638,598),(688,596),(722,618)], 16, t0=.3, t1=.35, amp=1.5, var=.4))

# ================= RAMBUT =================
cap = [(300,704),(288,600),(312,502),(372,424),(452,386),(480,366),(570,356),(646,372),(684,388),(756,440),(806,534),(816,644),(804,722),(784,734),(770,650),(732,574),(662,524),(560,502),(452,508),(372,544),(336,614),(326,704)]
add(blob(cap, 2.6, 10))
locks = [
 ([(346,478),(344,540),(358,590),(376,622)], 58), ([(414,466),(428,540),(462,598),(506,632)], 74),
 ([(500,456),(500,512),(514,548),(536,566)], 56), ([(580,452),(598,528),(636,574),(690,596)], 82),
 ([(690,474),(706,520),(728,540),(748,544)], 50), ([(318,560),(312,640),(320,722),(336,770)], 52),
 ([(790,540),(800,606),(796,664),(780,706)], 46), ([(462,430),(470,470),(458,500)], 34), ([(546,484),(550,528),(568,552)], 36),
]
for pts, w in locks: add(lock(pts, w, amp=3))
add(lock([(444,402),(430,376),(410,356),(396,352)], 34, amp=1.5)); add(lock([(656,394),(676,372),(700,362),(716,362)], 30, amp=1.5))
# jambul + helai terbang
add(lock([(560,380),(568,344),(598,322),(632,318)], 30, amp=1.5))
for pts, w in [([(498,390),(486,356),(460,334),(436,330)], 7), ([(626,384),(644,352),(672,336)], 6), ([(380,440),(354,420),(336,394)], 6), ([(742,452),(768,436),(782,412)], 5.5)]:
    add(stroke(pts, w, t0=.1, t1=.6, amp=1.5, tip=.05))
# sorot pada rambut (goresan krem tipis, tidak sejajar)
for pts, w in [([(420,436),(486,404),(566,398)], 6), ([(604,412),(662,420),(704,452)], 5), ([(352,520),(344,566)], 4), ([(470,480),(488,520)], 3.5)]:
    parts.append(f'<path d="{stroke(pts, w, t0=.2, t1=.5, amp=1.2, tip=.05)}" fill="{WHITE}" opacity=".85"/>')

svg = "\n          ".join(parts)
html = f'''<!doctype html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>Prototype Karakter 2D</title>
    <script src="assets/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; background: {PAPER}; }}
      #root {{ position: relative; width: 100%; height: 100%; overflow: hidden; background: {PAPER}; }}
      #stage {{ position: absolute; inset: 0; width: 100%; height: 100%; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="8" data-width="1080" data-height="1920">
      <svg id="stage" class="clip" data-start="0" data-duration="8" data-track-index="1" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <filter id="grain" x="0" y="0" width="100%" height="100%">
            <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="3"/>
            <feColorMatrix type="matrix" values="0 0 0 0 0.25  0 0 0 0 0.2  0 0 0 0 0.1  0 0 0 0.08 0"/>
          </filter>
        </defs>
        <rect width="1080" height="1920" fill="{PAPER}"/>
        <rect width="1080" height="1920" filter="url(#grain)"/>
        <g id="drawing">
          {svg}
        </g>
      </svg>
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
'''
open("index.html", "w").write(html)
print("ok", len(parts), "bentuk")
