import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pytesseract as ts
from PIL import Image


def load_image(image_file):
	img = Image.open(image_file)
	return img


def write_centered_image(img):
    st.image(img, use_column_width=True)
