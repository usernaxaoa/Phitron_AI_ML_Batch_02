import streamlit as st

image_uploader = st.file_uploader(
    label="Enter images: ", type=["jpg", "jpeg", "png"], accept_multiple_files=True
)
if image_uploader:
    column = st.columns(len(image_uploader))
    if len(column) == 3:
        for i, per_img in enumerate(image_uploader):
            with column[i]:
                st.image(per_img)
    else:
        st.error("Enter 3 picture. not more or less.")
