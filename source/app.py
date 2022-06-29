import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pytesseract as ts
from PIL import Image


def load_image(image_file):
	img = Image.open(image_file)
	return img


st.title("Digital Number Recognition")

image_file = st.file_uploader("Upload Image", type=["png","jpg","jpeg"])

if image_file is not None:
    file_details = { "filename":image_file.name, "filetype":image_file.type, "filesize":image_file.size }
    st.write(file_details)
    st.image(load_image(image_file), width=500)
