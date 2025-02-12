import streamlit as st

col1, col2 = st.columns(2, gap='small', vertical_alignment='top')

col1.image('assets/foto_perfil.png', width=300)
col2.header("Welcome to Samuel Rangel's Website")
col2.write('Data Analyst | Data Scientist | Data Engineer')