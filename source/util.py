import streamlit as st
import pytesseract as ts
import numpy as np
import cv2 as cv
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
    edited_image = img.convert('L')
    ign, edited_image = cv.threshold(np.array(edited_image), 125, 255, cv.THRESH_BINARY)
    edited_image = Image.fromarray(edited_image.astype(np.uint8))

    show_image(edited_image)

    raw_digits = ts.image_to_string(edited_image, config="--psm 12 --oem 3")
    return "".join(c for c in raw_digits if c in "0123456789,.")
