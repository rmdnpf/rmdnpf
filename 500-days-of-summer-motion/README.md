# (500) Days of Summer — motion graphic 60 dtk

Video vertikal 1080×1920, 60 detik, bahasa Indonesia, narasi VO + subtitle. Figur karakter dari gambar pengguna (dipakai apa adanya),
elemen lain orisinal dari SVG/HTML/GSAP, musik dan SFX sintetis.

## Dokumen
`BRIEF.md` · `STORYBOARD.md` · `frame.md` (palet dan naskah warna) · `ART_STYLE.md` · `ASSET_LIST.md` · `VO_SCRIPT.md`

## Alur build (urutan)
1. `python3 scripts/prep_figures.py` — potong latar putih `assets/figures/src/*.png` → `assets/figures/*.png`.
2. Taruh VO di `assets/vo/01.wav … 08.wav` (Cartesia; emosi per baris ada di `VO_SCRIPT.md`).
3. `python3 scripts/make_audio.py` — musik latar dan SFX (membaca `scripts/timing.json`, jadi jalankan setelah langkah 4 bila VO berubah).
4. `python3 scripts/build_index.py` — hitung jadwal dari durasi VO (`make_timing.py`), pasang figur dari `scripts/index.src.html`, susun blok audio (`add_audio.py`).
   Ubah tampilan di `scripts/index.src.html`, bukan di `index.html` (hasil bangun).
5. Carve musik di bawah VO (wajib diulang setiap kali `build_index.py` dijalankan, karena blok audio dibangun ulang):
   ```
   npm i --prefix /tmp/corepkg @hyperframes/core@0.8.170
   node <PLUGIN>/skills/hyperframes/scripts/plugin-cli.mjs --script <PLUGIN>/skills/hyperframes-audio/scripts/carve.mjs --comp index.html --core /tmp/corepkg
   ```
6. `npx hyperframes check` · `npx hyperframes snapshot --at ...` · `npx hyperframes render . -q high -o renders/500-days-of-summer-v2.mp4`

## Catatan
- `rachel-point.png` berlatar hitam + glow, belum dipakai (butuh versi latar putih).
- Fakta: rilis 2009, sutradara Marc Webb, anggaran sekitar US$7,5 juta, sekitar 85% kritikus positif; durasi 95 menit diperiksa ulang sebelum publikasi.
