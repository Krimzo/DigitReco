from read import *


centered_title("Digital Number Recognition")

image_info = st.file_uploader("", type=["png", "jpg", "jpeg", "bmp"], accept_multiple_files=False)

if image_info is not None:
    image_file = load_image(image_info)
    if image_file is not None:
        show_image(image_file)
        if centered_button("Read Digits", "Opens the image file and reads the digits"):
            centered_text(read_digits(image_file))
