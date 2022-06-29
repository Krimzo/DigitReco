import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pytesseract as ts
from PIL import Image


def centered_title(title):
    st.markdown("<h1 style='text-align: center; color: white;'>" + title + "</h1>", unsafe_allow_html=True)


def centered_text(text):
    st.markdown("<h2 style='text-align: center; color: white;'>" + text + "</h2>", unsafe_allow_html=True)


def centered_button(text, help_text):
    button_state = False
    col1, col2, col3 , col4, col5 = st.beta_columns(5)
    with col1:
        pass
    with col2:
        pass
    with col4:
        pass
    with col5:
        pass
    with col3:
        button_state = st.button(text, help=help_text)
    return button_state


def load_image(image_file):
	img = Image.open(image_file)
	return img


def write_image(img):
    st.image(img, use_column_width=True)
