import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Vehicle Data Viewer')  # Se agrega Encabezado de la App

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

# crear casillas de verificación
build_histogram = st.checkbox('Construir un histograma')
build_scatterplot = st.checkbox('Construir un diagrama de dispersión')

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Visualización de histograma de Kilometraje')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer",
                       title='Distribución de kilometraje individual de vehículos')

    # cambiar el nombre de los ejes
    fig.update_layout(xaxis_title='Kilometraje',
                      yaxis_title='No. de Vehículos')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if build_scatterplot:
    st.write('Visualización de diagrama de dispersión de precio vs kilometraje')

    # crear scatterplot
    fig = px.scatter(car_data, x="odometer", y="price", title='Relación Precio vs Kilomeraje',
                     color_discrete_sequence=['#36b381'])  # crear un gráfico de dispersión

    # cambiar el nombre de los ejes
    fig.update_layout(xaxis_title='Kilometraje', yaxis_title='Precio (USD)')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

'''hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
'''
