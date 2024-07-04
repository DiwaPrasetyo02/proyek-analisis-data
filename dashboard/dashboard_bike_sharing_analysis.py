import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

# URL file CSV dari dataset
url = 'https://raw.githubusercontent.com/DiwaPrasetyo02/submission-data-analysis/main/day.csv'
df = pd.read_csv(url)

# Mengonversi kolom tanggal
df['dteday'] = pd.to_datetime(df['dteday'])

# Sidebar untuk memilih analisis
analysis_type = st.sidebar.radio("Pilih Jenis Analisis", ('Cuaca', 'Musim'))

# Judul Aplikasi
st.title("Analisis Rental Sepeda berdasarkan Cuaca dan Musim")

if analysis_type == 'Cuaca':
    # Sidebar untuk filter cuaca
    selected_conditions = st.sidebar.multiselect("Pilih Kondisi Cuaca", ['Clear', 'Mist', 'Light Snow', 'Heavy Rain'])

    # Konversi nama cuaca menjadi angka
    weather_condition_map = {'Clear': 1,
                             'Mist': 2,
                             'Light Snow': 3,
                             'Heavy Rain': 4}

    # Filter data berdasarkan kondisi cuaca yang dipilih
    filtered_df = df[df['weathersit'].isin([weather_condition_map[c] for c in selected_conditions])]

    # Analisis Korelasi Cuaca dan Rental Sepeda
    st.header("Analisis Korelasi Cuaca dan Rental Sepeda")

    # Visualisasi jumlah rental sepeda berdasarkan kondisi cuaca
    weather_counts = filtered_df.groupby(['dteday', 'weathersit'])['cnt'].sum().reset_index()
    fig1, ax1 = plt.subplots()
    sns.lineplot(x='dteday', y='cnt', hue='weathersit', data=weather_counts, ax=ax1)
    ax1.set_xlabel("Tanggal")
    ax1.set_ylabel("Jumlah Rental Sepeda")
    ax1.set_title("Jumlah Rental Sepeda berdasarkan Kondisi Cuaca")
    ax1.tick_params(axis='x', rotation=45)
    # Menambahkan interaktivitas
    ax1.format_xdata = mdates.DateFormatter('%Y-%m-%d')
    ax1.format_ydata = lambda x: f'{x:.0f}' 
    ax1.grid(True)

    st.pyplot(fig1)

elif analysis_type == 'Musim':
    # Sidebar untuk filter musim
    selected_seasons = st.sidebar.multiselect("Pilih Musim", ['Spring', 'Summer', 'Fall', 'Winter'])

    # Konversi nama musim menjadi angka
    season_map = {'Spring': 1,
                  'Summer': 2,
                  'Fall': 3,
                  'Winter': 4}

    # Filter data berdasarkan musim yang dipilih
    filtered_df = df[df['season'].isin([season_map[s] for s in selected_seasons])]

    # Analisis Rental Sepeda Musiman
    st.header("Analisis Rental Sepeda Musiman")

    # Visualisasi jumlah rental sepeda berdasarkan musim
    season_counts = filtered_df.groupby(['dteday', 'season'])['cnt'].sum().reset_index()
    fig2, ax2 = plt.subplots()
    sns.lineplot(x='dteday', y='cnt', hue='season', data=season_counts, ax=ax2)
    ax2.set_xlabel("Tanggal")
    ax2.set_ylabel("Jumlah Rental Sepeda")
    ax2.set_title("Jumlah Rental Sepeda berdasarkan Musim")
    ax2.tick_params(axis='x', rotation=45)
    # Menambahkan interaktivitas
    ax2.format_xdata = mdates.DateFormatter('%Y-%m-%d')
    ax2.format_ydata = lambda x: f'{x:.0f}' 
    ax2.grid(True)

    st.pyplot(fig2)
