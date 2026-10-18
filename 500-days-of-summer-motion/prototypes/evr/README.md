# Prototipe Adegan 6 — Ekspektasi vs Kenyataan (v2, aset ilustrasi)

1080×1920, 30 fps, 9,5 dtk. Layar terbelah vertikal; dua panel dibangun dari satu fungsi `panel()` dan satu fungsi blocking `blocking(k, p)`; kamera memakai parameter shot yang sama (`camSet/camMove`). Aset asli, VO, storyboard lama, dan implementasi utama tidak diubah.

- Bangun: `python3 scripts/prep_new_assets.py` (kunci magenta) lalu `python3 scripts/build_index.py`
- Cek: `plugin-cli.mjs check` · Render: `plugin-cli.mjs render . -q draft -o renders/evr-v2-preview-draft.mp4`
- Audit teknis: `node scripts/motion_audit.mjs` (hanya hal terukur: kesamaan kamera, drift kaki, jendela statis)
- Aset baru: `assets/new/` (sumber asli `assets/new/src/`). Tom berdiri memakai `assets/fig/tom-stand.png` (aset lama).
- Shot: A wide 0,2–1,9 · B medium Summer 1,9–3,9 · C pelukan 3,9–5,9 · D insert tangan 5,9–7,5 · E tarik mundur 7,5–9,5.

## Temuan
Lihat laporan di percakapan; ringkasan: pelukan ilustrasi berhasil di Ekspektasi dan terbaca kaku di Kenyataan; transisi pose terjadi di potongan keras (kaki tidak bergeser); Tom berdiri (aset lama) belum sekelas gaya aset baru; plat latar tidak mengikuti spesifikasi garis lantai 78 % sehingga kaki ditempatkan berdasarkan perspektif plat (y dunia 1160).
