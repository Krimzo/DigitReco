from read import *


centered_title("Digital Number Recognition")

image_info = st.file_uploader("", type=["png", "jpg", "jpeg", "bmp"], accept_multiple_files=False)

if image_info is not None:
    image_file = load_image(image_info)
    if image_file is not None:
        write_image(image_file)

        cols = st.columns(5)
        was_pressed = False
        
        with cols[1]:
            was_pressed = st.button("Read Digits", help="Opens the image file and reads the digits")

        if was_pressed:
            with cols[2]:
                st.write("=>")
            with cols[3]:
                st.write(read_digits(image_file))
