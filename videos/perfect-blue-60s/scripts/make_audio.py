"""Sintesis musik latar dingin + SFX orisinal untuk Perfect Blue. Deterministik (seed tetap)."""
import json, subprocess, wave
import numpy as np
SR = 44100
rng = np.random.default_rng(21)

def dur(n):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f"assets/vo/{n:02d}.wav"]))
D = [dur(n) for n in range(1, 8)]
LS, t = {}, 2.2
for n in range(1, 8): LS[n] = t; t += D[n - 1] + 0.4
TOTAL = LS[7] + D[6] + 1.7

def save(name, x, gain=0.9):
    x = x / (np.max(np.abs(x)) + 1e-9) * gain
    with wave.open(name, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((x * 32767).astype("<i2").tobytes())

def env(n, a, d):  # attack & exponential decay
    x = np.arange(n) / SR
    return np.minimum(1, x / max(a, 1e-4)) * np.exp(-x * d)

def bandnoise(sec, f0, f1):
    n = int(SR * sec); X = np.fft.rfft(rng.standard_normal(n)); f = np.fft.rfftfreq(n, 1 / SR)
    X[(f < f0) | (f > f1)] = 0
    return np.fft.irfft(X, n)

# ---------- SFX ----------
def click():
    n = int(SR * .08); x = np.arange(n) / SR
    return (np.sin(2 * np.pi * 2200 * x) * .6 + bandnoise(.08, 2000, 9000) * .8) * env(n, .001, 60)
def glitch():
    n = int(SR * .35); out = np.zeros(n)
    for k in range(7):
        s = int(n * k / 7); ln = int(SR * rng.uniform(.015, .05)); seg = np.sign(rng.standard_normal(ln)) * rng.uniform(.3, 1)
        out[s:s + ln] += seg[: n - s]
    return out * np.linspace(1, .3, n)
def whoosh(sec=.9, rev=False):
    n = int(SR * sec); x = bandnoise(sec, 300, 6000) * np.sin(np.linspace(0, np.pi, n)) ** 2
    return x[::-1] if rev else x
def slam():
    n = int(SR * .7); x = np.arange(n) / SR
    f = 160 * np.exp(-x * 9) + 40; return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, .002, 7) + bandnoise(.7, 200, 4000) * env(n, .001, 14) * .5
def thump():
    n = int(SR * .3); x = np.arange(n) / SR
    return np.sin(2 * np.pi * np.cumsum(90 * np.exp(-x * 20) + 45) / SR) * env(n, .002, 12)
def ping():
    n = int(SR * .5); x = np.arange(n) / SR
    return (np.sin(2 * np.pi * 988 * x) + np.sin(2 * np.pi * 1480 * x) * .5) * env(n, .003, 9)
def shatter():
    n = int(SR * 1.4); out = bandnoise(1.4, 2500, 14000) * env(n, .001, 5)
    for k in range(18):
        s = int(SR * rng.uniform(.05, 1.0)); ln = int(SR * .08); x = np.arange(ln) / SR
        out[s:s + ln] += np.sin(2 * np.pi * rng.uniform(3000, 7000) * x)[: n - s] * np.exp(-x * 40)[: n - s] * .4
    return out
def impact():
    n = int(SR * 2.4); x = np.arange(n) / SR
    return np.sin(2 * np.pi * np.cumsum(70 * np.exp(-x * 2.2) + 38) / SR) * env(n, .003, 1.6) + bandnoise(2.4, 40, 900) * env(n, .002, 2.5) * .5
def chime():
    n = int(SR * 2.2); x = np.arange(n) / SR
    return sum(np.sin(2 * np.pi * f * x) * a for f, a in ((660, 1), (990, .6), (1320, .4), (1980, .25))) * env(n, .005, 2.2)
def curtain(): return whoosh(.8)

SFX = {"click": click(), "glitch": glitch(), "whoosh": whoosh(1.1, True), "slam": slam(), "thump": thump(), "ping": ping(), "shatter": shatter(), "impact": impact(), "chime": chime(), "curtain": curtain()}
for k, v in SFX.items(): save(f"assets/sfx/{k}.wav", v)
ev = [("glitch", .25), ("click", 1.5), ("whoosh", 2.2), ("thump", 7.5), ("slam", LS[3] + .1), ("click", LS[3] + 3.1), ("curtain", LS[3] + 3.3),
      ("ping", LS[4] + 5.3), ("ping", LS[4] + 6.3), ("glitch", LS[4] + 6.8), ("glitch", LS[5] + 4.2), ("shatter", LS[5] + 6.95),
      ("glitch", LS[6] + 6.2), ("impact", LS[6] + 7.0), ("chime", LS[7] + 10.2)]
json.dump([(n, round(t_, 2)) for n, t_ in ev], open("assets/sfx/sfx.json", "w"))

# ---------- Musik latar: pad dingin + denyut + riser ----------
n = int(SR * TOTAL); x = np.arange(n) / SR; out = np.zeros(n)
chords = [[110.0, 164.8, 220.0, 261.6], [98.0, 146.8, 196.0, 233.1], [87.3, 130.8, 174.6, 207.7], [110.0, 164.8, 220.0, 329.6]]
for i, f in enumerate([f for c in chords for f in c]):
    pass
seg = TOTAL / 4
for ci, ch in enumerate(chords):
    a, b = int(ci * seg * SR), int(min((ci + 1) * seg * SR + SR, n)); xs = x[a:b] - x[a]
    for f in ch:
        for det in (-.4, 0, .5):
            out[a:b] += np.sin(2 * np.pi * (f + det) * xs + rng.uniform(0, 6.28)) * 0.05 * np.minimum(1, xs / 3) * np.minimum(1, (b - a - np.arange(b - a)) / SR / 2)
out *= (0.7 + 0.3 * np.sin(2 * np.pi * x / 11))
pulse = np.zeros(n); beat = 60 / 62
tt = 0.0
while tt < TOTAL - 1:
    i = int(tt * SR); ln = int(SR * .45); k = np.arange(ln) / SR
    seg_ = np.sin(2 * np.pi * np.cumsum(70 * np.exp(-k * 14) + 42) / SR) * np.exp(-k * 8)
    amp = .5 if int(tt / beat) % 2 == 0 else .3
    pulse[i:i + ln] += seg_[: n - i] * amp; tt += beat
out += pulse * (0.25 + 0.55 * np.clip((x - LS[3]) / 20, 0, 1))
# riser menuju glitch F5, retakan F6, twist F7
def riser(t0, t1):
    a, b = int(t0 * SR), int(t1 * SR); m = b - a; r = bandnoise(t1 - t0 + 0.1, 800, 9000)[:m] * np.linspace(0, 1, m) ** 2 * .35
    out[a:b] += r
riser(LS[4] + 5.0, LS[4] + 6.8); riser(LS[5] + 5.6, LS[5] + 6.95); riser(LS[6] + 5.2, LS[6] + 7.0)
hole = (int((LS[6] + 6.9) * SR), int((LS[6] + 7.05) * SR)); out[hole[0]:hole[1]] *= 0.05
out *= np.minimum(1, (TOTAL - x) / 2.0)
save("assets/bgm.wav", out, .8)
print("ok", round(TOTAL, 2), "s", {k: round(v, 2) for k, v in LS.items()})
