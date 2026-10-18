# Rencana Aset — Adegan 1–5 dan 7–8 (berdasarkan pelajaran adegan 6)

Dokumen ini melanjutkan `prototypes/evr/ASSET_PROMPTS.md`. Tidak ada kode, render, atau perubahan pada implementasi utama, VO, dan aset lama. VO 07 dan 08 tetap belum final.

## 1. Pelajaran dari adegan 6 yang mengubah cara kita meminta aset

1. **Satu gaya.** Hasil terbaik muncul ketika figur dan plat dibuat di gaya yang sama (ilustrasi berwarna hangat dengan cahaya tepi dari kanan). Figur lama (`tom-desk`, `tom-walk`, `tom-sit`, `summer-lean`, `rachel-pat`, `autumn-walk`, dll.) bergaya lebih datar dan Summer lama memakai celana, bukan kostum rok. Rekomendasi: **buat ulang pose yang dibutuhkan di gaya baru**, jangan campur.
2. **Aset sekali pakai di latar magenta (#FF00FF)**, bukan putih. Pemotongan bersih, nol sisa magenta di tepi.
3. **Plat harus punya lantai/tanah yang terbaca** dan tinggi mata kamera yang jelas, supaya kaki karakter bisa ditempatkan menurut perspektif. Pada adegan 6, lantai kosong terlalu besar dan kaki ditempatkan berdasarkan perspektif plat, bukan garis lantai 78 %.
4. **Gerak datang dari ganti pose pada potongan keras, kamera, parallax, dan cahaya**, bukan dari gerak tubuh. Maka tiap adegan yang butuh gerak perlu **beberapa pose** (mis. tarian), bukan satu pose.
5. **Kostum kanon (dipakai di semua aset):**
   - Tom: hoodie hitam berzipper terbuka di atas kemeja abu-krem, dasi hitam tipis, tas selempang khaki-zaitun, celana cokelat tua, sneakers gelap berlist krem.
   - Summer: blus putih tanpa lengan berkerah kecil, rok mengembang biru-keabuan, flat shoes navy, tas bahu cokelat.
   - Rachel, Autumn, McKenzie, Paul: dibuat dari referensi lama (`assets/figures/src/`), kostum sama dengan aslinya.

## 2. Gerbang kerja (jangan dibuat sekaligus)

| Gerbang | Isi | Adegan | Lanjut jika |
|---|---|---|---|
| **1** | **P2** jalan LA siang + pose tarian Tom (3–4) | 5 | gaya cocok dengan aset adegan 6; skala dan lantai terbaca; pose bisa digilir tanpa lompatan |
| **2** | **P1** kamar kerja/kantor + `tom-desk`, `summer-lean`, `tom-draw`, `rachel` (gaya baru) | 1, 2, 3, 4, 7 | satu plat bisa di-grade menjadi kantor siang dan apartemen malam; Rachel terbaca sebagai adik, bukan pacar |
| **3** | **P4** bangku taman, **P5** lobi biro arsitektur + `tom-sit`, `summer-sit`, `summer-walk`, `autumn`, `tom-walk` | 4, 8 | Autumn jelas bukan pengganti Summer; cahaya konsisten |

Adegan 1 dan 2 (kalender, kartu) hampir seluruhnya dari kode; keduanya memakai P1 dan `tom-desk`, jadi tidak butuh gerbang sendiri. Adegan 4 memakai figur yang sama dari Gerbang 2 dan 3, ditambah McKenzie dan Paul (gaya baru) jika Anda setuju.

## 3. Gerbang 1 — Adegan 5 (Tom menari di kota siang hari)

**Yang menentukan adegan ini:** gerak Tom. Karena tidak ada siklus gerak, adegan dibangun dari **3–4 pose tarian** yang berganti pada ketukan, ditambah lompatan, bayangan di aspal, parallax gedung, dan siluet orang yang ikut menari (dari kode). Burung biru dan sketsa arsitektur dari kode.

### Kanvas dan skala (berlaku untuk semua aset Gerbang 1)
- Pose Tom: kanvas 1024×1536, latar magenta #FF00FF, skala tubuh **sama dengan `tom-new`** (tinggi berdiri ≈1440 px; kepala ≈ 1/7,5 tinggi tubuh).
- Pose yang menyentuh tanah: alas sepatu ±50 px dari tepi bawah. Pose lompatan: alas sepatu **setidaknya 220 px di atas** tepi bawah (agar bayangan bisa digambar di tanah).
- Semua pose **menghadap kanan**. Cahaya kunci hangat dari **kanan**, cahaya tepi hangat di sisi kanan, isian sejuk dari kiri.
- Wajah kosong tanpa fitur. Kostum kanon Tom (dasi boleh melayang karena gerak).

### Blok bersama (tempel di awal setiap prompt pose)
```
2D anime film illustration, flat cel shading with clean ink lines and subtle paper texture, painterly warm colors, same style and line quality as the reference image tom-stand-new. Faceless character (blank skin-toned face, no eyes, nose or mouth). Outfit identical to the reference: black open zip hoodie over a grey-cream shirt, thin black tie, khaki-olive messenger bag across the body, dark brown trousers, dark sneakers with cream trim, messy dark-brown hair. Light: warm amber key light from the RIGHT, thin warm rim light on right-side edges, soft cool fill from the left, flat 2-tone shadows. Solid pure magenta #FF00FF background, no glow, no shadow, no gradient, crisp clean edges, no white outline. Canvas 1024x1536. Full body, nothing cropped.
```

### P2 — jalan pusat kota Los Angeles, siang hari (plat)
Kanvas 1024×1536, ilustrasi penuh (bukan alpha). **Tanpa orang, tanpa teks, tanpa logo.**
```
2D anime film illustration, flat cel shading, clean ink lines, subtle paper texture, painterly warm colors, vertical 2:3 composition, no people, no readable text or logos.
A downtown Los Angeles street in bright midday sun, seen straight-on at low eye level (camera about 1.2 m high) looking down a wide street with a zebra crosswalk in the foreground. High-rise glass and concrete office towers on both sides receding toward a vanishing point slightly left of center, small shopfronts and awnings at street level, a few palm trees and traffic lights, deep blue sky with a few white clouds. Strong sunlight from the RIGHT casts long clean diagonal building shadows across the asphalt toward the lower left.
The central 60% of the width is clear open street and crosswalk (space for a dancing character); the bottom 35% of the image is plain sunlit asphalt with crosswalk stripes, no objects. Palette: sky blue #6f9bc9 and #a9c6e3, sun yellow #e3a43c, sand #d9c3a0, warm concrete, deep shadow #3f6aa0.
```

### `tom-dance-jump` — lompatan (puncak)
```
[BLOK BERSAMA]
Pose: mid-air joyful jump, three-quarter view facing RIGHT, both knees tucked up, one fist raised high above his head, the other arm swinging back, hoodie flaring open, tie and bag strap flying with the motion, body leaning slightly forward. Shoes are at least 220 px above the bottom of the canvas.
```

### `tom-dance-strut` — langkah percaya diri
```
[BLOK BERSAMA]
Pose: confident strut mid-step, head up, chest out, shoulders back, one arm swinging forward with a relaxed finger point, the other arm swinging back, hoodie open and tie swinging, one foot just lifting off the ground. Facing RIGHT in three-quarter view.
```

### `tom-dance-land` — mendarat, tangan terbuka
```
[BLOK BERSAMA]
Pose: landing from a jump into a low crouch with both arms flung wide open, head thrown back, bag swinging out to the side, knees bent, joyful and unrestrained. Facing RIGHT in three-quarter view. Both shoes touching the ground, about 50 px above the bottom of the canvas.
```

### `tom-dance-point` — menunjuk ke langit (opsional, pose ke-4)
```
[BLOK BERSAMA]
Pose: standing on one leg with the other leg kicked back, one arm pointing straight up toward the sky, the other hand as a fist on his hip, head tilted up. Facing RIGHT in three-quarter view. Standing foot about 50 px above the bottom of the canvas.
```

### Urutan pembuatan yang disarankan
1. Buat dulu **P2** dan **`tom-dance-jump`**. Kirim keduanya, saya cek skala, gaya, dan kecocokan dengan aset adegan 6.
2. Jika cocok, lanjut ke tiga pose lain, kirim bersama.
3. Saya pasang prototipe adegan 5 (Tom menari, bayangan, siluet penari dari kode, burung dari kode) dan kirim hasil render beserta still.

## 4. Gerbang 2 dan 3 (spesifikasi, prompt menyusul setelah Gerbang 1 disetujui)

**Gerbang 2 (adegan 1, 2, 3, 4, 7):**
- **P1** — kamar kerja/kantor beige dengan meja gambar, jendela, kalender dinding; satu plat yang di-grade menjadi kantor siang (adegan 3, 4), kamar malam (adegan 1, 2), dan apartemen Tom (adegan 7). Cahaya dari kanan, lantai terbaca, tanpa orang.
- `tom-desk` (gaya baru, di meja), `tom-draw` (menggambar di meja gambar), `summer-lean` (bersandar di sekat, kostum rok), `rachel` (adik Tom; berdiri dan menyentuh bahu; kostum sesuai referensi lama).

**Gerbang 3 (adegan 4, 8):**
- **P4** — bangku taman di bukit dengan kota jauh, sore tenang. **P5** — lobi biro arsitektur dengan jendela besar berlangit biru, bangku tunggu, maket.
- `tom-sit`, `summer-sit`, `summer-walk`, `autumn-stand` dan `autumn-walk`, `tom-walk` (gaya baru). `mckenzie-cheers` dan `paul-cheers` (gaya baru, bila adegan 4 ikut diperbarui).

Prioritas fallback bila Anda ingin menghemat: aset lama tetap bisa dipakai untuk adegan 4 (kenangan sekilas), tetapi gaya akan terlihat berbeda dari adegan lain.

## 5. Evaluasi (sama dengan adegan 6)

- **Otomatis (hanya yang terukur):** ukuran kanvas, skala relatif Tom, sisa magenta di tepi, kesamaan kamera kiri-kanan (khusus layar terbelah), drift kaki, `check` render, determinisme snapshot, sinkron audio.
- **Manual (wajib):** kualitas ilustrasi 2D, kecocokan gaya antar aset, kesesuaian dengan film, kewajaran gerak, apakah tiap gerakan punya tujuan visual/naratif.
