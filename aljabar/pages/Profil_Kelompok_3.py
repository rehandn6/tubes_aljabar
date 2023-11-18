import streamlit as st
from PIL import Image


st.set_page_config(
    page_title = "Aplikasi Input Output"

)



st.subheader("Aplikasi Penerapan Matriks dengan Analisis Input-Output untuk Memenuhi Tingkat Permintaan ")
st.text("Kelompok 3 Kelas D")
st.write("---")

col1, col2 = st.columns(2)
with col1 :
    st.image('rehand.jpg', width = 300)
with col2 :
    st.header("Rehand Naifisurya Hermansyah")
    st.subheader("227006117")
    st.text("Tugas Individu:   ")
    st.text("- Menentukan Parameter")
    st.text("- Membuat Dataset Dummy")
    st.text("- Membuat Interface")
st.write("---")
col12, col22 = st.columns(2)
with col12 :
    st.image('nada.jpeg', width = 300)
with col22 :
    st.header("Fadli Fajri")
    st.subheader("227006097")
    st.text("Tugas Individu:   ")
    st.text("- Membuat Logika Matriks ")
    st.text("""- Backend Program  
    - Matriks 3x3
    - Matriks 6x6
    - Matriks 9x9
            """)
    
st.write("---")

col13, col23 = st.columns(2)
with col13 :
    st.image('fadli.jpeg', width = 320)
with col23 :
    st.header("Qathrun Nada Annaqiya")
    st.subheader("227006100")
    st.text("Tugas Individu:   ")
    st.text("- Riset Jurnal")
    st.text("- Perhitungan Manual")
    st.text("- Perhitungan pada Excel")
