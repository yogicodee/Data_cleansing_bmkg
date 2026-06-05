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