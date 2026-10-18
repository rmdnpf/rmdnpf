# Prototipe Adegan 7 — Kembali menggambar

1080×1920, 30 fps, 4,7 dtk. **VO 07 belum final**: tidak ada VO; subtitle memakai teks draf ("Adiknya mengingatkan: Tom hanya mengingat yang indah." / "Ia pun kembali menggambar."), hanya musik/SFX placeholder. Aset asli, VO, storyboard lama, dan implementasi utama tidak diubah.

- Bangun: `python3 scripts/prep.py` lalu `python3 scripts/build_index.py`
- Cek: `plugin-cli.mjs check` · Render: `plugin-cli.mjs render . -q draft -o renders/draw-preview-draft.mp4`
- Aset: `assets/new/`: plat P1 (di-grade malam), `tom-draw-new`, `rachel-new`.
- Alur: cahaya pintu terbuka dan Rachel muncul (tanpa berjalan), ia menjangkau Tom, foto kenangan hangat bergeser dan halaman abu muncul di sela-selanya, label "RACHEL · ADIK TOM", garis gedung tergambar di papan, lembar sketsa menumpuk jadi portofolio.

## Keterbatasan
Rachel muncul dengan fade, bukan masuk dari pintu (tidak ada aset berjalan); ujung tangannya hampir menyentuh punggung Tom, kontak tidak sempurna; foto, halaman abu, dan sketsa dari kode; Tom menggambar dalam pose tunggal (hanya napas).
