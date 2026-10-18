---
workflow: general-video
flow: companion
storyboard: yes
message: "Di balik kehancuran Elden Ring ada kisah Ratu Marika: kehilangan, pemberontakan, dan misteri alasan sebenarnya ia menghancurkan tatanan dunia"
destination: shorts-reels-tiktok
aspect: 1080x1920
language: id
audience: "penggemar game dan dark fantasy di TikTok/Reels/Shorts, termasuk yang belum memahami cerita Elden Ring"
length: 90s
angle: "turun dari mahkota ke akar Erdtree dengan paralaks berlapis; bagian misteri terbelah jadi tiga akar (tiga teori)"
---

## Intent

Video lore sinematik 90 detik berjudul "Mengapa Ratu Marika Menghancurkan Elden Ring?". Bercerita seperti dongeng fantasi tragis,
bukan ulasan gameplay. Hook kuat di 3 detik pertama, konflik bertahap, klimaks Shattering, lalu tiga teori seimbang
(duka atas Godwyn / pemberontakan melawan Greater Will / rencana yang memanfaatkan Tarnished) dan penutup yang membuat penasaran.
Fakta dalam game dibedakan dari teori; teori diberi penanda visual dan kalimat tersendiri.

## Assets

- assets/art/*.png: ilustrasi dari pengguna (Gemini/image generator), 12-15 gambar, setelah storyboard disetujui. Daftar dan prompt di ASSETS.md.
- assets/vo/01.wav ... 11.wav: narasi Cartesia dari pengguna setelah naskah disetujui (VO_SCRIPT.md).

## Customizations

- Metafora visual: kerajaan emas yang runtuh. Kamera turun vertikal dari mahkota ke akar Erdtree; tiap ketinggian adalah satu era.
- Palet dinamis per adegan (emas antik #C4A35A, krem pucat #E9DCC3, arang #292B30, merah gelap #8A3434, biru malam #24334A).
- Font: Cinzel (judul singkat), Inter (subtitle/teks pendukung). Tipografi hanya pendukung.
- Ilustrasi berlapis (subjek terpisah dari latar) agar bisa dianimasikan paralaks.
- Kamu (Claude) membuat: bentuk geometris, simbol, partikel, kabut, cahaya, animasi pecahan Elden Ring (dipotong dari gambar cincin), peta Lands Between sederhana, transisi, musik orisinal dark fantasy ambient, SFX.

## Notes

- Dilarang memakai cuplikan gameplay, cutscene, artwork resmi, atau musik asli Elden Ring. Visual berupa fan illustration orisinal yang terinspirasi.
- Hindari: gaya Perfect Blue, siluet biru navy untuk semua karakter, latar putih polos, vector korporat, gambar statis yang hanya di-zoom, bounce acak, transisi berlebihan, teks memenuhi layar, desain karakter tidak konsisten antar-scene.
- Fakta lore dicek ulang sebelum build; tandai Fakta vs Teori di naskah dan visual.
- Cinzel tidak termasuk font bawaan renderer: akan dibundel lokal (woff2) agar render deterministik.
