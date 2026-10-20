# Prompt Final Aset — Prototipe Adegan 6 (Ekspektasi vs Kenyataan)

Enam aset, dibuat bertahap dengan gerbang evaluasi. Prompt ditulis dalam bahasa Inggris (lebih stabil di generator gambar); catatan dalam bahasa Indonesia. Tidak ada aset lama yang diubah; semua file baru masuk ke `prototypes/evr/assets/new/`.

## 0. Urutan kerja (gerbang evaluasi)

| Gerbang | Aset | Lanjut jika |
|---|---|---|
| 1 | `P3-bg`, `summer-greet` | gaya ilustrasi kedua aset menyatu dengan Tom/Summer yang sudah ada; Summer-greet terbaca hangat, bukan antagonis; skala dan lantai cocok |
| 2 | `hug-warm`, `hug-stiff` | pasangan pelukan satu gaya dengan Gerbang 1; anatomi tangan benar; kontras hangat vs kaku terbaca tanpa teks |
| 3 | `hand-insert` (+ lapisan cincin), `P3-fg` | tangan identik di dua varian kecuali cincin; foreground tidak menutupi area aksi |

Jangan membuat keenamnya sekaligus. Setiap gerbang: kirim gambar, saya cek (potong, edge, skala, konsistensi), baru lanjut.

## 1. Sistem bersama (berlaku untuk semua aset)

**Dunia komposisi** 1080×1920 (9:16). Aset dikirim 2× (kamera masuk sampai skala ±2,05).
- Garis lantai (titik pijak kaki) = y 1500 dunia = **78,1 %** dari tinggi kanvas.
- Tinggi Tom berdiri = 800 px dunia = **41,7 %** tinggi kanvas. Summer = **0,93× Tom** (745 px dunia, 38,8 %).
- Pada kanvas 2× (2304×3456 untuk P3-bg): lantai di y=2700, Tom 1440 px, Summer 1340 px.
- Aset karakter dikirim sebagai kanvas sendiri dengan skala yang sama (Tom 1600 px, Summer 1490 px tinggi, alas kaki 40 px dari tepi bawah).

**Arah cahaya (kunci):** matahari senja keemasan masuk dari **kanan layar** lewat pintu kaca teras; cahaya tepi (rim) hangat di sisi kanan setiap figur; isian sejuk redup dari kiri (ruang dalam). Bayangan jatuh ke kiri-bawah, lunak. Sama di semua aset.

**Gaya:** ilustrasi 2D sel-datar bergaya anime film (seperti figur yang sudah ada): kontur tinta bersih, blok bayangan datar 2–3 nada, tekstur kertas halus. Palet film: kertas #efe3cf, pasir #d9c3a0, tinta #2a211c, biru #a9c6e3/#6f9bc9/#3f6aa0, amber #e3a43c, bata #c8622a, marun #b8333d. Warna dasar netral-hangat; grading ekspektasi vs kenyataan dilakukan di kode.

**Wajah:** kosong tanpa fitur (kulit polos), seperti referensi yang sudah ada. Rambut dan postur yang membawa emosi.

**Kostum — kanon pesta (jangan berubah antar aset):**
- Tom: hoodie hitam berzipper terbuka di atas kemeja abu-krem, dasi hitam tipis, tas selempang khaki-zaitun, celana cokelat tua, sneakers gelap berlist krem. (sesuai `tom-stand.png`)
- Summer: blus putih tanpa lengan berkerah kecil, rok mengembang biru-keabuan sebetis-atas-lutut, flat shoes navy, tas bahu cokelat kecil. (sesuai `summer-twirl.png` dan `summer-walk.png`). Catatan: `summer-lean`/`summer-stand` berkostum celana abu — itu kostum lain, jangan dicampur dalam adegan ini; `summer-greet` baru menggantikannya di adegan 6.

**Referensi yang selalu dilampirkan:** `assets/figures/src/tom-stand.png`, `assets/figures/src/summer-twirl.png`, `assets/figures/src/summer-walk.png` (kostum + gaya). Untuk Gerbang 2–3 lampirkan juga hasil `summer-greet` dan `P3-bg` yang sudah disetujui.

**Teknis umum:** PNG 8-bit sRGB. Aset karakter/tangan/foreground dibuat di **latar magenta solid #FF00FF** (bukan putih: blus putih dan halo putih merusak pemotongan sebelumnya), tanpa glow, bayangan, atau gradasi latar; tepi tajam bersih tanpa tepi putih. Tanpa teks, tanda air, atau logo. Nama file persis seperti di bawah.

**Negative prompt bersama:** photo, photorealistic, 3D render, face features, eyes, mouth, nose, text, watermark, logo, white outline, halo, glow behind subject, drop shadow on background, extra fingers, fused fingers, extra limbs, cropped feet, cropped hands, motion blur, heavy bloom, lens flare, different outfit, different hairstyle, chibi.

---

## 2. GERBANG 1

### 2.1 `P3-bg` — latar apartemen Summer ke teras atap (tanpa orang)
**Fungsi:** satu plat latar yang di-grade dua kali (hangat/kenyataan dingin) di kode. Bukan placeholder lagi.
**Kanvas:** 2304×3456 px, ilustrasi penuh (bukan alpha). Jendela dunia 1080×1920 diposisikan di tengah; sisi kiri-kanan ±100 px dunia cadangan untuk pan.
**Komposisi (sumbu vertikal 9:16, kamera sejajar mata, horizon rendah):**
- Kiri: ambang pintu masuk apartemen (dinding krem, kusen kayu gelap) tempat Tom berdiri; sedikit lorong gelap di belakang.
- Tengah: ruang tamu pesta sederhana (sofa rendah, rak buku, lampu lantai), lantai kayu hangat. **Tidak ada barang tinggi di x 35–65 %** agar area aksi bersih.
- Kanan: pintu geser kaca terbuka ke teras atap; pagar logam; siluet downtown Los Angeles senja; untaian lampu bohlam kecil menyilang di atas teras.
- Tamu: 3–4 siluet kecil, jauh, buram lembut, di sudut kanan-belakang; tidak ada wajah.
- Garis lantai (batas lantai–dinding) harus ada; titik pijak di y=2700 (78,1 %). Tidak boleh ada karpet bergaris kuat yang menyulitkan kontak kaki.
**Cahaya:** senja keemasan dari kanan lewat pintu kaca, bidang cahaya miring ke lantai kiri-bawah; ruang dalam lebih redup dan sedikit sejuk. Kontras sedang (jangan terlalu gelap; grading kode akan menurunkan/menaikkan).
**Prompt:**
```
2D anime film illustration, flat cel shading, clean ink lines, subtle paper texture, vertical 2:3 composition, no people in the foreground.
Interior of a small Los Angeles apartment during a house party at golden hour, seen straight-on at eye level with a low horizon. Left third: an open apartment entry doorway with cream walls and dark wooden frame. Center: a simple living room with a low sofa, bookshelf and floor lamp pushed to the sides, warm wooden floor, the central band of the image kept empty for characters. Right third: open sliding glass doors onto a rooftop terrace with a metal railing, downtown Los Angeles skyline silhouette at dusk, strings of small bulb lights across the terrace. Three or four tiny faceless guest silhouettes, soft and distant, far right background.
Light: warm amber sunset entering from the right through the glass doors, long soft light shapes falling toward the lower left of the floor; interior slightly cooler and dimmer. Medium contrast, neutral-warm palette: paper #efe3cf, sand #d9c3a0, amber #e3a43c, burnt orange #c8622a, maroon #b8333d, blues #6f9bc9 and #3f6aa0, ink #2a211c.
Floor-wall line at 78% of image height, clearly readable. No text, no logos.
```

### 2.2 `summer-greet` — Summer menyapa Tom
**Fungsi:** Summer menyambut di pintu terbuka; dipakai di dua panel (cahaya/kosmetik membedakan, bukan pose). Menggantikan `summer-lean` di adegan 6.
**Kanvas:** 1400×1700, latar magenta, tinggi tubuh 1490 px, kaki rata di y=1660.
**Pose:** berdiri 3/4, **menghadap KIRI secara native** (ke Tom), berat di satu kaki, bahu terbuka; satu tangan terangkat setinggi bahu sedikit melambai/menyapa, tangan lain memegang tali tas. Tidak sedang bersandar. Rok diam dengan gerakan angin kecil.
**Prompt:**
```
Full-body 2D anime film illustration of a young woman, flat cel shading, clean ink lines, faceless (blank skin-toned face, no eyes, nose or mouth), same character and outfit as the reference images: long wavy dark-brown hair with straight bangs, white sleeveless blouse with small collar, blue-grey flared skirt just above the knee, navy ballet flats, small brown shoulder bag.
Pose: standing in three-quarter view facing LEFT, weight on one leg, shoulders open and relaxed, one hand raised to shoulder height in a small friendly wave, the other hand holding the bag strap. Warm, welcoming body language, not stiff, not distant. Feet fully visible, flat on the ground line.
Light: warm amber key light from the RIGHT with a thin warm rim light on right-side edges, soft cool fill from the left, flat 2-tone shadows.
Solid pure magenta #FF00FF background, no glow, no shadow, no gradient, crisp clean edges, no white outline. Full body, nothing cropped.
```

---

## 3. GERBANG 2 (setelah Gerbang 1 disetujui)

### 3.1 `hug-warm` — pelukan ekspektasi
**Kanvas:** 2200×1700, latar magenta; Tom kiri (1600 px tinggi), Summer kanan (1490 px), alas kaki rata satu garis, lampirkan `summer-greet` sebagai acuan wajah-rambut-kostum.
**Pose:** keduanya berdiri berhadapan dekat (profil 3/4). Tangan Summer melingkar di leher/bahu Tom; tangan Tom melingkar di punggung bawah Summer. Kepala saling condong, pipi hampir bersentuhan, Summer sedikit berjinjit dengan satu kaki sedikit terangkat ke belakang, rok mengembang lembut. Tubuh menempel natural, bukan tumpang tindih; tangan memiliki 5 jari benar.
```
Two-character full-body 2D anime film illustration, same style, outfits and hairstyles as the reference images, both faceless. Tom on the left (black open zip hoodie over grey-cream shirt, thin black tie, khaki-olive messenger bag, dark brown trousers, dark sneakers), Summer on the right (white sleeveless blouse, blue-grey flared skirt, navy flats, brown shoulder bag). They are in a warm, tender embrace: Summer's arms wrapped around Tom's neck and shoulders, Tom's arms around her lower back, heads tilted toward each other cheek-to-cheek, Summer slightly on tiptoe with one foot lifted behind her, skirt softly flaring. Bodies touch naturally with correct anatomy, five fingers per hand, bag straps not tangled.
Tom is 1.075 times Summer's height. Both stand on the same ground line, feet fully visible. Light: warm amber key from the RIGHT, thin warm rim on right edges, soft cool fill from left, flat 2-tone shadows.
Solid pure magenta #FF00FF background, no glow or shadow, crisp clean edges.
```

### 3.2 `hug-stiff` — pelukan kaku (kenyataan)
**Kanvas, skala, garis lantai, kostum, kamera identik dengan `hug-warm`.**
**Pose:** pelukan cepat dan canggung, bukan dingin atau kejam: Tom memeluk erat; Summer membalas ringan dengan satu tangan menepuk punggung Tom, tangan satunya menggantung di sisi; pinggul sedikit menjauh, kepala menoleh sedikit ke arah lain melewati bahu Tom; sopan dan hangat tipis, tidak menolak.
```
Same two characters, outfits, scale, ground line and camera as the previous image. An awkward, brief hug: Tom holds Summer tightly with both arms, Summer returns it politely with one hand lightly patting his back while her other arm hangs at her side, her hips leaning slightly away, her head turned a little aside past his shoulder. Kind and polite, not cold, not hostile. Natural anatomy, five fingers per hand, feet on the same ground line.
Light: warm amber key from the RIGHT with thin warm rim on right edges (identical to the warm hug), soft cool fill from left.
Solid pure magenta #FF00FF background, no glow, no shadow, crisp clean edges.
```
Catatan teknis Gerbang 2: kedua file harus bisa bertukar di titik yang sama (posisi Tom persis sama ±8 px agar potongan antar pose tak melompat).

---

## 4. GERBANG 3

### 4.1 `hand-insert` (+ `hand-insert-ring`)
**Fungsi:** insert tangan dekat; satu ilustrasi, dua varian (tanpa/dengan cincin) yang identik kecuali cincin.
**Kanvas:** 2304×3456, latar magenta untuk tangan+lengan; cincin sebagai **lapisan terpisah** (`hand-insert-ring.png`, alpha, kanvas sama) agar kilau dianimasikan di kode.
**Komposisi:** makro setinggi dada; tangan kiri Summer menyentuh bahu/punggung hoodie hitam Tom, jari manis menghadap kamera di tengah-atas, kulit dan hoodie dari kostum kanon, sebagian blus putih tepi atas. Cahaya dari kanan, rim hangat di tepi jari. Cincin: pita emas tipis dengan berlian kecil di jari manis.
```
Close-up 2D anime film illustration, flat cel shading, clean ink lines. A young woman's left hand resting on the shoulder of a black hoodie (the man's back), ring finger clearly visible in the upper center, five fingers with correct anatomy, soft skin tone, short natural nails. A small edge of a white sleeveless blouse at the top. Warm amber key light from the RIGHT with a thin warm rim on finger edges, soft cool fill from the left. VERSION A: bare ring finger. Draw the ring as a separate layer in VERSION B: thin gold band with one small diamond, same hand, same linework, same position.
Solid pure magenta #FF00FF background, crisp clean edges, no glow.
```

### 4.2 `P3-fg` — lapisan foreground
**Kanvas:** 2304×3456 PNG **alpha** (atau magenta untuk dipotong), sama dengan P3-bg.
**Isi:** elemen foreground buram lembut untuk oklusi/kedalaman: daun tanaman pot di tepi kiri-bawah, bingkai pintu kaca/pagar teras di tepi kanan, mungkin satu gelas di tepi bawah. Seluruhnya di ≤15 % lebar masing-masing sisi; **x 20–80 % harus kosong**. Cahaya dari kanan sama seperti P3-bg.
```
Foreground-only layer for the same apartment scene, 2D anime film illustration, flat cel shading with soft defocus. Left edge: large leaves of a potted plant, bottom-left, slightly blurred and dark. Right edge: part of a glass door frame and metal terrace railing, slightly blurred. Nothing in the central 60% of the width. Warm amber light from the right, rim on right edges. Solid magenta #FF00FF everywhere else, crisp edges, no glow.
```

---

## 5. Evaluasi

**Otomatis (hanya yang terukur):** ukuran/rasio kanvas dan garis lantai, skala Tom/Summer, ketepatan alpha/keying (tidak ada magenta/putih tersisa di tepi), tinggi tubuh dan alas kaki pasangan pelukan, kamera/transform dua panel identik, dimensi cincin vs tanpa cincin, `check` render, sinkron audio, determinisme snapshot. Audit tidak dipakai untuk menilai naturalitas gerak atau kualitas sinematik.

**Manual (wajib, oleh Anda dan saya):** kualitas ilustrasi 2D, kecocokan gaya dengan figur lama, kesesuaian dengan film (kostum, pesta teras atap, Summer tidak antagonis), kewajaran pelukan dan tangan, kontras ekspektasi vs kenyataan tanpa audio, tiap gerakan punya tujuan visual/naratif.

**Kriteria yang direvisi (sesuai arahan):** stillness disengaja boleh untuk penekanan emosional (tidak ada kewajiban gerak per 0,5 dtk); tidak wajib tiga kanal gerak per bidikan, tiap gerakan harus punya fungsi.

---

## 6. Tambahan setelah evaluasi v2

Dua aset untuk merapikan shot berdiri (A, B, E). Lampirkan referensi yang sama (`hug-warm.png`, `summer-greet.png`, dan figur lama di `assets/figures/src/`). Kanvas 1024×1536, latar magenta #FF00FF.

### 6.1 `tom-stand-new` — Tom berdiri (gaya sama dengan hug-warm)
Skala: tinggi Tom ±1440 px pada kanvas (sama dengan Tom di `hug-warm`); kaki rata, alas sepatu ±50 px dari tepi bawah.
```
Full-body 2D anime film illustration, same style, line quality, colors and lighting as the reference image hug-warm: flat cel shading with clean ink lines, faceless character (blank skin-toned face, no eyes, nose or mouth).
A young man standing relaxed in three-quarter view facing RIGHT, weight slightly on one leg, both hands in his trouser pockets, shoulders a little lowered, head slightly turned toward the right. Outfit identical to the reference: black open zip hoodie over a grey-cream shirt, thin black tie, khaki-olive messenger bag across the body, dark brown trousers, dark sneakers with cream trim. Messy dark-brown hair.
Light: warm amber key light from the RIGHT, thin warm rim light on right-side edges, soft cool fill from the left, flat 2-tone shadows. Feet fully visible and flat on the ground.
Solid pure magenta #FF00FF background, no glow, no shadow, no gradient, crisp clean edges, no white outline. Full body, nothing cropped. Canvas 1024x1536, figure about 1440 px tall.
```

### 6.2 `summer-stand-new` — Summer berdiri tanpa lambaian
Untuk sisi Kenyataan setelah pelukan: sopan, hangat tipis, tidak dingin. Skala: tinggi Summer ±1340 px pada kanvas (0,93× Tom).
```
Full-body 2D anime film illustration, same character, outfit, style and lighting as the reference image summer-greet, faceless (blank skin-toned face, no eyes, nose or mouth).
Pose: standing in three-quarter view facing LEFT, weight on one leg, both arms relaxed: one hand holding the brown shoulder-bag strap, the other hand hanging loosely at her side (no waving, no raised hand). Head turned slightly toward the left, shoulders relaxed. Polite and kind, a little reserved, not cold and not hostile. Skirt hangs naturally with a very slight sway.
Outfit identical: long wavy dark-brown hair with straight bangs, white sleeveless blouse with small collar, blue-grey flared skirt above the knee, navy ballet flats, small brown shoulder bag. Feet fully visible and flat on the ground.
Light: warm amber key light from the RIGHT, thin warm rim light on right-side edges, soft cool fill from the left, flat 2-tone shadows.
Solid pure magenta #FF00FF background, no glow, no shadow, no gradient, crisp clean edges, no white outline. Full body, nothing cropped. Canvas 1024x1536, figure about 1340 px tall.
```

Setelah kedua gambar jadi: simpan sebagai `tom-stand-new.png` dan `summer-stand-new.png` di `prototypes/evr/assets/new/src/` (atau kirim ke chat), lalu saya pasang ke prototipe dan render ulang.
