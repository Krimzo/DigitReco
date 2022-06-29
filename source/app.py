from util import *


centered_title("Digital Number Recognition")

image_info = st.file_uploader("", type=["png", "jpg", "jpeg", "bmp"], accept_multiple_files=False)

if image_info is not None:
    image_file = load_image(image_info)

    if image_file is not None:
        show_image(image_file)

        digit_data = read_digits(image_file)
        if digit_data is None:
            centered_text("NO DIGITS")
        else:
            centered_text(digit_data)
