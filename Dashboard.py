import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Judul Aplikasi
st.title("Bike sharing dataset")
st.write("Hal ini untuk menganalisis pengaruh suhu terhadap jumlah total sewa sepeda pada hari kerja dan hari libur.")
st.write("Nama: Amalia Putri")
st.write("Email: m384b4kx0446@bangkit.academy")
st.write("ID Dicoding: aleailearn")

# Memuat Data
data = pd.read_csv(r'C:\Users\amali\Downloads\Bike sharing dataset - proyek\day.csv')

# Menambahkan kolom baru untuk membedakan hari kerja dan akhir pekan
data['is_weekend'] = data['weekday'].apply(lambda x: 1 if x >= 5 else 0)

# Memeriksa data
if data.empty:
    st.error("Data tidak ditemukan atau kosong.")
else:

    st.header("Pertanyaan 1")
    st.write("""
   "Bagaimana pengaruh suhu (temp) terhadap jumlah total sewa (cnt) pada hari kerja dibandingkan dengan hari libur?
    """)

    # Pertanyaan 1: Pengaruh Suhu terhadap Jumlah Sewa
    st.header("Analisis Pengaruh Suhu Terhadap Jumlah Sewa")
    avg_sewa = data.groupby(['holiday'])[['cnt', 'temp']].mean().reset_index()

    # Visualisasi
    plt.figure(figsize=(10, 5))
    sns.barplot(data=avg_sewa, x='holiday', y='cnt', palette='viridis')
    plt.title('Rata-rata Jumlah Sewa berdasarkan Hari (Kerja vs Libur)')
    plt.xlabel('Hari (0 = Hari Kerja, 1 = Hari Libur)')
    plt.ylabel('Rata-rata Jumlah Sewa')
    st.pyplot(plt)

    # Tampilkan Statistik Deskriptif
    st.subheader("Statistik Deskriptif:")
    st.write(data.describe())

    # Analisis Distribusi Jumlah Sewa
    st.header("Analisis Distribusi Jumlah Sewa")
    plt.figure(figsize=(10, 6))
    sns.histplot(data['cnt'], bins=30, kde=True)
    plt.title('Distribusi Jumlah Sewa (cnt)')
    plt.xlabel('Jumlah Sewa')
    plt.ylabel('Frekuensi')
    st.pyplot(plt)

    # Hubungan antara suhu dan jumlah sewa
    st.header("Hubungan Suhu dan Jumlah Sewa")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='temp', y='cnt', hue='workingday', data=data, alpha=0.7)
    plt.title('Hubungan Suhu (temp) dan Jumlah Sewa (cnt)')
    plt.xlabel('Suhu (temp)')
    plt.ylabel('Jumlah Sewa (cnt)')
    plt.legend(title='Hari Kerja')
    st.pyplot(plt)

    # Analisis Jumlah Sewa berdasarkan Suhu
    st.header("Analisis Jumlah Sewa berdasarkan Suhu")
    avg_sewa = data.groupby(['is_weekend', 'temp'])['cnt'].mean().reset_index()

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=avg_sewa, x='temp', y='cnt', hue='is_weekend', marker='o')
    plt.title('Rata-rata Jumlah Sewa berdasarkan Suhu')
    plt.xlabel('Suhu (temp)')
    plt.ylabel('Rata-rata Jumlah Sewa (cnt)')
    plt.xticks(rotation=45)
    plt.legend(title='Hari', labels=['Hari Kerja', 'Akhir Pekan'])
    st.pyplot(plt)

    #Analisis pertanyaan 2
    st.header("Pertanyaan 2")
    st.write("""
   "Ide desain atau fitur seperti apa yang perlu diterapkan pada aplikasi untuk meningkatkan jumlah pengguna pada hari kerja yang memiliki cuaca buruk?
    """)
    
    # Analisis Cuaca Buruk
    st.header("Analisis Jumlah Sewa pada Hari Kerja Berdasarkan Cuaca")
    weather_analysis = data[data['workingday'] == 1].groupby('weathersit')['cnt'].mean().reset_index()

    plt.figure(figsize=(8, 6))
    sns.barplot(data=weather_analysis, x='weathersit', y='cnt')
    plt.title('Rata-rata Jumlah Sewa pada Hari Kerja Berdasarkan Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Rata-rata Jumlah Sewa (cnt)')
    plt.xticks(ticks=[0, 1, 2], labels=['Cerah', 'Sedang', 'Buruk'], rotation=0)
    st.pyplot(plt)


    # Rekomendasi Fitur
    st.header("Rekomendasi Fitur untuk Meningkatkan Pengguna pada Hari Kerja")
    st.write("""
    - **Penawaran Khusus**: Diskon atau promo untuk sewa sepeda saat cuaca buruk.
    - **Peringatan Cuaca**: Notifikasi yang memberi tahu pengguna tentang cuaca dan saran untuk menggunakan sepeda.
    - **Rekomendasi Rute**: Rute yang lebih aman atau lebih tertutup dari cuaca buruk.
    """)


