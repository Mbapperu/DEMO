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
