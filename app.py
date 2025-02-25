# Importar librerias

import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("vehicles_us.csv")

st.header("Generacion de graficos")

button_hist = st.button('Generar histograma')
button_disp = st.button('Generar grafico de dispersion')

if button_hist:

    st.write('Generamos histograma a partir de los datos')
    hist = px.histogram(df, x='odometer')
    st.plotly_chart(hist, use_container_width=True)

if button_disp:
    
    st.write('Generamos un grafico de dispersion a partir de los datos')
    disp = px.scatter(df,x='odometer', y='price')
    st.plotly_chart(disp,use_container_width=True)
