# Tugas-Analisis-Data
Ini Merupakan Tugas Submission Analisis Data. Cara menjalankan yang berisi cara menjalankan dashboard

## Setup Environment - Anaconda
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt

## Setup Environment - Shell/Terminal
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
NB: Nama proyek bisa di sesuaikan 

## Run steamlit app
streamlit run dashboard.py
