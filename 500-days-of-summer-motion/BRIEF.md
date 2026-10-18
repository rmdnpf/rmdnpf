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
angle: "malam kota biru-hangat, hari-hari berhamburan seperti lembar kalender dan foto; tokoh gambar anime tanpa wajah"
---

## Intent

Motion graphic 60 detik tentang (500) Days of Summer (2009, sutradara Marc Webb). Bukan hanya tipografi: figur Tom dan Summer
(gambar anime tanpa wajah, referensi di assets/ref/), lembar kalender, bingkai foto, kartu ucapan, layar terbelah, piringan hitam,
siluet kota. Narasi Indonesia (Cartesia, di-generate pengguna) menjadi patokan timing; animasi mengikuti durasi tiap baris VO.
Spoiler ringan: Autumn muncul di akhir hanya sebagai isyarat visual (warna, daun), tidak dinamai dan tidak dijelaskan. Fokus: ketepatan pesan dan detail per frame, bukan jumlah efek.

## Assets

- assets/ref/tom-ref.png, assets/ref/summer-ref.png — referensi gaya (latar hitam + cahaya). Dipakai sebagai acuan prompt.
- assets/figures/src/*.png — gambar sumber latar putih polos (lihat ASSET_LIST.md). Belum tersedia.
- assets/vo/01.wav … 08.wav — VO hasil generate pengguna dari VO_SCRIPT.md. Belum tersedia.

## Customizations

- Figur bergaya silhouette line-art seperti Perfect Blue: hapus latar putih, lalu warnai ulang per karakter (Summer biru, Tom krem, Autumn oranye, pendukung abu-biru). Lihat ART_STYLE.md.
- Semua elemen lain (kalender, kartu, kota, piringan hitam, grafik) orisinal dari SVG/HTML/GSAP.
- Musik dan SFX orisinal hasil sintesis; BGM di-carve di bawah VO.
- Tanpa footage, poster, atau musik asli film.
- Karakter pendukung dipakai sebagai cameo visual berlabel kecil (tanpa VO): McKenzie dan Paul (sahabat) di F4, Rachel (adik) di F5 dan F7. Autumn di F8 hanya isyarat. Vance tidak dipakai.
- Total 14 gambar figur, disiapkan pengguna: Tom 5, Summer 4, Rachel 2, McKenzie 1, Paul 1, Autumn 1.

## Notes

- Fakta: rilis 2009, sutradara Marc Webb, anggaran sekitar US$7,5 juta, sekitar 85% kritikus positif (agregator). Angka box office tidak dipakai (sumber berbeda). Durasi sekitar 95 menit: diperiksa ulang sebelum build.
- Palet: navy #0b1a33, panel #13264a, biru Summer #4c8df6, hangat #f2b872, kertas #f4ead8, mawar #f0647e (aksen tunggal).
- Font: League Gothic (judul), Space Mono (label dan subtitle).
- Versi pertama (vektor, krem-kuning) ada di index.html lama; dibangun ulang setelah storyboard disetujui.
