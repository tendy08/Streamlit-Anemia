import pickle 
import numpy as np
import streamlit as st

#load save model
model = pickle.load(open('anemia.sav', 'rb'))

#judul web
st.title('Prediksi Penyakit Anemia')

Gender = st.number_input('Jenis Kelamin (0 = Laki-laki, 1 = Perempuan)')

col1, col2 = st.columns(2)

with col1 :
    Hemoglobin = st.number_input('Hemoglobin (hb)')
with col2 : 
    MCH = st.number_input('MCH')
with col1 :
    MCHC = st.number_input('MCHC')
with col2:
    MVC = st.number_input('MVC')

#predic
Result = ''

#tombol
if st.button('Prediksi Penyakit Anemia') :
    Result = model.predict([[Gender, Hemoglobin, MCH, MCHC, MVC]])

    if(Result[0]==1) :
        Result = 'Pasien Mengidap Anemia'
    else : 
        Result = 'Pasien Tidak Mengidap Anemia'
st.success(Result)

st.write('191351099 - Tendy Ilhamudin Firdaus')