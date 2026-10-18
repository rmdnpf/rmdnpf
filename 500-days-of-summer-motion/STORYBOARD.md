---
format: 1080x1920
duration: 60s
message: "(500) Days of Summer jujur sejak awal: ini bukan kisah cinta, ini kisah tentang berharap terlalu banyak. Layak ditonton."
arc: "Hook → Judul → Tokoh → Tak berurutan → Ekspektasi/Kenyataan → Kenangan → Angka → Verdict"
audience: "penonton film umum di Indonesia"
mode: collaborative
---

Durasi tiap frame final mengikuti durasi file VO (ditambah jeda 0.4 dtk), seperti Perfect Blue. Angka di bawah adalah perkiraan.

## Frame 1 — Hook: hari ke-500

- status: outline
- duration: 5s
- transition_in: cut
- scene: Malam kota biru. Lembar kalender raksasa; angka "HARI" berputar cepat dari 1 ke 500 sambil lembar-lembar terkelupas dan beterbangan. Stempel "Ini bukan kisah cinta" menghantam, hati patah muncul.
- voiceover: "Cowok bertemu cewek. Tapi sejak awal, ini bukan kisah cinta."
- blueprint: titlecard-reveal
- rules: counting-dynamic-scale, spring-pop-entrance
- assets: (kode saja)

Nilai di beat pertama: janji film yang jujur, bukan nama film.

## Frame 2 — Judul

- status: outline
- duration: 5.5s
- transition_in: wipe
- scene: Judul "(500) DAYS OF SUMMER" dibangun dari lembar kalender yang menempel satu per satu; bingkai foto berayun di kiri-kanan, cahaya hangat merembes dari bawah. Label "2009 · Marc Webb" diketik.
- voiceover: "(500) Days of Summer. Tahun 2009. Sutradara Marc Webb."
- blueprint: typewriter-reveal
- rules: spring-pop-entrance, waterfall-entry
- registry: grain-overlay

## Frame 3 — Tom dan Summer

- status: outline
- duration: 8s
- transition_in: crossfade
- scene: Layar terbagi dua pita vertikal. Tom (tom-desk, menulis kartu) di kiri dengan kartu ucapan berterbangan; Summer (summer-lean, menoleh) di kanan dengan satu hati yang retak. Label "SUMMER · ASISTEN BARU" muncul di samping Summer. Garis putus-putus menghubungkan keduanya.
- voiceover: "Tom, penulis kartu ucapan yang percaya cinta sejati. Summer, asisten baru bosnya, yang tak mau hubungan serius."
- blueprint: comparison-split
- rules: svg-path-draw, waterfall-entry
- assets: tom-desk, summer-lean (tom-ref, summer-ref sebagai acuan gaya)

## Frame 4 — Tak berurutan

- status: outline
- duration: 9s
- transition_in: wipe
- scene: Dinding bingkai foto bernomor hari (1, 8, 31, 34, 290, 322, 488, 500) tertata acak lalu tertukar posisi. Grafik garis bahagia versus patah hati tergambar menembus bingkai, penanda bergantian hati dan bintang. Di sudut kanan-bawah, dua sahabat (mckenzie-cheers, paul-cheers) bersandar di tepi grafik dengan label "MCKENZIE & PAUL · SAHABAT", mengangkat gelas saat grafik naik dan menunduk saat turun.
- voiceover: "Ceritanya melompat-lompat antar hari. Dari hari pertama sampai hari ke-500, bahagia dan patah hati bergantian."
- blueprint: data-chart
- rules: svg-path-draw, counting-dynamic-scale
- assets: tom-stand, summer-stand kecil sebagai penanda di grafik, mckenzie-cheers, paul-cheers

## Frame 5 — Ekspektasi vs Kenyataan

- status: outline
- duration: 9s
- transition_in: glitch
- scene: Layar terbelah. Atas hangat: balon, konfeti, Tom dan Summer menari (tom-dance, summer-twirl). Bawah pudar abu-biru: hujan, Tom duduk sendirian di bangku (tom-sit), kursi kosong. Di sisi Kenyataan, adik Tom (rachel-pat) berdiri di samping bangku dan menepuk bahunya, dengan label "RACHEL · ADIK". Garis pemisah menggeser, VS berputar.
- voiceover: "Adegan paling terkenal: ekspektasi lawan kenyataan. Tom ternyata lebih mencintai bayangannya tentang Summer, bukan Summer yang nyata."
- blueprint: comparison-split
- rules: viewport-change, waterfall-entry
- assets: tom-dance, summer-twirl, tom-sit, rachel-pat

## Frame 6 — Kenangan: lagu dan kota

- status: outline
- duration: 7s
- transition_in: crossfade
- scene: Senja Los Angeles: siluet kota, piringan hitam raksasa berputar, equalizer berdenyut. Tom dan Summer berjalan berdampingan di depan kota (tom-walk, summer-walk, dua gambar terpisah), titik cahaya jendela menyala satu per satu.
- voiceover: "Tapi ada juga tarian di jalan, lagu-lagu indie, dan kota Los Angeles yang jadi saksi."
- blueprint: camera-journey
- rules: viewport-change, spring-pop-entrance
- assets: tom-walk, summer-walk

## Frame 7 — Angka

- status: outline
- duration: 6.5s
- transition_in: wipe
- scene: Tiga kartu data: cincin 85% dengan tomat, tumpukan koin "US$7,5 juta", jam "95 menit" (diperiksa ulang). Rachel (rachel-point) berdiri di tepi kanan dan menunjuk tiap kartu bergantian.
- voiceover: "Dibuat hanya dengan sekitar tujuh setengah juta dolar, dan dipuji kritikus sampai sekarang."
- blueprint: data-chart
- rules: counting-dynamic-scale, stat-bars-and-fills
- assets: rachel-point

## Frame 8 — Verdict: musim berganti

- status: outline
- duration: 7s
- transition_in: crossfade
- scene: Tom duduk sendirian di bangku (tom-sit). Sinar musim panas memudar, lembar kalender "Hari 500" menguning dan berubah menjadi daun-daun musim gugur yang berjatuhan. Dari tepi kanan, satu siluet perempuan berpakaian oranye hangat berjalan masuk (autumn-walk) tanpa dijelaskan. Stempel "Layak Ditonton" turun, lima bintang menyala empat.
- voiceover: "Layak ditonton? Ya. Terutama kalau kamu pernah berharap terlalu banyak. Dan musim pun berganti."
- blueprint: titlecard-reveal
- rules: spring-pop-entrance, waterfall-entry
- assets: tom-sit, autumn-walk

Autumn hanya isyarat visual (warna dan daun); namanya tidak disebut di VO atau teks. Tidak ada penjelasan akhir cerita.
