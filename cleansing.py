import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

# 1. Load Data (Gunakan pemisah titik koma sesuai format asli)
df = pd.read_csv("DATA AWS TANGSEL 21-25.csv", sep=";")

# 2. Konversi kolom tgl_data menjadi format Waktu (Datetime)
df['tgl_data'] = pd.to_datetime(df['tgl_data'], errors='coerce', format='mixed')

# 3. Paksa kolom yang error menjadi numerik (yang rusak otomatis jadi kosong/NaN)
kolom_bermasalah = ['rr', 'tt_air_max', 'rh_avg']
for col in kolom_bermasalah:
    df[col] = pd.to_numeric(df[col], errors='coerce')

print("Tahap 1 Selesai. Dimensi Data:", df.shape)
==========================================================================
# 1. Filter semua baris yang memiliki minimal 1 nilai kosong
df_kosong = df[df.isnull().any(axis=1)].copy()

# 2. Ekstraksi Tahun, Tanggal, dan Jam untuk pencatatan
df_kosong['Tahun'] = df_kosong['tgl_data'].dt.year
df_kosong['Tanggal'] = df_kosong['tgl_data'].dt.date
df_kosong['Jam'] = df_kosong['tgl_data'].dt.time

# 3. Sortir berdasarkan waktu agar mudah melihat dari jam berapa sampai jam berapa
df_kosong = df_kosong.sort_values(by='tgl_data')

# 4. Simpan ke dalam CSV baru sebagai bukti/laporan
kolom_laporan = ['tgl_data','rr']
df_kosong[kolom_laporan].to_csv("Log_Data_Kosong_Tercatat_kondisi_1.csv", index=False)

print(f"Laporan berhasil dibuat! Ada {len(df_kosong)} baris data kosong yang telah dicatat di 'Log_Data_Kosong_Tercatat_kondisi_1.csv'")
================================================================================================================================================
# 1. Pengecekan dan Penghapusan Data Duplikat
jumlah_duplikat = df.duplicated().sum()
df = df.drop_duplicates()
print(f"Ditemukan dan dihapus {jumlah_duplikat} baris data duplikat.")

# 2. Pemusnahan Data Kosong (Sesuai instruksi)
df_bersih = df.dropna().copy()
print(f"Sisa data setelah cleansing mutlak: {len(df_bersih)} baris.")
=============================================================================================
# 1. Isolasi semua baris yang Hujan (rr)-nya kosong
df_kosong = df[df['Hujan (rr)'].isnull()].copy()

# 2. Ekstraksi Tahun, Tanggal, dan Jam untuk pencatatan riwayat
df_kosong['Tahun'] = df_kosong['tgl_data'].dt.year
df_kosong['Tanggal'] = df_kosong['tgl_data'].dt.date
df_kosong['Jam'] = df_kosong['tgl_data'].dt.time

# 3. Sortir kronologis dari jam ke jam
df_kosong = df_kosong.sort_values(by='tgl_data')

# 4. Simpan ke dalam CSV baru sebagai bukti/laporan
df_kosong.to_csv("Log_Data_Hujan_Kosong.csv", index=False)

print(f"Laporan berhasil dibuat! {len(df_kosong)} baris data kosong telah direkam ke 'Log_Data_Hujan_Kosong.csv'")
==================================================================================================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Data Revisi (Gunakan pemisah titik koma)
df = pd.read_csv("DATA AWS TANGSEL 21-25.csv", sep=";")

# 2. Konversi kolom tgl_data menjadi format Waktu (Datetime)
df['tgl_data'] = pd.to_datetime(df['tgl_data'])

# 3. Paksa kolom Hujan menjadi numerik (data teks yang rusak akan menjadi kosong/NaN)
df['Hujan (rr)'] = pd.to_numeric(df['Hujan (rr)'], errors='coerce')

print("Tahap 1 Selesai. Dim, df.shape)
===============================================================================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files  # Modul wajib untuk fitur download di Google Colab

# 1. Load Data Revisi (Gunakan pemisah titik koma)
df = pd.read_csv("DATA AWS TANGSEL 21-25.csv", sep=";")