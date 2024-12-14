import streamlit as st
import pandas as pd
import datetime

def change_label_style(label, font_size='2px', font_color='blue', font_family='sans-serif'):
    html = f"""
    <script>
        var elems = window.parent.document.querySelectorAll('p');
        var elem = Array.from(elems).find(x => x.innerText == '{label}');
        elem.style.fontSize = '{font_size}';
        elem.style.color = '{font_color}';
        elem.style.fontFamily = '{font_family}';
    </script>
    """
    st.components.v1.html(html)

titulo = ":blue[Mi Primera Aplicación en Streamlit]"
st.title(titulo)
autor = ":red[Carlos Pérez Reyes]"
st.title(autor)

mes = st.slider("Seleccionar mes actual:", 1, 12, 12)
st.write("Seleccionó el mes: ", mes)

st.subheader("Vista Preliminar")

## Usando With
with st.sidebar:

    nombre = st.text_input("Nombres:")
    apellido = st.text_input("Apellidos:")
    edad = st.number_input("Edad:", 0, 100)
    genero = st.radio("Genero:" , ("Masculino" , "Femenino" ))
    fecha_nacimiento = st.date_input("Fecha de nacimiento:",value="today", format="DD/MM/YYYY",min_value=None)
    hora = st.time_input("Hora de nacimiento:",value="now")

    ## Carga los datos del archivo CSV
    data = pd.read_csv('datos.csv')
    ## Obtenemos la lista de países
    paises = data['nombre'].unique()
    ## Crea la caja de selección de los países
    pais_seleccionado = st.selectbox('País de origen:', paises)
    ## Filtramos los datos
    datos_filtrados = data[data['nombre'] == pais_seleccionado]

    agree = st.checkbox("Acepta los términos")
    st.button("Vista Preliminar", type="primary")


if nombre and edad and genero and fecha_nacimiento and hora and pais_seleccionado and agree:
    st.write("Su nombre es: ", nombre)
    st.write("Su apellido es: ", apellido)
    st.write("Su edad es: ", edad, "años.")
    st.write("Su genero es: ", genero)
    st.write("Su fecha de nacimiento es:", fecha_nacimiento)
    st.write("Usted nació a las:", hora)
    st.write("Su país de origen es:",pais_seleccionado)
else:
    st.warning("Por favor llenar todos campos")

cargar_archivo = st.file_uploader("Escoja el archivo",['csv'])
if cargar_archivo is not None:

    ## Vamos a leer el archivo CSV y cargarlo a un dataframe
    dataframe = pd.read_csv(cargar_archivo)
    st.write(dataframe)




