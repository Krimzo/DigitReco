from util import *


st.title("Digital Number Recognition")

image_file = st.file_uploader("", type=["png", "jpg", "jpeg", "bmp"], accept_multiple_files=False)

if image_file is not None:
    image = load_image(image_file)

    st.write({ "filename":image_file.name, "filetype":image_file.type, "filesize":image_file.size })
    write_centered_image(image, 500, 500)
