# Prototipe Adegan 1–3 — Menghitung mundur, Kartu terbuka, Dua dunia

1080×1920, 30 fps, 20,6 dtk. VO lama `01–03.wav` (tidak diubah; mulai 0,4 / 5,56 / 11,84 dtk), BGM/SFX lama sebagai placeholder. Aset asli, VO, storyboard lama, dan implementasi utama tidak diubah.

- Bangun: `python3 scripts/prep.py` (kunci magenta, plat 2×) lalu `python3 scripts/build_index.py`
- Cek: `plugin-cli.mjs check` · Render: `plugin-cli.mjs render . -q draft -o renders/opening-preview-draft.mp4`
- Aset: `assets/new/` (sumber asli di `assets/new/src/`): plat P1, `tom-desk-new`, `summer-lean-new`. Huruf tulisan tangan: Caveat (`assets/fonts/caveat.woff2`, SIL OFL).
- Adegan 1 (0–5,5): kalender dengan halaman disobek 500 → 1 (kode), kamera menarik mundur ke kamar malam, kartu "ini bukan kisah cinta" terbang ke kamera. Adegan 2 (5,5–11,8): kartu terbuka dari atas meja (digambar dari kode), judul/tahun/sutradara, sketsa gedung, mendorong ke putih. Adegan 3 (11,8–20,6): kantor siang, rack focus Tom → Summer, cahaya biru merembes, kartu melayang ke garis cahaya, halaman kalender menutup layar.

## Keterbatasan
Adegan 2 seluruhnya dari kode (gaya lebih datar daripada ilustrasi); kalender, kartu, dan sobekan juga dari kode; Tom dan Summer hanya bernapas/bergoyang halus (pose tunggal, tanpa gerakan menulis); kartu terbang berupa sprite sederhana; Summer di kejauhan berukuran kecil karena perspektif plat.
