# Panduan Serah Terima & Pemeliharaan Situs Beasiswa Matahari

Panduan ini disusun untuk memudahkan serah terima (*handover*) proyek situs web Beasiswa Matahari kepada pengelola baru. Dokumen ini dirancang khusus agar mudah dipahami oleh pemula yang baru pertama kali menggunakan **VS Code** atau asisten pengodean berbasis AI seperti **Antigravity**.

---

## 📌 1. Pendahuluan Proyek

Situs **Beasiswa Matahari** adalah situs statis berbasis **HTML, CSS, dan JavaScript**. 
Situs ini **tidak menggunakan build tool** (seperti React, Vue, Next.js, atau Webpack). Artinya:
*   Setiap halaman web adalah file HTML terpisah yang berada di folder utama (contoh: `index.html`, `formulir.html`, dll.).
*   Perubahan pada komponen global (seperti Menu Header atau Footer) harus diterapkan di **setiap file HTML** agar konsisten di seluruh situs.
*   Anda bisa langsung melihat hasil perubahan dengan menyegarkan (*refresh*) browser.

---

## 💻 2. Persiapan Awal (VS Code & Asisten AI)

### Membuka Proyek di VS Code
1. Jalankan aplikasi **VS Code**.
2. Pilih menu **File** > **Open Folder...**
3. Pilih folder proyek `beasiswa-matahari.github.io` yang telah diunduh di komputer Anda.

### Menggunakan Asisten AI (Antigravity / Cursor)
Asisten AI seperti **Antigravity** dapat menuliskan kode untuk Anda secara otomatis. Anda hanya perlu memberikan perintah menggunakan bahasa sehari-hari.

> [!TIP]
> **Cara Terbaik Meminta Bantuan Asisten AI:**
> *   Tekan tombol chat AI di editor Anda.
> *   Sebutkan nama file yang ingin diubah (gunakan simbol `@` diikuti nama file, misalnya `@index.html`).
> *   Berikan instruksi yang spesifik (misal: *"Tolong ubah tanggal batas waktu pendaftaran di formulir.html menjadi 20 Juli 2026"*).

---

## 🚀 3. Cara Menjalankan Situs di Komputer Lokal

Sebelum mempublikasikan perubahan ke internet, Anda harus mengujinya terlebih dahulu di komputer Anda.

1. Buka Terminal di VS Code: klik menu **Terminal** > **New Terminal**.
2. Jalankan perintah berikut untuk memulai server lokal:
   ```bash
   python3 -m http.server 8000 --bind 127.0.0.1
   ```
3. Buka browser Anda (Google Chrome, Firefox, dll.) dan kunjungi alamat:
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
4. Setiap kali Anda mengubah kode dan menyimpan file (`Ctrl + S`), cukup segarkan (*refresh*) halaman browser untuk melihat hasilnya.

---

## ✏️ 4. Panduan Modifikasi Situs (Kasus Umum)

Berikut adalah petunjuk langkah demi langkah untuk melakukan perubahan yang sering dibutuhkan:

### Kasus A: Mengubah Menu Header (Navigasi)

Karena situs ini bersifat statis, menu header ditulis secara manual di bagian atas setiap file HTML.

> [!IMPORTANT]
> Jika Anda mengubah atau menambah menu navigasi di header, Anda **wajib menerapkan perubahan tersebut di 7 file HTML berikut**:
> `index.html`, `formulir.html`, `pengurus.html`, `pencapaian.html`, `testimoni.html`, `donatur-faq.html`, `beswan-faq.html`.

**Cara Melakukannya Secara Manual:**
1. Buka file HTML yang ingin diedit.
2. Cari bagian `<nav class="v2-nav">` di dekat baris ke-15 sampai 35. Strukturnya terlihat seperti ini:
   ```html
   <nav class="v2-nav" aria-label="Navigasi utama">
       <a href="index.html">Homepage</a>
       <a href="formulir.html">Formulir</a>
       ...
   </nav>
   ```
3. Ubah teks di dalam tag `<a>` atau tambahkan baris baru jika ada menu tambahan.

**Cara Meminta Bantuan Asisten AI (Lebih Mudah):**
> *Prompt Chat AI:*
> *"Tolong ubah link menu navigasi di bagian header untuk seluruh file HTML. Saya ingin mengganti teks menu 'Testimoni' menjadi 'Kisah Beswan'."*

---

### Kasus B: Mengubah Formulir & Tanggal Pendaftaran Beswan

Informasi mengenai pendaftaran beswan dikelola di dalam file `formulir.html` dan `index.html`.

**1. Mengubah Tanggal Deadline Pendaftaran:**
*   **Di `formulir.html`:** Cari teks **Deadline dan Tanggal Penting** (sekitar baris ke-65). Ganti tanggal lama dengan tanggal baru di dalam tag `<strong>`.
*   **Di `index.html`:** Cari bagian timeline semester ganjil (sekitar baris ke-125) untuk memperbarui tanggal pengumpulan berkas hingga pengumuman penerima.

**2. Mengganti Link Pendaftaran (Jotform / Google Form):**
*   Tautan form pendaftaran beswan berada di `formulir.html` di dalam kode berikut:
    ```html
    <a href="https://form.jotform.com/233512451226447" class="v2-button primary" target="_blank">Buka Form Beswan</a>
    ```
    Ganti tautan di dalam `href="..."` dengan tautan form pendaftaran yang baru.

**Cara Meminta Bantuan Asisten AI:**
> *Prompt Chat AI:*
> *"Tolong perbarui tanggal deadline pendaftaran beswan di formulir.html dan index.html menjadi 25 Juli 2026. Selain itu, ganti link tombol Jotform beswan di formulir.html menjadi 'https://link-form-baru.com'."*

---

### Kasus C: Mengubah Formulir & Skema Donatur

Informasi donatur berada di bagian bawah `formulir.html` dan pertengahan `index.html`.

1. **Mengubah Paket Donasi (Sun Flare & Sun Spot):**
   Rincian minimal donasi dan durasi tertulis di dalam struktur kartu paket (`package-card`). Buka `index.html` and `formulir.html`, cari teks `Sun Flare` atau `Sun Spot` dan ubah nominalnya sesuai kebijakan terbaru.
2. **Mengubah Link Laporan Keuangan:**
   Di bagian bawah halaman donatur pada `formulir.html`, terdapat tautan Laporan Keuangan:
   ```html
   <p><a href="https://bit.ly/LaporanKeuanganBesMat" target="_blank">Laporan Keuangan</a></p>
   ```
   Ubah nilai `href="..."` tersebut jika tautan Google Drive Laporan Keuangan diperbarui.

---

### Kasus D: Memperbarui Laporan Penyaluran (Pencapaian)

Data laporan penyaluran diinput secara manual dalam bentuk tabel HTML di dalam file `pencapaian.html`.

1. **Mengunggah File PDF Laporan Keuangan Baru:**
   *   Simpan file PDF laporan terbaru Anda di folder `/images/laporan/`.
   *   Buka `pencapaian.html`. Cari baris kode `<iframe>` (sekitar baris ke-70).
   *   Ubah bagian `src="..."` agar mengarah ke nama file PDF baru Anda, contoh:
       ```html
       src="images/laporan/Laporan%20Periode%20XVI%20(Publik).pdf"
       ```
2. **Menambah Tabel Periode Baru:**
   *   Untuk membuat tabel periode baru di atas tabel lama, Anda bisa menyalin salah satu blok kode `<h3>` dan `<table>` di `pencapaian.html` (sekitar baris ke-80), lalu menempelkannya tepat di atasnya.
   *   Ubah data baris `<tr>` dan kolom `<td>` di dalamnya dengan Kode Beswan, Angkatan, Jenis Beasiswa, dan Nominal Penerimaan yang baru.

**Cara Meminta Bantuan Asisten AI:**
> *Prompt Chat AI:*
> *"Tolong bantu saya tambahkan tabel baru untuk 'Periode XVI (Agustus 2026 - Januari 2027)' di bagian atas daftar tabel pada pencapaian.html. Ini adalah data beswannya:
> 1. BM202403, Angkatan 2024, Bantuan UKT, Nominal Rp 3.000.000
> 2. BM202501, Angkatan 2025, Biaya Hidup, Nominal Rp 1.500.000"*

---

## ⬆️ 5. Cara Menyimpan & Mengunggah Perubahan (GitHub)

Setelah Anda memastikan perubahan berjalan dengan baik di server lokal (`http://127.0.0.1:8000/`), Anda harus mempublikasikannya agar situs di internet ikut ter-update. Situs ini di-hosting menggunakan **GitHub Pages**.

---

### 📖 Pengertian Perintah Git Utama

Agar Anda memahami apa yang Anda ketik, berikut adalah pengertian sederhana dari perintah-perintah Git yang akan sering digunakan:

1. **`git status` (Melihat Status Perubahan)**
   *   **Pengertian:** Digunakan untuk melihat daftar file mana saja yang baru ditambahkan, diedit, atau dihapus, namun belum disimpan secara permanen.
   *   **Cara Membaca Hasilnya:** 
       *   File berwarna **merah** (*Changes not staged for commit*): File telah diubah tetapi belum ditandai untuk disimpan.
       *   File berwarna **hijau** (*Changes to be committed*): File sudah ditandai (`git add`) dan siap untuk disimpan.
       *   *nothing to commit, working tree clean*: Menunjukkan tidak ada perubahan baru dibandingkan versi tersimpan sebelumnya.

2. **`git pull` (Menarik Update Terbaru)**
   *   **Pengertian:** Mengunduh (*download*) versi kode terbaru yang ada di internet (GitHub) ke komputer lokal Anda.
   *   **Fungsi:** Menghindari bentrokan kode (*conflict*) jika ada pengelola lain yang memperbarui file sebelum Anda. Selalu jalankan ini di awal sebelum mulai mengedit kode.

3. **`git push` (Mengunggah Perubahan)**
   *   **Pengertian:** Mengunggah (*upload*) semua perubahan kode yang telah Anda simpan di komputer lokal ke server online GitHub.
   *   **Fungsi:** Membuat semua perubahan yang Anda lakukan aktif secara langsung di situs web internet.

---

### 🛠️ Tatacara Alur Kerja Pembaruan Situs

Bagi pemula, ikuti urutan langkah berikut secara disiplin saat melakukan pembaruan situs:

1. **Buka Terminal** di VS Code (menu **Terminal** > **New Terminal**).
2. **Matikan server lokal** jika sedang berjalan dengan menekan tombol **Ctrl + C** di terminal.
3. **Ambil update terbaru** dari GitHub online dengan menjalankan perintah:
   ```bash
   git pull origin main
   ```
4. **Lakukan edit kode** pada file-file HTML yang dibutuhkan, kemudian simpan perubahan dengan menekan **Ctrl + S**.
5. **Periksa file mana saja yang telah berubah** dengan mengetik:
   ```bash
   git status
   ```
   *(Pastikan hanya file yang ingin Anda edit yang terdaftar di terminal)*.
6. **Tandai file untuk disimpan** dengan menjalankan:
   ```bash
   git add .
   ```
   *(Tanda titik `.` menandakan Anda ingin menandai semua file yang telah diubah)*.
7. **Simpan perubahan secara lokal** dengan menyertakan catatan pendek yang jelas:
   ```bash
   git commit -m "update: memperbarui tanggal pendaftaran beswan"
   ```
8. **Unggah perubahan ke internet** agar situs web ter-update:
   ```bash
   git push origin main
   ```
9. Tunggu sekitar 2-5 menit, lalu buka alamat situs Beasiswa Matahari di internet untuk melihat perubahan Anda secara langsung.

---

## 🎓 6. Manfaat & Keterampilan yang Akan Didapat

Mengelola dan memelihara proyek situs web ini akan melatih beberapa keterampilan (*skills*) mendasar yang sangat berguna di bidang teknologi dan manajemen proyek:

1. **Dasar Pemrograman Web & Struktur HTML/CSS**
   *   **Manfaat:** Memahami bagaimana halaman web dirancang secara modular dan visual tanpa menggunakan framework rumit. Pengelola baru akan belajar langsung cara kerja tag HTML (seperti navigasi, tabel, form, dan iframe) serta bagaimana *stylesheet* (CSS) mengontrol tampilan visual situs.
2. **Version Control dengan Git & GitHub Pages**
   *   **Manfaat:** Melatih kemampuan menggunakan Git (`pull`, `status`, `add`, `commit`, `push`) melalui terminal atau antarmuka VS Code. Ini merupakan *core skill* wajib di industri perangkat lunak untuk mengelola versi kode dan mempublikasikan situs via GitHub Pages.
3. **Kolaborasi Berbantuan AI (*AI-Assisted Development*)**
   *   **Manfaat:** Menulis instruksi (*prompt*) yang efektif dan spesifik untuk asisten AI (seperti Antigravity atau Cursor) demi mempercepat pemecahan masalah, penulisan kode, dan pencarian kesalahan (*debugging*).
4. **Manajemen Konten & Pemeliharaan Web**
   *   **Manfaat:** Melatih ketelitian dalam mengelola konten situs web statis multi-halaman agar tetap konsisten (seperti sinkronisasi navigasi header di 7 halaman HTML sekaligus) serta pengelolaan berkas PDF.

---

> [!WARNING]
> **Hal Penting yang Harus Diingat:**
> *   Jangan pernah mengubah struktur nama file HTML (misalnya mengubah `index.html` menjadi `home.html`) karena akan merusak tautan navigasi antar halaman.
> *   Pastikan setiap tautan URL baru selalu diawali dengan `https://`.
