import streamlit as st
import pandas as pd
from PIL import Image

def cargar_datos():
    data = pd.read_csv('data/red_recarga_acceso_publico_2021.csv', sep = ';')
    

    return data

def home():

    
    st.title('Cargatron')
    st.image('img/puntos-recarga-madrid.jpg')
    st.expander('Más información')
    df = cargar_datos()
    with st.expander('Más información'):
        st.write('Para combatir el cambio climatico facilitamos el uso de coches elecdtricos mostrando todas las estaciones de carga por Madrid.')
    with st.echo():
        st.dataframe(df)

def visualizaciones(df):
    df = cargar_datos()
    st.map(df, latitude='latidtud', longitude='longitud')
    st.bar_chart(df.groupby(['DISTRITO'])['Nº CARGADORES'].sum())
    st.bar_chart(df.groupby(['OPERADOR'])['Nº CARGADORES'].sum())

def menu_filtros(): 
    menu = st.sidebar.selectbox('Selecciona una opción', ('Distrito', 'Operador'))
    df = cargar_datos()
    