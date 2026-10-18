# (500) Days of Summer — motion graphic 60 dtk

Video vertikal 1080×1920, 60 detik, bahasa Indonesia. Semua visual orisinal (SVG/HTML/GSAP), musik dan SFX sintetis.

## Alur
- `BRIEF.md`, `frame.md`, `VO_SCRIPT.md` — brief, spesifikasi desain, naskah VO (opsional).
- `index.html` — komposisi (8 scene, subtitle selalu tampil).
- `python3 scripts/make_audio.py` — buat ulang `assets/bgm.wav` dan `assets/sfx/*`.
- `python3 scripts/add_audio.py` — susun blok `<audio>`; otomatis menyertakan VO jika `assets/vo/01..08.wav` ada.
- `npm run check` · `npx hyperframes preview --background` · `npm run render`

## Menambah VO
1. Generate 8 baris di `VO_SCRIPT.md` (bahasa `id`), simpan sebagai `assets/vo/01.wav` … `08.wav`.
2. `python3 scripts/add_audio.py`, lalu carve musik di bawah suara (skill `hyperframes-audio`, `scripts/carve.mjs --comp index.html`).
3. Pastikan tiap file lebih pendek dari slot di tabel naskah.
