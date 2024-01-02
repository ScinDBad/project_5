import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Vehicle Data Viewer')  # Se agrega Encabezado de la App

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

# crear casillas de verificación
build_histogram = st.checkbox('Construir un histograma')
build_scatterplot = st.checkbox('Construir un diagrama de dispersión')

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if build_scatterplot:
    st.write('Construir un diagrama de dispersión de precio vs kilometraje')

    # crear scatterplot
    fig = px.scatter(car_data, x="odometer", y='price')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

'''hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
'''
