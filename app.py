import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos desde la raíz de tu proyecto
car_data = pd.read_csv("vehicles_us.csv")

st.header("Cuadro de Mando de Venta de Vehículos")

# Botón para construir un histograma
hist_button = st.button("Construir histograma")

if hist_button:
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncios de venta de coches"
    )
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir un gráfico de dispersión
scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Creación de un gráfico de dispersión para analizar el kilometraje")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
    
