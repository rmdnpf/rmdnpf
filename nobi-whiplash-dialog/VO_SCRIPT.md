# Naskah Dialog — "Satu Menit" (Nobi Movie Studio · Whiplash 2014)

Dua suara berbeda di Cartesia (bahasa `id`). Generate PER BARIS, simpan WAV di `assets/vo/` dengan nama persis.

- **Fletcher** — suara pria, tegas dan dingin, sedikit meninggi saat menekankan.
- **Andrew** — suara pria muda, sopan, agak tegang lalu mantap di baris terakhir.

| File | Tokoh | Teks |
|---|---|---|
| `01.wav` | Fletcher | Kamu terlambat satu menit. |
| `02.wav` | Andrew | Maaf, Pak. Macet. |
| `03.wav` | Fletcher | Di panggung, tidak ada macet. Hanya ada yang siap, dan yang tersingkir. |
| `04.wav` | Andrew | Saya siap, Pak. Hitung dari awal. |
| `05.wav` | Fletcher | Lagi. Sampai tanganmu berdarah. |
| `06.wav` | Andrew | Satu ronde lagi. |

Setelah file ada: `node scripts/build.mjs` (timing, subtitle, dan gerak mulut otomatis dari durasi dan volume tiap file),
lalu `npx hyperframes check`, preview, dan render.
