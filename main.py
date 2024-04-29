import streamlit as st
import pandas as pd
from PIL import Image
from functions import *
# from functions import home, datos, cargar_datos, menu_filtros
#st.beta_expander ahora es expander
# Este es mi script


st.set_page_config(page_title='Cargatron', layout='wide', page_icon=':battery:')

menu = st.sidebar.selectbox('Selecciona una opción', ('Home', 'Visualizaciones', 'Filtros'))

uploaded_file = st.file_uploader("Sube un archivo .csv", type= ['.csv'])
      
if menu == 'Home':
    home()

elif menu == 'Visualizaciones':
    df= cargar_datos()
    visualizaciones(df) 
elif menu == 'Filtros':
    menu_filtros()
    



st.write('Hola mundo')

st.balloons()