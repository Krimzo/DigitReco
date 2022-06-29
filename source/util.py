import streamlit as st
import pytesseract as ts
from PIL import Image


def centered_title(title):
    st.markdown("<h1 style='text-align: center; color: white;'>" + title + "</h1>", unsafe_allow_html=True)


def centered_text(text):
    st.markdown("<h2 style='text-align: center; color: white;'>" + text + "</h2>", unsafe_allow_html=True)


def load_image(image_file):
	return Image.open(image_file)


def show_image(img):
    st.image(img, use_column_width=True)


def read_digits(img):
    raw_digits = ts.image_to_string(img, config="--psm 11 --oem 3")
    return "".join(c for c in raw_digits if c.isdigit())
