"""Musik dark fantasy orchestral ambient + SFX orisinal (sintesis, seed tetap). Bukan tiruan soundtrack Elden Ring."""
import json, wave
import numpy as np
SR = 44100
rng = np.random.default_rng(33)
TM = json.load(open("scripts/timing.json")); LS = {int(k): v for k, v in TM["LS"].items()}; ST = {int(k): v for k, v in TM["ST"].items()}
TOTAL = TM["TOTAL"]
hit5 = LS[5] + 4.4; snap9 = LS[9] + 6.3

def save(path, x, gain=0.9):
    x = x / (np.max(np.abs(x)) + 1e-9) * gain
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((x * 32767).astype("<i2").tobytes())
def env(n, a, d): x = np.arange(n) / SR; return np.minimum(1, x / max(a, 1e-4)) * np.exp(-x * d)
def bnoise(sec, f0, f1):
    n = int(SR * sec); X = np.fft.rfft(rng.standard_normal(n)); f = np.fft.rfftfreq(n, 1 / SR); X[(f < f0) | (f > f1)] = 0; return np.fft.irfft(X, n)
def lp(x, fc):
    a = np.exp(-2 * np.pi * fc / SR); y = np.zeros_like(x); s = 0.0
    for i in range(len(x)): s = a * s + (1 - a) * x[i]; y[i] = s
    return y
def lpf_fft(x, fc):
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1 / SR); X *= 1 / (1 + (f / fc) ** 4); return np.fft.irfft(X, len(x))

# ---------- SFX ----------
def boom(sec=3.2): n = int(SR * sec); x = np.arange(n) / SR; return np.sin(2 * np.pi * np.cumsum(62 * np.exp(-x * 1.6) + 28) / SR) * env(n, .004, 1.1) + lpf_fft(bnoise(sec, 20, 700), 400) * env(n, .003, 2.4) * .6
def shatter(sec=2.4):
    n = int(SR * sec); out = bnoise(sec, 2500, 14000) * env(n, .001, 3.5)
    for k in range(34):
        s = int(SR * rng.uniform(.04, 1.6)); ln = int(SR * .12); x = np.arange(ln) / SR
        out[s:s + ln] += (np.sin(2 * np.pi * rng.uniform(2500, 8000) * x) * np.exp(-x * 35))[: n - s] * .35
    return out
def riser(sec=1.8): n = int(SR * sec); return bnoise(sec, 400, 9000) * (np.linspace(0, 1, n) ** 2.2) + np.sin(2 * np.pi * np.cumsum(np.linspace(90, 700, n)) / SR) * np.linspace(0, 1, n) ** 2 * .3
def whoosh(sec=.9): n = int(SR * sec); return bnoise(sec, 300, 5000) * np.sin(np.linspace(0, np.pi, n)) ** 2
def clink(): n = int(SR * .6); x = np.arange(n) / SR; return sum(np.sin(2 * np.pi * f * x) * a for f, a in ((1800, 1), (2700, .6), (4100, .4))) * env(n, .001, 9) * .6
def snap(): n = int(SR * 1.0); x = np.arange(n) / SR; return (bnoise(1.0, 1500, 12000) * env(n, .001, 10) + np.sin(2 * np.pi * 220 * x) * env(n, .001, 16) * .5) * 1.0
def bell(sec=3.5): n = int(SR * sec); x = np.arange(n) / SR; return sum(np.sin(2 * np.pi * f * x) * a for f, a in ((440, 1), (880, .7), (1320, .5), (1760, .3), (2217, .2))) * env(n, .004, 1.2)
def shimmer(sec=2.6): n = int(SR * sec); x = np.arange(n) / SR; return sum(np.sin(2 * np.pi * f * x + rng.uniform(0, 6.3)) * a for f, a in ((880, 1), (1320, .8), (1760, .6), (2640, .4))) * np.sin(np.linspace(0, np.pi, n)) ** 2 * .35
def rumble(sec=2.4): n = int(SR * sec); return lpf_fft(bnoise(sec, 20, 200), 140) * np.sin(np.linspace(0, np.pi, n)) ** 1.5
S = {"boom": boom(), "shatter": shatter(), "riser": riser(), "whoosh": whoosh(), "clink": clink(), "snap": snap(), "bell": bell(), "shimmer": shimmer(), "rumble": rumble()}
for k, v in S.items(): save(f"assets/sfx/{k}.wav", v)
ev = [("bell", LS[1] + 7.2), ("whoosh", LS[3] + 2.2), ("whoosh", LS[3] + 2.9), ("whoosh", LS[3] + 3.6), ("shimmer", LS[3] + 4.6), ("rumble", LS[4] + 3.7),
      ("riser", hit5 - 1.6), ("boom", hit5), ("shatter", hit5 + 0.05),
      ("clink", ST[9] + 1.6), ("clink", ST[9] + 1.9), ("clink", ST[9] + 2.2), ("rumble", ST[9] + 0.3), ("snap", snap9), ("boom", snap9 + 0.02), ("whoosh", snap9 + 0.3),
      ("bell", LS[11] + 0.1)]
json.dump([(n, round(t, 2)) for n, t in ev], open("assets/sfx/sfx.json", "w"))

# ---------- musik ----------
n = int(SR * TOTAL); t = np.arange(n) / SR; out = np.zeros(n)
def inten(tt):   # 0..1 kurva ketegangan
    pts = [(0, .25), (10, .3), (21, .5), (30, .45), (39, .8), (hit5, 1.0), (hit5 + 3, .5), (47.8, .45), (56.8, .35), (65.7, .5), (75, .6), (snap9, .85), (snap9 + 2, .4), (84.4, .45), (94.3, .55), (TOTAL - 3, .3), (TOTAL, 0)]
    xs, ys = zip(*pts); return np.interp(tt, xs, ys)
I = inten(t)
# drone
drone = (np.sin(2 * np.pi * 36.7 * t) + .6 * np.sin(2 * np.pi * 73.4 * t + 1) + .35 * np.sin(2 * np.pi * 110.0 * t + 2)) * (.55 + .25 * np.sin(2 * np.pi * t / 13.0))
out += drone * .22 * (.6 + .6 * I)
# pad senar (saw aditif, low-pass), progresi Dm - Bb - Gm - A
chords = [[146.8, 174.6, 220.0], [116.5, 146.8, 174.6], [98.0, 116.5, 146.8], [110.0, 138.6, 164.8]]
seg = TOTAL / 8.0
pad = np.zeros(n)
for ci in range(8):
    ch = chords[ci % 4]; a, b = int(ci * seg * SR), int(min((ci + 1) * seg * SR + 2 * SR, n)); xs = t[a:b] - t[a]
    e = np.minimum(1, xs / 2.5) * np.minimum(1, (len(xs) - np.arange(len(xs))) / (2 * SR))
    for f in ch:
        for det in (-0.6, 0, 0.7):
            w = sum(np.sin(2 * np.pi * (f + det) * h * xs + rng.uniform(0, 6.3)) / h for h in range(1, 9))
            pad[a:b] += w * e * .05
pad = lpf_fft(pad, 900)
out += pad * (.55 + .8 * I)
# paduan suara samar (formant) saat teori & ketegangan
choir = np.zeros(n)
for f in (293.7, 349.2, 440.0):
    vib = 1 + .004 * np.sin(2 * np.pi * 5.2 * t + f); choir += np.sin(2 * np.pi * f * vib * t) * .5 + np.sin(2 * np.pi * 2 * f * vib * t) * .18
choir *= np.clip((I - .45) * 2, 0, 1) * .05
out += choir
# timpani + denyut
def timp(a=1.0):
    ln = int(SR * 1.4); x = np.arange(ln) / SR
    return np.sin(2 * np.pi * np.cumsum(95 * np.exp(-x * 5) + 52) / SR) * np.exp(-x * 3.2) * a + lpf_fft(bnoise(1.4, 30, 600), 300) * np.exp(-x * 9) * .3 * a
def put(tt, sig, g=1.0):
    i = int(tt * SR); 
    if i < n: out[i:i + len(sig)] += sig[: n - i] * g
beat = 60 / 52
tt = LS[3] + .6
while tt < TOTAL - 4:
    amp = float(np.interp(tt, [LS[3], hit5, hit5 + 3, TOTAL], [.5, .9, .35, .3]))
    if not (hit5 - .15 < tt < hit5 + 3.2) and abs(tt - snap9) > .2: put(tt, timp(amp * .55), .5)
    tt += beat * 2
put(LS[3] + 1.0, timp(1.0), .8); put(snap9, timp(1.0), .9)
out[int((hit5 - .25) * SR):int((hit5 - .02) * SR)] *= 0.08     # jeda tipis sebelum hantaman
put(hit5, boom(3.2), .55)
# fade akhir
out *= np.minimum(1, (TOTAL - t) / 3.0)
save("assets/bgm.wav", out, .8)
print("ok", TOTAL, "s")
