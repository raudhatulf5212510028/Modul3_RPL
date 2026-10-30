# Sistem Perpustakaan - Aplikasi Manajemen Buku & Autentikasi

Aplikasi desktop berbasis Python yang dirancang menggunakan pendekatan arsitektur **Model-View-Controller (MVC)** dan pustaka antarmuka grafis **CustomTkinter**, serta terintegrasi dengan basis data **MySQL**.

---

## 📂 Struktur Direktori MVC

Proyek ini diorganisasikan menggunakan struktur direktori berbasis MVC untuk memisahkan logika data, antarmuka, dan pengontrol sistem:

```text
Modul3_RPL/
├── .github/
│   └── workflows/
│       └── ci_pipeline.yml   # Konfigurasi GitHub Actions CI/CD
├── config/
│   └── database.py           # Konfigurasi koneksi database MySQL
├── controllers/
│   └── auth_controller.py    # Logika pengontrol autentikasi & buku
├── models/
│   ├── buku_model.py         # Model manajemen data buku
│   └── user_model.py         # Model manajemen pengguna & login
├── views/
│   └── login_view.py         # Antarmuka grafis (GUI) login aplikasi
├── tests/
│   ├── test_model.py         # Skrip unit testing model
│   └── test_user.py          # Skrip unit testing autentikasi
├── requirements.txt          # Daftar pustaka dependensi proyek
└── README.md                 # Dokumentasi proyek
```
