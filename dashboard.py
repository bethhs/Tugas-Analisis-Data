import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Data Contoh
data_day = {
    'temp': [0.24, 0.22, 0.22, 0.24, 0.24],
    'hum': [0.81, 0.80, 0.80, 0.75, 0.75],
    'windspeed': [0.0, 0.0, 0.0, 0.0, 0.0],
    'cnt': [16, 40, 32, 13, 1]
}
df_day = pd.DataFrame(data_day)

data_hour = {
    'temp': [0.24, 0.22, 0.22, 0.24, 0.24],
    'hum': [0.81, 0.80, 0.80, 0.75, 0.75],
    'windspeed': [0.0, 0.0, 0.0, 0.0, 0.0],
    'cnt': [16, 40, 32, 13, 1]
}
df_hour = pd.DataFrame(data_hour)

# Fungsi untuk membuat dan menampilkan subplot
def create_plots(data_day, data_hour, data):
    plt.figure(figsize=(12, 8))

    # Subplot 1: Suhu vs Jumlah Pengguna (Day)
    plt.subplot(2, 2, 1)
    sns.scatterplot(x='temp', y='cnt', data=data_day)
    plt.title('Suhu vs Jumlah Pengguna (Day)')

    # Subplot 2: Suhu vs Jumlah Pengguna (Hour)
    plt.subplot(2, 2, 2)
    sns.scatterplot(x='temp', y='cnt', data=data_hour)
    plt.title('Suhu vs Jumlah Pengguna (Hour)')

    # Subplot 3: Kelembapan vs Jumlah Pengguna (Day)
    plt.subplot(2, 2, 3)
    sns.scatterplot(x='hum', y='cnt', data=data_day)
    plt.title('Kelembapan vs Jumlah Pengguna (Day)')

    # Subplot 4: Kelembapan vs Jumlah Pengguna (Hour)
    plt.subplot(2, 2, 4)
    sns.scatterplot(x='hum', y='cnt', data=data_hour)
    plt.title('Kelembapan vs Jumlah Pengguna (Hour)')

    plt.tight_layout()

    return plt

# Streamlit app
st.title('Visualisasi Data Suhu dan Kelembapan')

# Menampilkan data yang diunggah
st.write("Data Harian:", df_day)
st.write("Data Per Jam:", df_hour)

# Contoh data yang dibersihkan
all_df = pd.concat([df_day, df_hour], ignore_index=True)

# Buat dan tampilkan plot
fig = create_plots(df_day, df_hour, df_day)  # Misalnya df_day digunakan untuk data
st.pyplot(fig)

# Simpan data yang telah dibersihkan
cleaned_data_file = "all_data.csv"
all_df.to_csv(cleaned_data_file, index=False)
st.write(f"Data yang telah dibersihkan disimpan di: {cleaned_data_file}")
