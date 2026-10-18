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
- Latar dasar malam navy supaya warna hangat figur menonjol; elemen dekor memakai palet video.
- Garis tepi putih tipis di sekeliling figur (gaya stiker) agar terpisah dari latar gelap, ditambah bayangan lembut di bawah kaki.
- Frame 5 dibalik: sisi Ekspektasi berlatar hangat dan cerah, sisi Kenyataan gelap dan pudar (figur dikurangi saturasinya lewat filter di komposisi saja, file aslinya tidak diubah).
- Ukuran tampil: tinggi figur sekitar 700–900 px pada kanvas 1080×1920; pendukung sedikit lebih kecil sesuai proporsi.

## Palet video (menyesuaikan warna figur yang hangat dan netral)
navy #0f1b3d (dasar), panel #18295a, biru Summer #5aa0f0 (aksen grafis dan teks), biru muda #cfe3f7, amber #f2b84b, krem #f4ead8, oranye #e8793a, abu-biru #7f8aa3, mawar #e8607a (hanya hati).

## Dibuat dari kode
Kalender, bingkai foto, kartu ucapan, grafik, kota, piringan hitam, layar terbelah, stempel, dan teks.
