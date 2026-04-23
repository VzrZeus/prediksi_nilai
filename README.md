# 🎓 AI Grade Prediction System

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Sistem cerdas berbasis web yang dirancang untuk membantu mahasiswa memprediksi **Grade Nilai Akhir** (A-E) secara akurat. Aplikasi ini tidak hanya menghitung, tetapi juga memberikan analisis strategi untuk mencapai target nilai tertentu.

---

## 🚀 Fitur Unggulan

* **Smart Calculation:** Menghitung nilai berdasarkan bobot standar akademik.
* **Target Analysis:** Memberitahu Anda skor minimum UAS yang dibutuhkan untuk mendapatkan Grade A.
* **Interactive UI:** Dilengkapi dengan slider dan animasi piala (Lottie) untuk user experience yang lebih baik.
* **Visualisasi Grafik:** Distribusi nilai ditampilkan dalam bentuk chart untuk analisis kontribusi tiap komponen.
* **Attendance Alert:** Peringatan otomatis jika kehadiran berada di bawah batas aman (75%).

---

## 🛠️ Instalasi & Persiapan

Ikuti langkah-langkah berikut untuk menjalankan aplikasi di perangkat lokal Anda:


1.  **Instal Library yang Dibutuhkan:**
    ```bash
    pip install streamlit pandas streamlit-lottie requests
    ```

2.  **Jalankan Aplikasi:**
    ```bash
    streamlit run app.py
    ```

---

## 📊 Bobot Penilaian & Grade

Aplikasi ini menggunakan standar penilaian perguruan tinggi sebagai berikut:

### Komponen Penilaian
| Komponen | Bobot | Deskripsi |
| :--- | :--- | :--- |
| **Tugas** | 20% | Rata-rata nilai harian |
| **Absensi** | 10% | Persentase kehadiran |
| **UTS** | 30% | Ujian Tengah Semester |
| **UAS** | 40% | Ujian Akhir Semester |

### Klasifikasi Grade
* **A**: ≥ 85 (Sangat Memuaskan)
* **B**: 75 - 84 (Baik)
* **C**: 60 - 74 (Cukup)
* **D**: 45 - 59 (Remidi)
* **E**: < 45 (Gagal)

---

## 📸 Preview Tampilan
*(Tips: Tambahkan screenshot aplikasi Anda di sini untuk tampilan yang lebih menarik)*

> **Note:** Proyek ini menggunakan **Lottie Animation** untuk efek piala emas saat mahasiswa diprediksi mendapatkan Grade A.

---

## 👤 Developer
* **Nama:** Fajar
* **Institusi:** STMIK AMIKOM Surakarta
* **Program Studi:** Informatika
* **GitHub:** [@VzrZeus](https://github.com/VzrZeus)

---
*Dibuat untuk pemenuhan tugas mata kuliah **Sistem Cerdas**. © 2026*