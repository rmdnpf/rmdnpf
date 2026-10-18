"""Hitung jadwal dari durasi VO (assets/vo/NN.wav): awal tiap baris, awal tiap scene, dan potongan ucapan (dibelah di jeda >0.30 dtk).
Menulis scripts/timing.json dan menyegarkan blok TIMING di index.html (konstanta JS + data-start/data-duration tiap scene).
Pakai: python3 scripts/make_timing.py"""
import json, re, wave
import numpy as np

TOTAL = 60.0
LEAD = 0.4     # VO 1 mulai
GAP = 0.2      # jeda antar file VO
PAUSE = 0.30   # jeda minimum yang membelah potongan ucapan
THR = 10 ** (-42 / 20)


def analyse(path):
    w = wave.open(path); sr = w.getframerate()
    x = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2").astype(np.float32) / 32768
    a = np.abs(x); idx = np.where(a > THR)[0]
    lead, last = idx[0] / sr, idx[-1] / sr
    win = int(sr * 0.05)
    quiet = np.convolve(a, np.ones(win) / win, "same") < THR
    runs, s = [], None
    for i, v in enumerate(quiet):
        if v and s is None: s = i
        if not v and s is not None: runs.append((s / sr, i / sr)); s = None
    cuts = [(t0, t1) for t0, t1 in runs if t1 - t0 > PAUSE and t0 > lead + 0.1 and t1 < last - 0.05]
    bounds, st = [], lead
    for t0, t1 in cuts:
        bounds.append((round(st, 2), round(t0, 2))); st = t1
    bounds.append((round(st, 2), round(last, 2)))
    return len(x) / sr, bounds


L, S, D, P = {}, {}, {}, {}
t = LEAD
for n in range(1, 9):
    d, ch = analyse(f"assets/vo/{n:02d}.wav")
    L[n], D[n], P[n] = round(t, 2), round(d, 2), ch
    t += d + GAP
for n in range(1, 9):
    S[n] = 0.0 if n == 1 else round(L[n] - 0.05, 2)
dur = {n: round((S[n + 1] if n < 8 else TOTAL) - S[n], 2) for n in range(1, 9)}
end_vo = L[8] + D[8]
json.dump({"L": L, "S": S, "D": D, "dur": dur, "chunks": P, "total": TOTAL, "vo_end": round(end_vo, 2)}, open("scripts/timing.json", "w"), indent=1)

block = ("      // TIMING:START (dibuat oleh scripts/make_timing.py)\n"
         f"      const L = {json.dumps({str(k): v for k, v in L.items()})};\n"
         f"      const S = {{ {', '.join(f'f{k}: {v}' for k, v in S.items())} }};\n"
         f"      const P = {json.dumps({str(k): v for k, v in P.items()})};\n"
         "      // TIMING:END")
try:
    s = open("index.html").read()
    s = re.sub(r"      // TIMING:START.*?// TIMING:END", lambda m: block, s, flags=re.S)
    for n in range(1, 9):
        s = re.sub(r'(<section id="f%d" class="scene clip" data-start=")[^"]*(" data-duration=")[^"]*(")' % n,
                   lambda m: f'{m.group(1)}{S[n]}{m.group(2)}{dur[n]}{m.group(3)}', s)
    open("index.html", "w").write(s)
except FileNotFoundError:
    pass
print("L", L); print("S", S); print("dur", dur); print("vo_end", round(end_vo, 2), "sisa", round(TOTAL - end_vo, 2))
for n in range(1, 9): print(n, len(P[n]), P[n])
