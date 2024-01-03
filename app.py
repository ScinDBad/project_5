import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.header('Datos Vehiculares y Ventas')  # Se agrega Encabezado de la App

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

# crear casillas de verificación
build_histogram = st.checkbox('Histograma (Kilometraje)')
build_scatterplot = st.checkbox('ScatterPlot (Precio vs Kilometraje)')
build_stackbar_1 = st.checkbox('BarGraph (Tipos de vehículos por condición)')
build_stackbar_2 = st.checkbox('BarGraph (Condición de vehículos por tipo)')

# Verificación de seleción de histograma
if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Visualización de histograma de Kilometraje')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer",
                       title='Distribución de kilometraje individual de vehículos')

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
    st.write('Visualización de diagrama de dispersión de precio vs kilometraje')

    # crear scatterplot
    fig = px.scatter(car_data, x="odometer", y="price", title='Relación Precio vs Kilometraje', opacity=0.4,
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
    st.write('Visualización de diagrama de barras de tipo de vehículo por condición')

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
        title='Cantidad de Vehículos por tipo y condición',
        xaxis_title='Tipo de Vehículo',
        yaxis_title='No. de Vehículos',
        barmode='stack',  # Modo apilado
    )

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# Verificación de selección de Bargraph_2
if build_stackbar_2:
    st.write('Visualización de diagrama de barras de condición de vehículo por tipo')

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
        title='Cantidad de Vehículos por condición y tipo',
        xaxis_title='Condición',
        yaxis_title='No. de Vehículos',
        barmode='stack',  # Modo apilado
    )

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
