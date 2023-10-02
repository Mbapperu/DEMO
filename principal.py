#importando bibliotecas necesarias 
import streamlit as st
from PIL import Image
#titulo de la pagina principal
st.title("Calculadora de gastos de un pequeño emprendedor")
#imagen de un kiosco
image = Image.open('image.png')

st.image(image, caption='')

# Demostración de la aplicación
st.header("Demostración")
st.write("Problema a Resolver:")
st.write("Muchas personas tienen dificultades para llevar un control de sus gastos mensuales y calcular su presupuesto disponible.")

st.write("Funcionamiento de la Aplicación:")
st.write("1. En la sección 'App', el usuario ingresa sus gastos mensuales en diferentes categorías.")
st.write("2. La aplicación calcula el presupuesto total sumando los gastos ingresados.")
st.write("3. El resultado se muestra en la sección 'Presupuesto Total'.")

st.write("Explicación Técnica:")
st.write("Hemos utilizado Streamlit para crear la interfaz de usuario y Python para el cálculo de presupuesto.")
st.write("La aplicación se encuentra en un repositorio de GitHub y se despliega utilizando Streamlit Sharing.")

# Ejecutar la aplicación
if __name__ == "__main__":
    st.button("Ejecutar App")
