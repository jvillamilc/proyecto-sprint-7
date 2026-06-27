# 🚗 Análisis de Anuncios de Venta de Coches — Aplicación Web Interactiva

**TripleTen Data Science Bootcamp | Sprint 7**

## Descripción del proyecto

Este proyecto consiste en el desarrollo de una aplicación web interactiva construida con **Streamlit** y desplegada en la nube. La aplicación permite explorar visualmente un dataset real de anuncios de venta de coches en Estados Unidos, con el objetivo de identificar patrones en los precios, kilometraje y condición de los vehículos.

El enfoque del proyecto no es solo el análisis de datos, sino el proceso completo de ingeniería: configuración de entorno virtual, desarrollo de la app, control de versiones con Git y despliegue en producción.

## Demo en vivo

🔗 [Ver aplicación desplegada](https://proyecto-sprint-7.onrender.com) 
*(reemplaza este enlace con tu URL real de Render)*

## Dataset

`vehicles_us.csv` — Anuncios de venta de coches usados en EE.UU.

Columnas principales: precio, año del modelo, condición, kilometraje, tipo de combustible, tipo de transmisión, tracción, número de cilindros, días publicado.

## Análisis exploratorio

El notebook `notebooks/EDA.ipynb` documenta el análisis inicial del dataset:

- Distribución de precios por tipo de vehículo
- Relación entre kilometraje (odómetro) y precio
- Patrones por condición del vehículo y año del modelo
- Identificación de valores atípicos y datos faltantes

## Funcionalidad de la app

La aplicación incluye:

- **Histograma interactivo** — distribución del kilometraje de los vehículos
- **Gráfico de dispersión** — relación entre precio y kilometraje
- Visualizaciones generadas con **Plotly** e integradas en **Streamlit**
- Interfaz con casillas de verificación para activar cada gráfico

## Stack técnico

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=flat-square&logo=render&logoColor=black)

## Estructura del repositorio
