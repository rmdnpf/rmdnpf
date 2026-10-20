---
workflow: general-video
flow: companion
storyboard: yes
message: "(500) Days of Summer jujur sejak awal: ini bukan kisah cinta, ini kisah tentang berharap terlalu banyak. Layak ditonton."
destination: shorts-reels
aspect: 1080x1920
language: id
audience: "penonton film umum di Indonesia"
length: 60s
angle: "ilustrasi kartu ucapan hangat era 2009: kertas, tinta, tanah dan biru abu; hari-hari berhamburan seperti lembar kalender dan foto; tokoh anime berwarna tanpa wajah"
---

## Intent

Motion graphic 60 detik tentang (500) Days of Summer (2009, sutradara Marc Webb). Bukan hanya tipografi: figur Tom dan Summer
(gambar anime tanpa wajah, referensi di assets/ref/), lembar kalender, bingkai foto, kartu ucapan, layar terbelah, piringan hitam,
siluet kota. Narasi Indonesia (Cartesia, di-generate pengguna) menjadi patokan timing; animasi mengikuti durasi tiap baris VO.
Spoiler ringan: Autumn muncul di akhir hanya sebagai isyarat visual (warna, daun), tidak dinamai dan tidak dijelaskan. Fokus: ketepatan pesan dan detail per frame, bukan jumlah efek.

## Assets

- assets/ref/tom-ref.png, assets/ref/summer-ref.png — referensi gaya (latar hitam + cahaya). Dipakai sebagai acuan prompt.
- assets/figures/src/*.png — 14 gambar figur dari pengguna (diterima); assets/figures/*.png — hasil potong latar.
- assets/vo/01.wav … 08.wav — VO hasil generate pengguna dari VO_SCRIPT.md. Belum tersedia.

## Customizations

- Figur dipakai apa adanya dari gambar pengguna (anime berwarna penuh, wajah kosong); hanya latar putih dipotong (scripts/prep_figures.py). Tidak ada konversi siluet atau pewarnaan ulang. Lihat ART_STYLE.md.
- Semua elemen lain (kalender, kartu, kota, piringan hitam, grafik) orisinal dari SVG/HTML/GSAP.
- Musik dan SFX orisinal hasil sintesis; BGM di-carve di bawah VO.
- Tanpa footage, poster, atau musik asli film.
- Karakter pendukung dipakai sebagai cameo visual berlabel kecil (tanpa VO): McKenzie dan Paul (sahabat) di F4, Rachel (label "RACHEL" saja, hubungan keluarga tidak ditulis) di F5 dan F7. Autumn di F8 hanya isyarat. Vance tidak dipakai.
- Total 14 gambar figur, disiapkan pengguna: Tom 5, Summer 4, Rachel 2, McKenzie 1, Paul 1, Autumn 1.

## Notes

- Fakta: rilis 2009, sutradara Marc Webb, anggaran sekitar US$7,5 juta, sekitar 85% kritikus positif (agregator). Angka box office tidak dipakai (sumber berbeda). Durasi sekitar 95 menit: diperiksa ulang sebelum build.
- Palet (dari gambar karakter dan bahasa warna film): paper #efe3cf, sand #d9c3a0, ink #2a211c, night #16243a, deretan biru Summer #dbe8f4 / #a9c6e3 / #6f9bc9 / #3f6aa0 / #1d3a63, amber #e3a43c, burnt #c8622a, maroon #b8333d, olive #4d5a34, reality #8a8178. Warna dipakai sebagai cerita (Tom coklat-krem, Summer biru, hari baik semarak, hari buruk abu). Lihat frame.md.
- Font: League Gothic (judul), Space Mono (label dan subtitle).
- Versi pertama (vektor, krem-kuning) ada di index.html lama; dibangun ulang setelah storyboard disetujui.
