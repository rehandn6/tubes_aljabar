import streamlit as st
from PIL import Image


st.set_page_config(
    page_title = "Aplikasi Input Output"

)

st.header("Cara Penggunaan ")

st.subheader("Analisis Input Output ")

st.write("""Analisis Input-Ouput (I-O) adalah suatu model matematis untuk menganalisis keterkaitan antar 
sektor dalam suatu perekonomian.
Tujuan aplikasi ini untuk menghitung permintaan akhir agar dapat terpenuhi berdasarkan sektor-sektor yang telah ditentukan maka harus memproduksi barang/ output berturut-turut senilai berapa rupiah.""")

st.subheader("Matriks Koefisien Teknis ")
st.write("""Matriks ini berasal dari perhitungan setelah dibuatnya matriks transaksi yang merupakan dasar statistik dari sistem input output 
dalam suatu perekonomian, maka langkah selanjutnya adalah membuat "matriks koefisien teknis, 
atau matriks koefisien input.""")

st.image('koef.png')
st.write("Cara penggunaan pada aplikasi : ")
st.write("1. Masukan nilai sesuai matriks nya.")
st.write(" Contohnya apabila ingin menginput sesuai dataset dengan ukuran 3x3 (3 sektor) ")
st.write("  - pada bagian baris 1 input 0.1468 0.2346	0.1417")
st.write("  - pada bagian baris 2 input 0.0896 0.2658	0.2077")
st.write("  - pada bagian baris 3 input 0.2568 0.1299	0.1684")
st.write("2. Masukan Permintaan Akhir.")
st.write("3. Lihat bagian hasil dari perhitungan.")



st.subheader(" Kalkulator Matriks Transaksi ")
st.write("""Tabel dasar dari sistem input-output dikenal dengan sebutan sebagai matriks transaksi, di 
mana nilai dari data yang dimasukan ke dalam matriks transaksi adalah berupa satuan nilai dari 
berbagai arus ekonomi yang ada dalam suatu perekonomian selama periode tahun dasar tertentu.""")

st.image('transaksi.png')
st.write("Cara penggunaan pada aplikasi : ")
st.write("1. Masukan nilai sesuai matriks nya.")
st.write(" Contohnya apabila ingin menginput sesuai dataset dengan ukuran 3x3 (3 sektor) ")
st.write("  - pada bagian baris 1 input 2593, 3593, 2090 ")
st.write("  - pada bagian baris 2 input 1583, 4072, 3064 ")
st.write("  - pada bagian baris 3 input 4536, 1990, 2485 ")
st.write("2. Masukan Permintaan Akhir.")
st.write("3. Matriks Koefisien akan muncul dan input kembali setiap nilainya.")
st.write("4. Lihat bagian hasil dari perhitungan.")
