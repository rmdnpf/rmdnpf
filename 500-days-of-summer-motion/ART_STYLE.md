# Panduan gaya — (500) Days of Summer: silhouette line-art

Gaya mengikuti Perfect Blue: figur berupa siluet satu warna dengan garis dalam tipis terang, tanpa wajah, latar putih untuk dipotong.
Gambar referensi `assets/ref/tom-ref.png` dan `assets/ref/summer-ref.png` dipakai hanya untuk pakaian, postur, dan proporsi, bukan untuk gaya render.

## Gambar sumber (yang Anda siapkan)
- Isi tubuh: satu warna navy pekat rata (sekitar #0a1a6a), tanpa bayangan, tanpa warna kulit atau pakaian.
- Detail: garis tipis terang di dalam siluet saja (lipatan kemeja, dasi, kancing, pita pinggang, rimpel rok, helai rambut, tali sepatu, gelas).
- Wajah tidak digambar; kepala murni siluet. Telinga dan rambut tetap terbaca dari bentuk luarnya.
- Latar putih polos, tanpa glow, tanpa bayangan lantai; seluruh tubuh terlihat; portrait 1024×1536.
- Properti yang menempel pada pose (kartu, gelas, tas) ikut digambar sebagai siluet.

## Warna adalah identitas (saya yang mewarnai ulang)
Pewarnaan ulang memakai pemetaan terang-gelap seperti `prep_figures.py` di Perfect Blue: badan satu warna, garis dalam jadi tepi terang.

| Karakter | Warna badan | Tepi/garis | Alasan |
|---|---|---|---|
| Summer | biru #4c8df6 | biru muda #cfe0ff | biru adalah warna Summer |
| Tom | krem kertas #f4ead8 | putih hangat | tokoh utama, kontras tertinggi di latar gelap |
| Autumn | oranye #f08a3c | kuning muda | satu-satunya oranye; isyarat musim |
| Rachel, McKenzie, Paul | abu-biru #8fa0c0 | putih | pendukung, tidak menyaingi dua tokoh utama |

## Latar
- Dasar video malam biru-navy (#0b1a33), figur terang di atasnya, seperti Perfect Blue.
- Pembalikan di Frame 5: sisi Ekspektasi berlatar hangat (kuning-krem) dengan siluet navy, sisi Kenyataan berlatar gelap pudar dengan siluet abu. Pembalikan terang-gelap itu sendiri yang menceritakan perbedaannya.
- Elemen kode (kalender, bingkai foto, kartu, grafik, kota, piringan hitam, stempel, teks) memakai palet yang sama.

## Karena siluet tidak berekspresi
- Emosi dibawa oleh gerak dan komposisi: melompat, berputar, menunduk, berjarak. Pose di `ASSET_LIST.md` dipilih untuk itu.
- Pose harus terbaca dari bentuk luar saja; hindari tangan atau properti yang menyatu dengan badan.
- Siluet tiap tokoh harus unik: Tom berambut mencuat dan berdasi tipis menjuntai; Summer berponi dengan rok A-line dan pita; Rachel kecil berkuncir; McKenzie tinggi berjaket; Paul berompi rajut; Autumn berambut sebahu bermantel.

## Proporsi
Tom 1,0 · Summer 0,93 · McKenzie 1,05 · Paul 0,98 · Autumn 0,92 · Rachel 0,78 (tinggi relatif).
