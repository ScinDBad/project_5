import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

"""
# Datos Vehiculares y Ventas

Esta aplicación realiza un análisis y visualización de datos relacionados con vehículos y ventas.

## Subtítulo

Aquí puedes agregar información adicional sobre la aplicación.
"""

# Se agrega Encabezado de la App
st.header('Análisis Exploratorio de Datos Vehiculares')
st.subheader('Realizado por Adrián Vinueza')

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

# crear casillas de verificación
build_histogram = st.checkbox('Gráfico 1 - Histograma (Kilometraje)')
build_scatterplot = st.checkbox(
    'Gráfico 2 - ScatterPlot (Precio vs Kilometraje)')
build_stackbar_1 = st.checkbox(
    'Gráfico 3 - BarGraph (Tipos de vehículos por condición)')
build_stackbar_2 = st.checkbox(
    'Gráfico 4 - BarGraph (Condición de vehículos por tipo)')

# Verificación de seleción de histograma
if build_histogram:  # si la casilla de verificación está seleccionada

    # crear un histograma
    fig = px.histogram(car_data, x="odometer",
                       title='Grafico 1. Distribución de kilometraje individual de vehículos')

    # rotulación interactiva
    fig.update_traces(
        hovertemplate='Kilometraje: %{x}m<br>No. Vehículos: %{y}')

    # cambiar el nombre de los ejes
    fig.update_layout(xaxis_title='Kilometraje',
                      yaxis_title='No. de Vehículos')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# Verificación de selección de scatterplot
if build_scatterplot:

    # crear scatterplot
    fig = px.scatter(car_data, x="odometer", y="price", title='Gráfico 2. Relación Precio vs Kilometraje', opacity=0.4,
                     color_discrete_sequence=['#36b366'])  # crear un gráfico de dispersión

    # rotulación interactiva
    fig.update_traces(
        hovertemplate='Kilometraje: %{x}m<br>Precio(USD): $%{y:,.2f}')

    # cambiar el nombre de los ejes
    fig.update_layout(xaxis_title='Kilometraje', yaxis_title='Precio (USD)')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# Verificación de selección de Bargraph_1
if build_stackbar_1:

    # Crear un DataFrame pivotado para facilitar la creación del gráfico
    pivot_df = car_data.groupby(['type', 'condition']).size().unstack()

    # Obtener las listas de tipos, condiciones y colores
    tipos = pivot_df.index
    condiciones = pivot_df.columns

    # Crear el gráfico de barras apiladas con Plotly Graph Objects
    fig = go.Figure()

    for i, condicion in enumerate(condiciones):
        fig.add_trace(go.Bar(
            x=tipos,
            y=pivot_df[condicion],
            name=condicion,
        ))

    # Personalizar el diseño del gráfico
    fig.update_layout(
        title='Gráfico 3. Cantidad de Vehículos por tipo y condición',
        xaxis_title='Tipo de Vehículo',
        yaxis_title='No. de Vehículos',
        barmode='stack',  # Modo apilado
    )

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# Verificación de selección de Bargraph_2
if build_stackbar_2:

    # Crear un DataFrame pivotado para facilitar la creación del gráfico
    pivot_df = car_data.groupby(['condition', 'type']).size().unstack()

    # Obtener las listas de condiciones, tipos y colores
    condiciones = pivot_df.index
    tipos = pivot_df.columns

    # Crear el gráfico de barras apiladas con Plotly Graph Objects
    fig = go.Figure()

    for i, tipo in enumerate(tipos):
        fig.add_trace(go.Bar(
            x=condiciones,
            y=pivot_df[tipo],
            name=tipo,
        ))

    # Personalizar el diseño del gráfico
    fig.update_layout(
        title='Gráfico 4. Cantidad de Vehículos por condición y tipo',
        xaxis_title='Condición',
        yaxis_title='No. de Vehículos',
        barmode='stack',  # Modo apilado
    )

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
