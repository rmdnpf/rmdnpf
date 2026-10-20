"""Sintesis musik latar ceria-melankolis + SFX orisinal untuk (500) Days of Summer. Deterministik (seed tetap).
Jalankan dari folder proyek: python3 scripts/make_audio.py"""
import json, wave
import numpy as np

SR = 44100
TOTAL = 60.0
rng = np.random.default_rng(500)


def save(path, x, gain=0.9):
    x = x / (np.max(np.abs(x)) + 1e-9) * gain
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((x * 32767).astype("<i2").tobytes())


def env(n, a, d):
    t = np.arange(n) / SR
    return np.minimum(1, t / max(a, 1e-4)) * np.exp(-t * d)


def bandnoise(sec, f0, f1):
    n = int(SR * sec)
    X = np.fft.rfft(rng.standard_normal(n)); f = np.fft.rfftfreq(n, 1 / SR)
    X[(f < f0) | (f > f1)] = 0
    return np.fft.irfft(X, n)


def pluck(freq, sec, bright=0.5):
    """Karplus-Strong: petikan senar gaya ukulele."""
    n = int(SR * sec); p = int(SR / freq)
    buf = (rng.uniform(-1, 1, p) * bright + np.sin(np.arange(p) / p * 2 * np.pi) * (1 - bright))
    out = np.zeros(n)
    for i in range(n):
        out[i] = buf[i % p]
        buf[i % p] = 0.4975 * (buf[i % p] + buf[(i + 1) % p])
    return out * np.minimum(1, np.arange(n) / (SR * 0.004))


# ---------- SFX ----------
def tick():
    n = int(SR * .06); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * 1800 * t) * .5 + bandnoise(.06, 1500, 8000) * .8) * env(n, .001, 70)

def whoosh():
    n = int(SR * .7); return bandnoise(.7, 400, 7000) * np.sin(np.linspace(0, np.pi, n)) ** 2

def pop():
    n = int(SR * .18); t = np.arange(n) / SR
    return np.sin(2 * np.pi * np.cumsum(900 * np.exp(-t * 25) + 250) / SR) * env(n, .001, 22)

def stamp():
    n = int(SR * .6); t = np.arange(n) / SR
    return np.sin(2 * np.pi * np.cumsum(130 * np.exp(-t * 10) + 45) / SR) * env(n, .002, 8) + bandnoise(.6, 200, 3500) * env(n, .001, 16) * .6

def ding():
    n = int(SR * 1.4); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * 1318 * t) + np.sin(2 * np.pi * 1976 * t) * .4) * env(n, .003, 3.2)

def coin():
    n = int(SR * .5); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * 1568 * t) * (t < .08) + np.sin(2 * np.pi * 2093 * t) * (t >= .08)) * env(n, .002, 7)

def chime():
    n = int(SR * 2.4); t = np.arange(n) / SR
    return sum(np.sin(2 * np.pi * f * t) * a for f, a in ((523, 1), (659, .7), (784, .6), (1046, .4))) * env(n, .005, 1.8)

def vinyl():
    n = int(SR * 1.2); return bandnoise(1.2, 3000, 9000) * env(n, .2, 2) * .3

SFX = dict(tick=tick(), whoosh=whoosh(), pop=pop(), stamp=stamp(), ding=ding(), coin=coin(), chime=chime(), vinyl=vinyl())
for k, v in SFX.items():
    save(f"assets/sfx/{k}.wav", v)

TM = json.load(open("scripts/timing.json"))
L = {int(k): v for k, v in TM["L"].items()}
S = {int(k): v for k, v in TM["S"].items()}
CH = {int(k): v for k, v in TM["chunks"].items()}
cs = lambda n, i: L[n] + CH[n][i][0]
ce = lambda n, i: L[n] + CH[n][i][1]
ev = [("tick", L[1] + .5 + i * .4) for i in range(7)] + [("stamp", cs(1, 1) + 1.4), ("pop", cs(1, 1) + 1.5)]
for n in range(2, 9):
    ev.append(("whoosh", S[n] - .42))
ev += [("stamp", L[2] + .65), ("pop", cs(2, 1)), ("pop", cs(2, 2)),
       ("pop", cs(3, 0) + .9), ("pop", ce(3, 1) - 1.6),
       ("tick", cs(4, 0) + .7), ("tick", cs(4, 0) + 1.5), ("pop", cs(4, 2) + .1), ("ding", cs(4, 2) + 1.0),
       ("pop", S[5] + .9), ("ding", cs(5, 1) + 1.2),
       ("vinyl", S[6] + .3), ("pop", L[6] + 2.3), ("pop", L[6] + 4.3),
       ("ding", cs(7, 1) + .3), ("pop", ce(7, 1) - 1.0)]
ev += [("coin", cs(7, 0) + .6 + i * .22) for i in range(7)]
ev += [("stamp", cs(8, 0) + .45), ("chime", cs(8, 3))] + [("pop", cs(8, 1) + .05 + i * .16) for i in range(5)]
ev.sort(key=lambda e: e[1])
json.dump([(n, round(t, 2)) for n, t in ev], open("assets/sfx/sfx.json", "w"))

S5 = S[5]
# ---------- Musik latar: ukulele + bass + perkusi lembut, 104 BPM ----------
n = int(SR * TOTAL); out = np.zeros(n)
bpm = 104; beat = 60 / bpm
# C - Am - F - G (ceria) lalu Am - F - C - G (lebih rindu) mulai F5 ke belakang
chords = {"C": [261.6, 329.6, 392.0, 523.3], "Am": [220.0, 261.6, 329.6, 440.0], "F": [174.6, 261.6, 349.2, 440.0], "G": [196.0, 293.7, 392.0, 493.9]}
bass = {"C": 65.4, "Am": 55.0, "F": 87.3, "G": 98.0}
prog1 = ["C", "Am", "F", "G"]; prog2 = ["Am", "F", "C", "G"]
bar = beat * 4
nb = int(TOTAL / bar) + 1
for b in range(nb):
    t0 = b * bar
    prog = prog1 if t0 < S5 else prog2
    ch = prog[b % 4]
    # strum: 8 petikan per bar
    for s in range(8):
        tt = t0 + s * beat / 2
        if tt >= TOTAL - 1: break
        note = chords[ch][[0, 2, 1, 3, 0, 2, 1, 3][s]]
        x = pluck(note, .5, .6) * (0.5 if s % 2 else 0.8)
        i = int(tt * SR); out[i:i + len(x)] += x[: n - i] * .35
    # bass pada beat 1 dan 3
    for k in (0, 2):
        tt = t0 + k * beat
        if tt >= TOTAL - 1: break
        m = int(SR * .5); x = np.arange(m) / SR
        bs = np.sin(2 * np.pi * bass[ch] * x) * env(m, .005, 4)
        i = int(tt * SR); out[i:i + m] += bs[: n - i] * .5
    # kick + hat
    for k in range(4):
        tt = t0 + k * beat
        if tt >= TOTAL - 1: break
        m = int(SR * .25); x = np.arange(m) / SR
        if k in (0, 2):
            kick = np.sin(2 * np.pi * np.cumsum(110 * np.exp(-x * 22) + 48) / SR) * env(m, .002, 14)
            i = int(tt * SR); out[i:i + m] += kick[: n - i] * .45
        hat = bandnoise(.06, 6000, 12000) * env(int(SR * .06), .001, 60)
        j = int((tt + beat / 2) * SR); out[j:j + len(hat)] += hat[: n - j] * .12
# fade in/out
x = np.arange(n) / SR
out *= np.minimum(1, x / 1.0) * np.minimum(1, (TOTAL - x) / 2.0)
save("assets/bgm.wav", out, .8)
print("ok", TOTAL, "s;", len(ev), "sfx")
