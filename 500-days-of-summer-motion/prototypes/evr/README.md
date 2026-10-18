# Prototipe Adegan 6 — Ekspektasi vs Kenyataan

1080×1920, 30 fps, 9,5 dtk. Hanya folder ini yang berisi pekerjaan baru; proyek utama, VO 07/08, dan aset produksi tidak disentuh. Tidak di-commit.

- Bangun: `python3 scripts/build_index.py` (style.css + timeline.js -> index.html)
- Cek: `plugin-cli.mjs check` · Render: `plugin-cli.mjs render . -q draft -o renders/evr-preview-draft.mp4`
- Audit gerak: `node scripts/motion_audit.mjs`
- Audio: VO lama `assets/vo/05.wav` (tak diubah, mulai 0,05 dtk), BGM/SFX lama sebagai placeholder.
- Latar dan tangan digambar dari kode (PLACEHOLDER). Cutout tepi-bersih dibuat dari sumber di `assets/fig/` (aset asli tidak diubah).

## Hasil
Berhasil: kamera L/R identik (selisih 0,000 px, satu fungsi parameter kamera dan satu fungsi blocking); lima shot dengan potongan keras; tidak ada jendela statis >0,2 dtk; kaki Tom/Summer tidak bergeser di luar busur masuk Summer (0–0,9 dtk, melayang); `check` 0 error; snapshot deterministik; subtitle tanpa kotak; insert tangan tanpa vs dengan cincin terbaca tanpa teks.

Gagal / terbatas:
- Pelukan TIDAK berhasil: aset satu-pose tidak bisa merangkul. Hasilnya dua figur berdiri berdekatan dan sedikit condong. Perlu aset pelukan khusus.
- Perbedaan Ekspektasi vs Kenyataan di shot C terutama dari cahaya/warna dan arah condong, bukan dari aksi.
- Tepi Summer (lean) masih ada halo krem tipis dan serpihan putih di sisi kanan celana; belum bersih 100%.
- Bayangan jatuh hanya elips kontak (bukan bayangan lemparan sesungguhnya); kaki terlihat agak melayang di beberapa frame.
- Tangan dan latar kasar (placeholder). Split subtitle baris 3 ke dua bagian pada 7,0 dtk adalah perkiraan.
- Sinkron audio: chunk ucapan 0,19–1,33 / 1,81–3,76 / 4,59–9,20; subtitle 0,17–1,48 / 1,79–3,79 / 4,58–9,25 (selisih ≤0,15 dtk).
