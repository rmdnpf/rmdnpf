# Prototipe Adegan 5 — Tom menari di kota siang hari

1080×1920, 30 fps, 6,6 dtk. VO lama `assets/vo/06.wav` (tidak diubah, mulai 0,05 dtk), BGM/SFX lama sebagai placeholder. Aset asli, VO, storyboard lama, dan implementasi utama tidak diubah.

- Bangun: `python3 scripts/prep.py` (kunci magenta, siluet, plat 2×) lalu `python3 scripts/build_index.py`
- Cek: `plugin-cli.mjs check` · Render: `plugin-cli.mjs render . -q draft -o renders/dance-preview-draft.mp4`
- Audit teknis: `node scripts/motion_audit.mjs`
- Aset: `assets/new/` (sumber asli `assets/new/src/`): plat P2, empat pose Tom (strut, jump, land, point).
- Bagian: A langkah (0,2–1,8) · B lompat dan mendarat (1,8–3,3) · C menunjuk, burung hinggap (3,3–4,3) · D rangkaian pose, kerumunan, kamera menyapu ke gedung dan sketsa (4,3–6,1) · E pembekuan foto, memutih ke kertas (6,15–6,6).
- Dari kode (bukan aset): siluet kerumunan (dari siluet pose Tom), burung biru, sketsa arsitektur, bayangan, cahaya.

## Keterbatasan
Siluet kerumunan terbaca sebagai bayangan berlapis, bukan orang sungguhan; burung vektor sederhana; pose bergantian tanpa gerak antar-pose (hanya lompat, squash-stretch, dan kamera); latar lantai bergulir sebagai pengganti jalan.
