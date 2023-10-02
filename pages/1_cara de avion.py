# Importar las bibliotecas necesarias
import streamlit as st
from PIL import Image

# Título de la aplicación
st.title("Calculadora de gastos de un pequeño emprendedor")

# Sección Home Page
st.header("Bienvenido a la calculadora de tus gastos como vendedor ")
st.write("En esta aplicación, resolveremos un problema común que le ocurre a pequeños emprendedores como TÚ: El cálculo de gastos. Así es, las matemáticas pueden ser un poquito complicadas, pero no temas, para eso estámos aquí. ")

# Sección App
st.header("Calculadora de Gastos Mensuales")
st.write("Ingresa tus gastos mensuales en diferentes categorías y te ayudaremos a calcular tu presupuesto.")

# Inicializar variables para los gastos
alquiler = st.slider("Alquiler", 0, 10000, 1000)
comida = st.slider("Comida", 0, 10000, 1000)
transporte = st.slider("Transporte", 0, 10000, 1000)

# Calcular el presupuesto total
presupuesto_total = alquiler + comida + transporte

# Mostrar el presupuesto total
st.subheader("Presupuesto Total")
st.write(f"Tu presupuesto total es: ${presupuesto_total}.")

#comando de la imagen asignada como salvavavidas en el codigo para que mister gonzalo no me baje puntos 
image = Image.open('image (1).png')

st.image(image, caption='')

