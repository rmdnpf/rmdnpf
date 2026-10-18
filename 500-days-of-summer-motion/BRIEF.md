---
workflow: general-video
flow: automation
storyboard: no
message: "(500) Days of Summer adalah komedi romantis non-linear yang jujur: bukan kisah cinta, tapi kisah tentang berharap terlalu banyak"
destination: shorts-reels
aspect: 1080x1920
language: id
audience: "penonton film umum di Indonesia"
length: 60s
angle: "motion graphic kalender hari-ke-N dengan banyak elemen visual ilustratif, bukan hanya tipografi"
---

## Intent

Motion graphic 60 detik tentang film (500) Days of Summer (2009, sutradara Marc Webb). Bukan hanya tipografi:
ilustrasi vektor orisinal (kalender, tokoh Tom dan Summer versi gaya datar, kartu ucapan, grafik suasana hati,
layar terbelah Ekspektasi vs Kenyataan, piringan hitam, siluet kota Los Angeles, koin, jam, tomat, stempel).
Perangkat visual utama: penghitung "HARI ke-N" yang melompat-lompat, meniru struktur cerita non-linear.
Tanpa spoiler berat. Subtitle Indonesia selalu tampil; narasi (VO) opsional.

## Assets

- assets/vo/01.wav … 08.wav — voice-over Indonesia, opsional (generate dari VO_SCRIPT.md, lalu jalankan scripts/add_audio.py).

## Customizations

- Semua visual orisinal (SVG/HTML/GSAP). Tidak memakai cuplikan, poster, wajah aktor, atau musik asli film.
- Musik dan SFX orisinal hasil sintesis (scripts/make_audio.py).

## Notes

- Fakta yang dipakai: rilis 2009, sutradara Marc Webb, anggaran sekitar US$7,5 juta, durasi sekitar 95 menit,
  kritikus sekitar 85% positif (agregator). Angka pendapatan film sengaja tidak dipakai karena sumber saling berbeda.
- Palet: krem #f6ebd6, tinta #1e2233, biru langit #4c8df6, biru tua #1d3b8b, kuning matahari #ffc93c, mawar #f0647e.
- Font: League Gothic (judul), Space Mono (label dan subtitle).
