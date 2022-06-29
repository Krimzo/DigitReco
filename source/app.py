from learning import *


centered_title("Digital Number Recognition")

image_info = st.file_uploader("", type=["png", "jpg", "jpeg", "bmp"], accept_multiple_files=False)

if image_info is not None:
    image_file = load_image(image_info)
    if image_file is not None:
        if st.button("Read Digits", help="Reads the image file and looks for digits"):
            centered_text("Digits: " + read_digits(image_file))
            write_image(image_file)
