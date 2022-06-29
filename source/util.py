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
    return "" + ts.image_to_string(img, config="--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789")
