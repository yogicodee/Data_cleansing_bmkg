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