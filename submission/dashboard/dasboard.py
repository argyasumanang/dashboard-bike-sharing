import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Aplikasi
st.title("Dashboard Analisis Data Bike Sharing")

# Menampilkan informasi tentang aplikasi
st.write("Selamat datang di aplikasi analisis data bike sharing.")

# Membaca data
uploaded_file = st.file_uploader("Upload file CSV", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    
    # Menampilkan data
    st.write("Beberapa baris data:")
    st.write(data.head())

    # Visualisasi 1: Total Pengguna Sepeda per Musim
    st.subheader("Total Pengguna Sepeda per Musim")
    musim_dict = {1: 'Musim Semi', 2: 'Musim Panas', 3: 'Musim Gugur', 4: 'Musim Dingin'}
    data['musim_label'] = data['season'].map(musim_dict)
    season_usage = data.groupby('musim_label')['cnt'].sum()

    # Membuat visualisasi bar chart
    plt.figure(figsize=(8, 5))
    sns.barplot(x=season_usage.index, y=season_usage.values, palette=['#87CEFA', '#90EE90', '#FF6347', '#FFD700'])
    plt.title("Total Pengguna Sepeda per Musim")
    plt.xlabel("Musim")
    plt.ylabel("Total Pengguna Sepeda")
    st.pyplot(plt)  # Menampilkan chart di streamlit

    # Visualisasi 2: Total Pengguna Sepeda per Kondisi Cuaca
    st.subheader("Total Pengguna Sepeda per Kondisi Cuaca")
    cuaca_dict = {1: 'Clear/Partly Cloudy', 2: 'Mist/Cloudy', 3: 'Light Snow/Rain', 4: 'Heavy Rain/Snow'}
    data['cuaca_label'] = data['weathersit'].map(cuaca_dict)
    weather_usage = data.groupby('cuaca_label')['cnt'].sum()

    # Memastikan semua kategori cuaca muncul, bahkan jika tidak ada datanya
    weather_usage = weather_usage.reindex(cuaca_dict.values(), fill_value=0)

    # Membuat visualisasi bar chart
    plt.figure(figsize=(8, 5))
    sns.barplot(x=weather_usage.index, y=weather_usage.values, palette=['#20B2AA', '#FFA07A', '#6495ED', '#B0C4DE'])
    plt.title("Total Pengguna Sepeda per Kondisi Cuaca")
    plt.xlabel("Kondisi Cuaca")
    plt.ylabel("Total Pengguna Sepeda")
    st.pyplot(plt)








    

