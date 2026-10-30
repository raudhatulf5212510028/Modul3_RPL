# APLIKASI PERPUSTAKAAN

## 1. Deskripsi Singkat Aplikasi

Aplikasi Perpustakaan merupakan aplikasi berbasis desktop yang dikembangkan menggunakan bahasa pemrograman Python dengan menerapkan arsitektur Model-View-Controller (MVC). Aplikasi ini dibuat untuk membantu proses pengelolaan data perpustakaan, seperti data buku, data anggota, serta proses peminjaman dan pengembalian buku.

Aplikasi ini menggunakan CustomTkinter sebagai antarmuka pengguna (_User Interface_) dan MySQL sebagai sistem manajemen basis data. Selain itu, aplikasi dilengkapi dengan fitur login yang membedakan hak akses antara admin dan anggota sehingga setiap pengguna dapat mengakses fitur sesuai dengan perannya.

## 2. Struktur Direktori MVC

Aplikasi ini menggunakan pola arsitektur Model-View-Controller (MVC) untuk memisahkan bagian pengelolaan data, tampilan, dan logika aplikasi.

Berikut struktur direktori proyek:

```text
Modul3/
│
├── models/
│   ├── __init__.py
│   ├── buku_model.py
│   ├── anggota_model.py
│   ├── peminjaman_model.py
│   └── pengembalian_model.py
│
├── views/
│   ├── __init__.py
│   ├── buku_view.py
│   ├── anggota_view.py
│   ├── peminjaman_view.py
│   └── pengembalian_view.py
│
├── controllers/
│   ├── __init__.py
│   ├── buku_controller.py
│   ├── anggota_controller.py
│   ├── peminjaman_controller.py
│   └── pengembalian_controller.py
│
├── main.py
├── requirements.txt
└── README.md
```

**Penjelasan direktori:**

- **models/**: Berisi kode untuk mengelola data dan berinteraksi dengan database MySQL.
- **views/**: Berisi kode untuk membuat tampilan aplikasi menggunakan CustomTkinter.
- **controllers/**: Berisi logika aplikasi yang menghubungkan Model dan View serta mengatur proses CRUD (Create, Read, Update, Delete).
- **main.py**: File utama untuk menjalankan aplikasi.
- **requirements.txt**: Berisi daftar pustaka Python yang dibutuhkan aplikasi.
- **README.md**: Berisi dokumentasi aplikasi, panduan instalasi, konfigurasi, dan cara menjalankan aplikasi.

## 3. Panduan Instalasi dan Konfigurasi Database MySQL

### A. Persiapan

Sebelum menjalankan aplikasi, pastikan perangkat telah memiliki beberapa perangkat lunak berikut:

1. Python versi 3.x.
2. MySQL atau Laragon sebagai server database.
3. Visual Studio Code sebagai editor kode.
4. Git untuk pengelolaan repositori (opsional).

### B. Clone Repository

Unduh proyek dari repository GitHub menggunakan perintah berikut:

```bash
git clone https://github.com/username/nama-repository.git
```

Masuk ke direktori proyek:

```bash
cd Modul3
```

### C. Membuat Virtual Environment

Buat lingkungan virtual Python dengan perintah:

```bash
python -m venv env
```

Aktifkan virtual environment pada Windows:

```bash
env\Scripts\activate
```

### D. Instalasi Dependencies

Instal seluruh pustaka yang dibutuhkan aplikasi menggunakan perintah:

```bash
pip install -r requirements.txt
```

### E. Konfigurasi Database MySQL

1. Jalankan server MySQL melalui Laragon atau XAMPP.
2. Buka phpMyAdmin melalui browser.
3. Buat database dengan nama `perpustakaan`.
4. Buat tabel-tabel yang diperlukan, seperti `buku`, `anggota`
5. Sesuaikan konfigurasi koneksi database pada file koneksi yang digunakan dalam direktori proyek.

Contoh konfigurasi koneksi database:

```python
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="perpustakaan"
)
```

**Catatan:** Sesuaikan konfigurasi host, username, dan password dengan pengaturan MySQL pada perangkat masing-masing.

## 4. Cara Menjalankan Aplikasi

Setelah proses instalasi dan konfigurasi database selesai, ikuti langkah berikut:

1. Pastikan server MySQL sudah berjalan.
2. Buka terminal pada direktori proyek.
3. Aktifkan virtual environment:

```bash
env\Scripts\activate
```

4. Jalankan aplikasi menggunakan perintah:

```bash
python main.py
```

5. Setelah aplikasi berhasil dijalankan, halaman login akan ditampilkan.
6. Masukkan username dan password yang telah terdaftar pada database.
7. Pengguna akan diarahkan ke halaman aplikasi sesuai dengan hak akses masing-masing, yaitu admin atau anggota.

## 5. Fitur Aplikasi

Aplikasi Perpustakaan memiliki beberapa fitur utama, yaitu:

- Login dan autentikasi pengguna.
- Pengelolaan data buku.
- Pengelolaan data anggota.
- Pengelolaan data peminjaman buku.
- Pengelolaan data pengembalian buku.
- Pembagian hak akses berdasarkan role admin dan anggota.

## 6. Teknologi yang Digunakan

| Teknologi              | Keterangan                        |
| ---------------------- | --------------------------------- |
| Python                 | Bahasa pemrograman                |
| CustomTkinter          | Pembuatan antarmuka aplikasi      |
| MySQL                  | Sistem manajemen database         |
| mysql-connector-python | Menghubungkan Python dengan MySQL |
| Pytest                 | Pengujian aplikasi                |
| Git & GitHub           | Pengelolaan versi kode            |

---

**Dikembangkan untuk memenuhi tugas praktikum Rekayasa Perangkat Lunak (RPL).**
