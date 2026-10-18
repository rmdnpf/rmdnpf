"""Sintesis musik latar orisinal + SFX untuk Invincible (deterministik, seed tetap). Tidak memakai musik/suara resmi."""
import json, wave
import numpy as np
SR = 44100
rng = np.random.default_rng(5)
TM = json.load(open("scripts/timing.json")); LS = {int(k): v for k, v in TM["LS"].items()}; ST = {int(k): v for k, v in TM["ST"].items()}; TOTAL = TM["TOTAL"]

def save(name, x, gain=0.9):
    x = x / (np.max(np.abs(x)) + 1e-9) * gain
    with wave.open(name, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((x * 32767).astype("<i2").tobytes())
def env(n, a, d):
    x = np.arange(n) / SR
    return np.minimum(1, x / max(a, 1e-4)) * np.exp(-x * d)
def bandnoise(sec, f0, f1):
    n = int(SR * sec); X = np.fft.rfft(rng.standard_normal(n)); f = np.fft.rfftfreq(n, 1 / SR)
    X[(f < f0) | (f > f1)] = 0
    return np.fft.irfft(X, n)
def sweep_noise(sec, f0, f1, up=True):
    n = int(SR * sec); x = bandnoise(sec, 200, 9000); t = np.linspace(0, 1, n)
    fc = f0 + (f1 - f0) * t; y = np.zeros(n); lp = 0.0
    a = np.clip(2 * np.pi * fc / SR, 0, 1)
    for i in range(0, n, 1):
        lp += a[i] * (x[i] - lp); y[i] = lp
    return y

# ---------- SFX ----------
def whoosh(sec=1.0, rev=False):
    n = int(SR * sec); x = bandnoise(sec, 300, 6500) * np.sin(np.linspace(0, np.pi, n)) ** 2
    return x[::-1] if rev else x
def boom(sec=2.2, f=62):
    n = int(SR * sec); x = np.arange(n) / SR
    return np.sin(2 * np.pi * np.cumsum(f * np.exp(-x * 2.4) + 34) / SR) * env(n, .003, 1.7) + bandnoise(sec, 40, 700) * env(n, .002, 3) * .55
def hit(sec=1.0):
    n = int(SR * sec); x = np.arange(n) / SR
    return np.sin(2 * np.pi * np.cumsum(110 * np.exp(-x * 14) + 46) / SR) * env(n, .002, 6) + bandnoise(sec, 150, 5000) * env(n, .001, 11) * .6
def crack():
    n = int(SR * .7); out = bandnoise(.7, 1500, 12000) * env(n, .001, 16) * .4
    for k in range(9):
        s = int(SR * rng.uniform(0, .45)); ln = int(SR * .02); out[s:s + ln] += np.sign(rng.standard_normal(ln)) * rng.uniform(.3, 1) * np.linspace(1, 0, ln)
    return out
def shatter():
    n = int(SR * 1.6); out = bandnoise(1.6, 2500, 14000) * env(n, .001, 4.5)
    for k in range(24):
        s = int(SR * rng.uniform(.03, 1.1)); ln = int(SR * .09); x = np.arange(ln) / SR
        out[s:s + ln] += np.sin(2 * np.pi * rng.uniform(2800, 7500) * x)[: n - s] * np.exp(-x * 38)[: n - s] * .45
    return out + boom(1.6, 80) * .35
def heart():
    n = int(SR * .9); out = np.zeros(n)
    for t0, a in ((0, 1), (.28, .7)):
        s = int(SR * t0); ln = int(SR * .22); x = np.arange(ln) / SR
        out[s:s + ln] += np.sin(2 * np.pi * np.cumsum(70 * np.exp(-x * 18) + 38) / SR) * np.exp(-x * 14) * a
    return out
def horn(sec=2.6, f=55):
    n = int(SR * sec); x = np.arange(n) / SR; y = np.zeros(n)
    for h, a in ((1, 1), (2, .7), (3, .5), (4, .3), (5, .2)): y += np.sin(2 * np.pi * f * h * x + h) * a
    return y * np.minimum(1, x / .6) * np.minimum(1, (sec - x) / .9)
def chime():
    n = int(SR * 3.0); x = np.arange(n) / SR
    return sum(np.sin(2 * np.pi * f * x) * a for f, a in ((440, 1), (660, .6), (880, .45), (1320, .25))) * env(n, .005, 1.5)
def drip():
    n = int(SR * .35); x = np.arange(n) / SR
    return np.sin(2 * np.pi * (1500 - 900 * x * 3) * x) * env(n, .002, 14)
def tick():
    n = int(SR * .12); x = np.arange(n) / SR
    return (np.sin(2 * np.pi * 1760 * x) * .6 + bandnoise(.12, 3000, 9000) * .3) * env(n, .001, 40)

SFX = {"whoosh": whoosh(1.2, True), "whoosh_out": whoosh(1.4), "boom": boom(), "hit": hit(), "crack": crack(), "shatter": shatter(), "heart": heart(), "horn": horn(), "chime": chime(), "drip": drip(), "tick": tick()}
for k, v in SFX.items(): save(f"assets/sfx/{k}.wav", v)
L = LS
ev = [("tick", .4), ("crack", L[1] + 8.4), ("boom", L[2] + .1), ("tick", ST[3] + .2), ("whoosh", ST[4] + .2), ("whoosh", ST[4] + .5),
      ("heart", L[5] + .8), ("heart", L[5] + 2.3), ("heart", L[5] + 3.8), ("heart", L[5] + 5.0), ("boom", L[5] + 5.6), ("heart", L[5] + 7.4), ("hit", L[5] + 6.6),
      ("crack", L[6] + 5.0), ("shatter", L[6] + 8.1), ("horn", L[7] + .6), ("hit", L[7] + 3.4),
      ("hit", L[8] + 1.6), ("hit", L[8] + 3.2), ("boom", L[8] + 4.8), ("drip", L[8] + 8.0), ("whoosh_out", L[8] + 7.3),
      ("crack", L[9] + 4.2), ("hit", L[10] + 3.6), ("chime", L[10] + 6.0)]
json.dump([(n, round(t_, 2)) for n, t_ in ev], open("assets/sfx/sfx.json", "w"))

# ---------- Musik latar (A minor) ----------
n = int(SR * TOTAL); x = np.arange(n) / SR; out = np.zeros(n)
def pad(t0, t1, freqs, amp, bright=1.0):
    a, b = int(t0 * SR), min(int(t1 * SR), n); xs = x[a:b] - x[a]; sec = t1 - t0
    e = np.minimum(1, xs / 2.0) * np.minimum(1, (sec - xs) / 2.0)
    for f in freqs:
        for det in (-.5, 0, .6):
            ph = rng.uniform(0, 6.28)
            y = np.sin(2 * np.pi * (f + det) * xs + ph) + .35 * bright * np.sin(2 * np.pi * 2 * (f + det) * xs + ph) + .15 * bright * np.sin(2 * np.pi * 3 * f * xs)
            out[a:b] += y * e * amp
def pluck(t0, f, amp=.12, dec=3.0):
    a = int(t0 * SR)
    if a >= n: return
    ln = min(int(SR * 2.2), n - a); xs = np.arange(ln) / SR
    y = (np.sin(2 * np.pi * f * xs) + .4 * np.sin(2 * np.pi * 2 * f * xs) * np.exp(-xs * 6) + .2 * np.sin(2 * np.pi * 3 * f * xs) * np.exp(-xs * 9)) * np.exp(-xs * dec) * np.minimum(1, xs / .004)
    out[a:a + ln] += y * amp
N = dict(A2=110, C3=130.8, D3=146.8, E3=164.8, F3=174.6, G3=196, A3=220, C4=261.6, D4=293.7, E4=329.6, F4=349.2, G4=392, A4=440, C5=523.3, E5=659.3)
CH = {"Am": [110, 164.8, 220, 261.6], "F": [87.3, 130.8, 174.6, 220], "C": [130.8, 196, 261.6, 329.6], "G": [98, 146.8, 196, 246.9], "Dm": [73.4, 110, 146.8, 174.6], "E": [82.4, 123.5, 164.8, 207.7]}
def sec(key): return ST[key]
# F1-F2 tenang/misterius
pad(0, ST[3] + 1, CH["Am"], .035, .6)
arp = ["A3", "C4", "E4", "A4", "E4", "C4"]
t = 1.0; i = 0
while t < ST[3]: pluck(t, N[arp[i % 6]], .09, 2.6); t += .75; i += 1
# F3-F4 naik heroik
pad(ST[3], ST[4] + 4, CH["F"], .045); pad(ST[4], ST[4] + 10, CH["C"], .055, 1.4); pad(ST[4] + 5, ST[5] + .5, CH["G"], .05, 1.4)
t = ST[3] + .5; i = 0; arp2 = ["F3", "A3", "C4", "F4", "C4", "A3", "G3", "D4"]
while t < ST[5]: pluck(t, N[arp2[i % 8]], .1, 2.2); t += .5; i += 1
# denyut tegang di F4
tt = ST[4]
while tt < ST[5] - .5:
    k = np.arange(int(SR * .4)) / SR; a = int(tt * SR); y = np.sin(2 * np.pi * np.cumsum(70 * np.exp(-k * 16) + 44) / SR) * np.exp(-k * 9); out[a:a + len(y)] += y[: n - a] * .22; tt += .5
# F5 gelap: drone rendah + disonan, riser ke kehancuran
pad(ST[5], ST[6] + 1, [55, 82.4, 116.5], .06, .5)
a, b = int((L[5] + 3.5) * SR), int((L[5] + 5.6) * SR); out[a:b] += bandnoise((b - a) / SR + .05, 600, 9000)[: b - a] * np.linspace(0, 1, b - a) ** 2 * .3
h0, h1 = int((L[5] + 5.5) * SR), int((L[5] + 5.62) * SR); out[h0:h1] *= .05
# F6 sedih/retak
pad(ST[6], ST[7], CH["Dm"], .045); 
for j, f in enumerate(["D4", "F4", "A4", "G4", "F4", "E4"]): pluck(ST[6] + 1.0 + j * 1.4, N[f], .1, 1.6)
h0, h1 = int((L[6] + 8.0) * SR), int((L[6] + 8.12) * SR); out[h0:h1] *= .05
# F7 Viltrum: horn rendah + ketukan
pad(ST[7], ST[8] + 1, CH["E"], .05, 1.6)
tt = ST[7] + .5
while tt < ST[8]:
    k = np.arange(int(SR * .5)) / SR; a = int(tt * SR); y = np.sin(2 * np.pi * np.cumsum(60 * np.exp(-k * 12) + 36) / SR) * np.exp(-k * 6); out[a:a + len(y)] += y[: n - a] * .3; tt += 1.0
# F8 pertarungan -> sedih
pad(ST[8], L[8] + 7.3, CH["Am"], .06, 1.5); pad(L[8] + 4.5, ST[9] + 1, CH["F"], .05)
tt = ST[8] + .3
while tt < L[8] + 7.0:
    k = np.arange(int(SR * .4)) / SR; a = int(tt * SR); y = np.sin(2 * np.pi * np.cumsum(75 * np.exp(-k * 14) + 42) / SR) * np.exp(-k * 8); out[a:a + len(y)] += y[: n - a] * .3; tt += .6
# F9 piano sedih
pad(ST[9], ST[10] + 1, CH["Am"], .035, .5)
mel = [("E4", 0), ("A4", 1.2), ("C5", 2.4), ("B4" if False else "A4", 3.6), ("G4", 4.8), ("E4", 6.0)]
for f, dt in mel: pluck(ST[9] + .8 + dt, N[f], .13, 1.3)
# F10 penyelesaian (A mayor-minor, harapan)
pad(ST[10], TOTAL, [110, 164.8, 220, 277.2, 329.6], .05, 1.2)
for j, f in enumerate(["A4", "C5", "E5", "C5", "A4"]): pluck(ST[10] + .6 + j * .9, N[f], .1, 1.8)
out *= (.85 + .15 * np.sin(2 * np.pi * x / 9))
out *= np.minimum(1, (TOTAL - x) / 2.5)
save("assets/bgm.wav", out, .8)
print("ok", TOTAL, len(ev), "sfx")
