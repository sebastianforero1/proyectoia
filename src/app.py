import streamlit as st
from dotenv import load_dotenv
import os
import openai

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la clave de API de OpenAI desde las variables de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title('Generador de imágenes con DALL-E')

with st.form("images_form"):
    text = st.text_input("Texto para generar la imagen")
    num_image = st.number_input("Número máximo de imágenes a generar", min_value=1, max_value=10, value=1)
    image_size = st.selectbox("Tamaño de la imagen", ["256x256", "512x512", "1024x1024"], index=0)
    submit_button = st.form_submit_button(label="Generar imágenes")

if submit_button:
    st.write("Generando la imagen...")
    try:
        # Uso de la nueva API de OpenAI para generar imágenes
        response = openai.Image.create(
            prompt=text,
            n=num_image,
            size=image_size
        )
        for i in range(num_image):
            url = response['data'][i]['url']
            st.image(url, caption=f"Imagen {i+1}", use_column_width=True)
    except Exception as e:
        st.error(f"Error al generar la imagen: {e}")








         