import streamlit as st
import pandas as pd
import libreria_funciones as lf



#TITULO DE LA APLICACION

st.set_page_config(page_title="Análisis de Clientes Bancarios", layout="wide")
st.sidebar.title("Configuración")
st.title("Proyecto final Rojas-Cobos-Lara")

uploaded_files = st.file_uploader(
    "Upload data", accept_multiple_files=True, type="csv"
)
for uploaded_file in uploaded_files:
    df = pd.read_csv(uploaded_file)
    st.write(df)
