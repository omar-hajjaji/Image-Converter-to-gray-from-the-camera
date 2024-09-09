import streamlit as st
from PIL import Image

# Start the camera:
camera_image = st.camera_input("Camera")

# Create a pillow image instance:
img = Image.open(camera_image)

# Convert the pillow image to grayscale:
gray_img = img.convert("L")

# Render the grayscale image on the web page:
st.image(gray_img)
