import streamlit as st
from PIL import Image
# Sección Contacto
st.header("Contacto")
st.write("Esta aplicación fue desarrollada por:")
st.write("- CEO: Joaquín Tobar")
st.write("- Product Manager: Tomás Valdés")
st.write("- Developer: Jesus Berroeta")

image = Image.open('klipartz.com.png')

st.image(image, caption='')