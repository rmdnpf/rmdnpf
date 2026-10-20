"""Menyusun blok <audio> di index.html (BGM, SFX, dan VO bila file assets/vo/NN.wav ada).
Idempoten: hanya mengganti isi antara penanda AUDIO:START dan AUDIO:END.
Setelah VO ditambahkan, jalankan carve agar musik menyingkir dari suara:
  node <PLUGIN>/skills/hyperframes-audio/scripts/carve.mjs --comp index.html
Pakai: python3 scripts/add_audio.py"""
import json, os, re, wave

TIMING = json.load(open("scripts/timing.json"))
VO_START = [TIMING["L"][str(n)] for n in range(1, 9)]
vo = [(i + 1, t) for i, t in enumerate(VO_START) if os.path.exists(f"assets/vo/{i + 1:02d}.wav")]
lines = []
def _len(path):
    with wave.open(path) as w:
        return w.getnframes() / w.getframerate()

for n, t in vo:
    lines.append(f'      <audio id="vo{n:02d}" src="assets/vo/{n:02d}.wav" data-start="{t}" data-duration="{round(_len(f"assets/vo/{n:02d}.wav"), 2)}" data-track-index="7" data-audio-group="voiceover" data-volume="1"></audio>')
vol = "0.5" if vo else "0.6"
carve = ""
if vo:
    carve = ' data-fx-carve="{&quot;enabled&quot;:true,&quot;sources&quot;:[&quot;voiceover&quot;],&quot;strength&quot;:0.8}"'
lines.append(f'      <audio id="bgm" src="assets/bgm.wav" data-start="0" data-duration="60" data-track-index="8" data-volume="{vol}"{carve}></audio>')
def wav_len(path):
    with wave.open(path) as w:
        return w.getnframes() / w.getframerate()

ends = {}  # track -> waktu selesai; SFX yang tumpang tindih dipindah ke track lain
for i, (name, t) in enumerate(json.load(open("assets/sfx/sfx.json"))):
    tr = 9
    while ends.get(tr, -1) > t:
        tr += 1
    d = round(wav_len(f"assets/sfx/{name}.wav"), 2)
    ends[tr] = t + d
    lines.append(f'      <audio id="sfx{i:02d}" src="assets/sfx/{name}.wav" data-start="{t}" data-duration="{d}" data-track-index="{tr}" data-volume="0.7"></audio>')
block = "      <!-- AUDIO:START -->\n" + "\n".join(lines) + "\n      <!-- AUDIO:END -->"
s = open("index.html").read()
if "<!-- AUDIO:START -->" in s:
    s = re.sub(r"      <!-- AUDIO:START -->.*?<!-- AUDIO:END -->", lambda m: block, s, flags=re.S)
else:
    s = s.replace('      <div id="wipe2"></div>', block + '\n\n      <div id="wipe2"></div>')
open("index.html", "w").write(s)
print("audio ok:", len(vo), "VO,", len(lines) - len(vo) - 1, "SFX")
