# Struktur Halaman dan Sistem Desain

## Ringkasan Fitur

Fokus fitur ini adalah pengalaman membaca yang lebih bersih dan navigasi yang lebih jelas untuk website Beasiswa Matahari.

### User Stories

1. Sebagai pengunjung baru, saya ingin langsung memahami tujuan Beasiswa Matahari, supaya saya cepat tahu konteks websitenya.
2. Sebagai calon beswan, saya ingin menemukan formulir dan timeline pendaftaran dengan cepat, supaya saya tidak perlu mencari-cari.
3. Sebagai calon donatur, saya ingin melihat opsi donasi dan FAQ, supaya saya bisa mengambil keputusan tanpa bingung.
4. Sebagai pembaca, saya ingin layout halaman konsisten, supaya konten terasa rapi dan mudah diikuti.

## Peta Halaman

| Halaman | Fungsi | Catatan Tampilan |
| --- | --- | --- |
| `index.html` | Landing page utama | Perlu hero yang jelas, CTA, dan section cards. |
| `formulir.html` | Akses formulir | Perlu callout deadline dan daftar berkas yang dibutuhkan. |
| `pengurus.html` | Daftar pengurus | Perlu grid card yang rapi dan ringkas. |
| `pencapaian.html` | Laporan penyaluran dana | Perlu pemisahan yang jelas antara ringkasan dan tabel data. |
| `testimoni.html` | Testimoni dosen | Perlu layout yang lebih mudah dipindai. |
| `donatur-faq.html` | FAQ donatur | Perlu question-answer blocks yang tegas. |
| `beswan-faq.html` | FAQ beswan | Perlu question-answer blocks yang tegas. |

## Sistem Desain

### Warna

- Accent utama: nuansa amber / gold.
- Surface: putih hangat.
- Background: gradasi lembut, bukan flat putih polos.

### Tipografi

- Heading harus terasa tegas dan terstruktur.
- Body text dijaga nyaman dibaca di ukuran kecil.

### Komponen

- Hero card untuk halaman utama.
- Content card untuk halaman konten.
- Button CTA untuk aksi utama.
- Card grid untuk daftar artikel, pengurus, dan highlight.
- Table wrapper untuk data laporan.

## Aturan Konten

1. Gunakan heading secara berurutan dan hindari markup yang rusak.
2. Gunakan paragraf pendek agar mudah dipindai.
3. Link penting harus terlihat sebagai aksi utama, bukan teks biasa.
4. Gambar harus punya `alt` yang informatif.

## Implementasi yang Diinginkan

- CSS global menangani layout, warna, kartu, dan responsivitas.
- HTML tiap halaman hanya perlu menambahkan wrapper yang konsisten.
- Sidebar tetap dipakai, tetapi tampil lebih rapi dan tidak terlalu dominan.
