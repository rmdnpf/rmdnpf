# Daftar aset gambar — (500) Days of Summer (14 gambar, disiapkan pengguna)

Status: **14 gambar sudah diterima** (di `assets/figures/src/`), dipakai apa adanya (anime berwarna penuh, wajah kosong). Lihat `ART_STYLE.md`.
Hasil potong latar putih: `assets/figures/*.png` (dibuat oleh `scripts/prep_figures.py`).

Masih perlu perhatian:
- `rachel-point.png` berlatar hitam + glow, belum bisa dipotong bersih. Sementara Frame 7 memakai `rachel-pat`; jika ingin pose menunjuk, perlu versi latar putih.
- `summer-stand.png` setengah badan; dipakai sebagai potret kecil di Frame 4.

## Jumlah per karakter

| Karakter | Pose | Keputusan |
|---|---|---|
| Tom | 5 | stand, desk, dance, sit, walk |
| Summer | 4 | stand, lean, twirl, walk |
| Rachel | 2 | pat, point |
| McKenzie | 1 | cheers |
| Paul | 1 | cheers |
| Autumn | 1 | walk |
| **Total** | **14** | |

## Daftar file

| File | Frame | Pose |
|---|---|---|
| `tom-stand.png` | F4 | Berdiri, tangan di saku (seperti referensi), versi latar putih |
| `tom-desk.png` | F3 | Duduk di meja kerja kecil, menulis di kartu ucapan, kartu bertebaran |
| `tom-dance.png` | F5 | Melompat gembira, satu tangan terangkat |
| `tom-sit.png` | F5, F8 | Duduk sendirian di bangku, bahu turun, kepala menunduk |
| `tom-walk.png` | F6 | Berjalan, dilihat dari samping atau belakang |
| `summer-stand.png` | F4 | Berdiri menoleh ke samping (seperti referensi), versi latar putih |
| `summer-lean.png` | F3 | Bersandar ke dinding, tangan di belakang, menoleh santai |
| `summer-twirl.png` | F5 | Berputar, rok mengembang |
| `summer-walk.png` | F6 | Berjalan, dilihat dari samping atau belakang, serasi dengan `tom-walk` |
| `rachel-pat.png` | F5 | Remaja perempuan (lebih pendek dari Tom), rambut diikat, satu tangan terangkat seperti menepuk bahu, tampak samping |
| `rachel-point.png` | F7 | Berdiri, satu tangan menunjuk ke samping |
| `mckenzie-cheers.png` | F4 | Pria berbadan tinggi berjaket, bersandar santai, mengangkat gelas |
| `paul-cheers.png` | F4 | Pria berkemeja dan rompi rajut, bersandar santai, mengangkat gelas |
| `autumn-walk.png` | F8 | Berjalan masuk dari samping, mantel/gaun oranye hangat, rambut sebahu, tas bahu |

Catatan siluet (warna akhir ditentukan saat pewarnaan ulang, bukan di gambar sumber): pendukung tampil hanya 2 sampai 3 detik, jadi bentuknya harus mudah dibedakan (McKenzie tinggi dan berjaket, Paul berompi rajut,
Rachel lebih pendek berambut diikat, Autumn berwarna oranye hangat, berbeda jelas dari biru Summer).

## VO
8 file di `assets/vo/01.wav … 08.wav` dari `VO_SCRIPT.md` (Cartesia, bahasa `id`, satu suara hangat dan santai).
