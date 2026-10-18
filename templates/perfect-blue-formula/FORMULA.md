# Formula konten "Perfect Blue" — untuk dipakai ulang di film lain

Sumber: `videos/perfect-blue-60s/` (hasil yang dinilai berhasil). Tujuan file ini: konsep yang sama, film berbeda.

## 1. Inti konsep (jangan diubah)
1. **Satu metafora visual yang lahir dari tema film.** Perfect Blue: identitas retak → layar/jendela OS bertumpuk, kaca retak, cermin.
   Film baru wajib punya metafora sendiri (contoh Invincible: foto keluarga yang retak + altimeter vertikal). Tanyakan dulu: "apa tema filmnya, benda/ruang apa yang bisa merepresentasikannya?"
2. **Busur 8–10 frame:** peringatan spoiler → hook (pertanyaan, bukan nama film) → judul/tahun/sutradara → tokoh → konflik → titik retak → pengungkapan → makna/tafsiran → penutup (judul + pertanyaan).
3. **Hook = pertanyaan tentang penonton**, bukan sinopsis.
4. **Fakta dan tafsiran dipisah:** tiap baris naskah diberi tag `[F]` fakta / `[T]` tafsiran; fakta dicek ulang sebelum build.
5. **Orisinal sepenuhnya:** tidak ada cuplikan, poster, atau musik resmi. Visual dari aset yang Anda generate + kode; musik/SFX hasil sintesis.

## 2. Bahasa visual
- Palet terbatas: **1 warna dasar gelap + 2 aksen + 1 warna kertas** (Perfect Blue: navy, biru listrik, pink, putih kertas; aksen alarm merah dipakai hemat).
- Tokoh sebagai **siluet satu warna dengan rim light**, latar polos agar mudah di-key. Siluet menjaga semua tokoh seragam dan menghindari masalah wajah/kostum.
- Elemen kerangka khas: jendela/bingkai, kursor/penanda, retakan yang menjalar, glitch RGB/scanline, tipografi League Gothic + Inter/mono.
- Tiap frame: satu fokus, teks besar (vertikal 1080×1920), subtitle di bawah dengan kotak gelap.
- Peristiwa cerita = peristiwa visual + SFX di detik yang sama (retak saat kata "retak", pecah saat twist).

## 3. Mode warna (putuskan SAAT PITCH, jangan berubah di tengah jalan)
| Mode | Tokoh | Kapan dipakai |
|---|---|---|
| **A. Siluet (default, seperti Perfect Blue)** | satu warna + rim light | film dengan nuansa psikologis/gelap, atau bila ingin tampilan seragam antar-konten |
| **B. Berwarna sesuai film** | flat cel-shaded, kostum asli | film yang identitasnya ada di warna kostum (contoh Invincible) |
Pelajaran Invincible: berpindah A→B setelah sketsa memakan satu putaran ulang aset. Pilih sekali di awal.

## 4. Alur kerja (selalu bertahap, persetujuan di tiap langkah)
1. Pitch konsep (2–3 opsi, plus mode warna) → setuju.
2. Naskah VO per baris (tag [F]/[T], emosi Cartesia per baris, ±190–210 kata untuk ±75–85 dtk) + storyboard → setuju.
3. Daftar aset + prompt Gemini (lihat `GEMINI_ASSET_PROMPTS.md`) → Anda generate.
4. Sketsa statis 10 frame (tanpa animasi) → setuju.
5. VO **per baris** (01.wav…10.wav; lebih aman daripada satu file yang dipotong) → durasi VO menentukan timing scene.
6. Animasi GSAP + musik/SFX orisinal + ducking (carve) → check → render → verifikasi.
Aturan: jangan render sebelum sketsa disetujui; jangan menimpa file VO lama dengan unggahan lama.

## 5. Audio
- Musik: pad dingin + denyut rendah; naik di bagian konflik; **jeda hening ±0,15 dtk tepat sebelum momen retak/twist**; resolusi pelan di penutup.
- SFX diikat ke peristiwa: klik, glitch, retak, pecah, hit/boom, tick altimeter, chime penutup.
- VO selalu menang: musik diturunkan otomatis (carve) di bawah suara.

## 6. Kesalahan yang sudah pernah terjadi (hindari)
- Bingkai buatan sendiri tidak pas dengan bingkai di latar → letakkan foto di dalam bukaan bingkai latar.
- Aset bawaan Gemini berlatar "transparan" palsu/kotak-kotak → minta latar putih polos #FFFFFF.
- Tokoh/gambar kelompok yang memuat tokoh utama lagi → tulis eksplisit siapa yang TIDAK boleh ada.
- Jubah/bagian tubuh terpotong di tepi gambar → minta ruang kosong di semua sisi.
- Karakter hasil kode (SVG) terlihat aneh → karakter selalu dari aset yang Anda generate.
