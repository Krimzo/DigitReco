from learning import *


centered_title("Digital Number Recognition")

image_info = st.file_uploader("", type=["png", "jpg", "jpeg", "bmp"], accept_multiple_files=False)

if image_info is not None:
    image_file = load_image(image_info)
    if image_file is not None:
        was_pressed = False
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(" ")
        with col2:
            was_pressed = st.button("Read Digits", help="Reads the image file and looks for digits")
        with col3:
            st.write(" ")

        if was_pressed:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write(" ")
            with col2:
                st.write(read_digits(image_file))
            with col3:
                st.write(" ") 

            col1, col2, col3 = st.columns(3)
            with col1:
                st.write(" ")
            with col2:
                st.image(image_file)
            with col3:
                st.write(" ")     
