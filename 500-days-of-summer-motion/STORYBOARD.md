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
- scene: Layar terbagi dua pita vertikal. Tom (tom-desk, menulis kartu) di kiri dengan kartu ucapan berterbangan; Summer (summer-lean, menoleh) di kanan dengan satu hati yang retak. Garis putus-putus menghubungkan keduanya.
- voiceover: "Tom, penulis kartu ucapan yang percaya cinta sejati. Summer, perempuan yang sama sekali tidak percaya."
- blueprint: comparison-split
- rules: svg-path-draw, waterfall-entry
- assets: tom-desk, summer-lean (tom-ref, summer-ref sebagai acuan gaya)

## Frame 4 — Tak berurutan

- status: outline
- duration: 9s
- transition_in: wipe
- scene: Dinding bingkai foto bernomor hari (1, 8, 31, 34, 290, 322, 488, 500) tertata acak lalu tertukar posisi. Grafik garis bahagia versus patah hati tergambar menembus bingkai, penanda bergantian hati dan bintang.
- voiceover: "Ceritanya melompat-lompat antar hari. Dari hari pertama sampai hari ke-500, bahagia dan patah hati bergantian."
- blueprint: data-chart
- rules: svg-path-draw, counting-dynamic-scale
- assets: tom-stand, summer-stand kecil sebagai penanda di grafik

## Frame 5 — Ekspektasi vs Kenyataan

- status: outline
- duration: 9s
- transition_in: glitch
- scene: Layar terbelah. Atas hangat: balon, konfeti, Tom dan Summer menari (tom-dance, summer-twirl). Bawah pudar abu-biru: hujan, Tom duduk sendirian di bangku (tom-sit), kursi kosong. Garis pemisah menggeser, VS berputar.
- voiceover: "Adegan paling terkenal: ekspektasi lawan kenyataan. Layar terbelah, dan kenyataan tak pernah selembut harapan."
- blueprint: comparison-split
- rules: viewport-change, waterfall-entry
- assets: tom-dance, summer-twirl, tom-sit

## Frame 6 — Kenangan: lagu dan kota

- status: outline
- duration: 7s
- transition_in: crossfade
- scene: Senja Los Angeles: siluet kota, piringan hitam raksasa berputar, equalizer berdenyut. Tom dan Summer berdiri berdampingan di depan kota (tom-summer-walk), titik cahaya jendela menyala satu per satu.
- voiceover: "Tapi ada juga tarian di jalan, lagu-lagu indie, dan kota Los Angeles yang jadi saksi."
- blueprint: camera-journey
- rules: viewport-change, spring-pop-entrance
- assets: tom-summer-walk

## Frame 7 — Angka

- status: outline
- duration: 6.5s
- transition_in: wipe
- scene: Tiga kartu data: cincin 85% dengan tomat, tumpukan koin "US$7,5 juta", jam "95 menit" (diperiksa ulang). Satu figur kecil menunjuk tiap kartu bergantian.
- voiceover: "Dibuat hanya dengan sekitar tujuh setengah juta dolar, dan dipuji kritikus sampai sekarang."
- blueprint: data-chart
- rules: counting-dynamic-scale, stat-bars-and-fills
- assets: tom-point (opsional)

## Frame 8 — Verdict

- status: outline
- duration: 5s
- transition_in: crossfade
- scene: Tom dan Summer duduk berdampingan di bangku menghadap matahari terbit (tom-summer-bench). Stempel "Layak Ditonton" turun, lima bintang menyala empat.
- voiceover: "Layak ditonton? Ya. Terutama kalau kamu pernah berharap terlalu banyak."
- blueprint: titlecard-reveal
- rules: spring-pop-entrance
- assets: tom-summer-bench
