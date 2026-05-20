import streamlit as st
import pandas as pd
import libreria_funciones as lf

st.sidebar.title("configuración")
st.title("Proyecto final UCG")

uploaded_files = st.file_uploader(
    "Upload data", accept_multiple_files=True, type="csv"
)
for uploaded_file in uploaded_files:
    df = pd.read_csv(uploaded_file)
    st.write(df)
