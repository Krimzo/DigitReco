import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pytesseract as ts
from PIL import Image


def load_image(image_file):
	img = Image.open(image_file)
	return img

def write_centered_image(image, W, H):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(" ")
    with col2:
        st.image(image, width=W, height=H)
    with col3:
        st.write(" ")
