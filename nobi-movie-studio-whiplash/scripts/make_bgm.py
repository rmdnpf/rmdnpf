"""Sintesis loop drum jazz orisinal (60 dtk) untuk bed musik. Deterministik (seed tetap)."""
import wave
import numpy as np

SR, DUR, BPM = 44100, 55.2, 150
rng = np.random.default_rng(7)
n = int(SR * DUR)
out = np.zeros(n)
beat = 60.0 / BPM

def add(t, sig, gain=1.0):
    i = int(t * SR)
    if i >= n: return
    seg = sig[: n - i]
    out[i:i + len(seg)] += seg * gain

def env(ln, dec): 
    x = np.arange(ln) / SR
    return np.exp(-x * dec)

def hp(x):  # highpass kasar
    return np.concatenate(([0], np.diff(x)))

def kick():
    ln = int(SR * 0.25); x = np.arange(ln) / SR
    f = 120 * np.exp(-x * 18) + 45
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(ln, 14)

def snare():
    ln = int(SR * 0.22)
    return (rng.standard_normal(ln) * 0.8 + np.sin(2 * np.pi * 190 * np.arange(ln) / SR) * 0.4) * env(ln, 22)

def ride():
    ln = int(SR * 0.35)
    return hp(rng.standard_normal(ln)) * env(ln, 16) * 0.5

def crash():
    ln = int(SR * 2.2)
    return hp(rng.standard_normal(ln)) * env(ln, 2.2) * 0.6

# bagian: 0-4.8 sparse, 4.8-49.2 swing ride, 35.2-40.4 roll naik, 49.2-49.6 hening, 49.6 hit verdict
t = 0.0
swing = 2 / 3
k = 0
while t < DUR - 0.01:
    b = t
    if 4.8 <= b < 49.2:
        add(b, ride(), 0.5)
        add(b + beat * swing, ride(), 0.35)           # pola ride swing
        if k % 2 == 1 and not (41.2 <= b < 49.2): add(b, snare(), 0.45)   # backbeat
        if k % 4 == 0 and not (35.2 <= b < 49.2): add(b, kick(), 0.6)
    if 35.2 <= b < 40.4:                                  # roll snare naik
        steps = 4
        for s in range(steps):
            add(b + s * beat / steps, snare(), 0.25 + 0.5 * (b - 35.2) / 5.2)
        add(b, kick(), 0.6)
    if b < 4.8 and k % 2 == 0: add(b, snare(), 0.35)
    t += beat; k += 1

add(0.0, kick(), 0.9)
add(4.8, crash(), 0.5)
add(10.4, crash(), 0.4)
add(21.2, crash(), 0.4)
add(31.6, crash(), 0.4)
# 53.5-54.0 hening lalu hantaman verdict
mask = np.ones(n); mask[int(49.1 * SR):int(49.6 * SR)] = 0.0; out *= mask
add(49.6, kick(), 1.0); add(49.6, snare(), 0.8); add(49.6, crash(), 0.8)

out = out / (np.max(np.abs(out)) + 1e-9) * 0.85
pcm = (out * 32767).astype("<i2")
with wave.open("assets/bgm.wav", "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
print("ok", len(out) / SR, "detik")
