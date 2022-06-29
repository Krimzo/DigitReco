from util import *


st.title("Digital Number Recognition")

image_info = st.file_uploader("", type=["png", "jpg", "jpeg", "bmp"], accept_multiple_files=False)

if image_info is not None:
    st.write({ "filename":image_info.name, "filetype":image_info.type, "filesize":image_info.size })

    image_file = load_image(image_info)
    write_centered_image(image_file)
