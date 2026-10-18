# Panduan gaya — (500) Days of Summer

Keputusan: figur dipakai **apa adanya** seperti gambar yang disiapkan pengguna (anime cel-shaded berwarna penuh, wajah kosong). Tidak dikonversi ke siluet.
Satu-satunya pemrosesan: potong latar putih menjadi PNG transparan (`scripts/prep_figures.py`), tanpa mengubah warna, garis, atau bayangan.

## Figur
- Sumber: `assets/figures/src/*.png` (asli). Hasil potong: `assets/figures/*.png` (RGBA, dipangkas ke isi).
- Wajah kosong dibiarkan; telinga dan rambut tetap terbaca.
- Warna asli dipertahankan (cokelat, krem, abu, oranye, biru-abu). Tidak ada pewarnaan ulang.
- Pakaian Summer berganti (celana di `lean` dan `stand`, rok di `twirl` dan `walk`); dibaca sebagai hari yang berbeda, sesuai struktur "HARI ke-N".
- `summer-stand` setengah badan: dipakai sebagai potret kecil di grafik (Frame 4), bukan figur penuh.
- `rachel-point` masih berlatar hitam + glow; menunggu versi latar putih (sementara Frame 7 memakai `rachel-pat`).

## Menyatukan figur dengan latar (dikerjakan di kode)
- Warna latar mengikuti terang-gelap figur: figur gelap di atas krem/amber, figur terang di atas biru abu (slate) atau malam (night). Detail di `frame.md`.
- Garis tepi tipis (putih di latar gelap, tinta di latar terang) dan bayangan lembut di bawah kaki, supaya figur terpisah dari latar.
- Frame 5: sisi Ekspektasi hangat dan cerah (amber, krem), sisi Kenyataan abu hangat pudar (figur dikurangi saturasinya lewat filter di komposisi saja, file aslinya tidak diubah).
- Ukuran tampil: tinggi figur sekitar 700–900 px pada kanvas 1080×1920; pendukung sedikit lebih kecil.

## Palet video (diturunkan dari warna figur)
paper #efe3cf · sand #d9c3a0 · ink #2a211c · night #1d2c3f · slate #5f7fa3 (biru Summer) · pale #c9d6e3 · amber #e3a43c · burnt #c8622a · maroon #b8333d (hati) · olive #4d5a34 · reality #8a8178.

## Dibuat dari kode
Kalender, bingkai foto, kartu ucapan, grafik, kota, piringan hitam, layar terbelah, stempel, dan teks.
