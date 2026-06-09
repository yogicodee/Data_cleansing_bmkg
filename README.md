# Data Cleansing BMKG

Script Python ini berfungsi untuk membersihkan, merapikan, dan memproses dataset mentah dari BMKG (Badan Meteorologi, Klimatologi, dan Geofisika) agar siap digunakan untuk analisis lebih lanjut.

## **Fitur Utama**

*   **Pembersihan Duplikasi:** Otomatis mendeteksi dan menghapus baris data yang berulang (duplicate data).
*   **Penanganan Data Kosong:** Menghapus atau mengisi (imputasi) kolom yang memiliki nilai kosong (missing values).
*   **Standardisasi Data:** Menyesuaikan dan memperbaiki format data yang tidak sesuai (misalnya kesalahan pengetikan atau anomali nilai).
*   **Ekspor Otomatis ke Lokal:** Mengunduh dan menyimpan hasil pembersihan data secara otomatis ke penyimpanan lokal (misalnya dalam format `.csv`).

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue">
  <img src="https://img.shields.io/badge/Pandas-Data%20Processing-green">
  <img src="https://img.shields.io/badge/BMKG-Dataset-orange">
</p>

<h1 align="center">🌦️ Data Cleansing BMKG</h1>

<p align="center">
Python-based data cleansing pipeline for BMKG weather datasets.
</p>

## 📊 Sample Dataset

### Before Cleaning
| Tanggal | Suhu | Curah Hujan |
|----------|------|-------------|
| 2024-01-01 | 32 | NaN |
| 2024-01-01 | 32 | NaN |
| NULL | 30 | 5 |

### After Cleaning
| Tanggal | Suhu | Curah Hujan |
|----------|------|-------------|
| 2024-01-01 | 32 | 0 |
| 2024-01-02 | 30 | 5 |

## 🔄 Workflow
Raw Dataset
      ↓
Duplicate Removal
      ↓
Missing Value Handling
      ↓
Data Standardization
      ↓
Clean Dataset
      ↓
Export CSV
