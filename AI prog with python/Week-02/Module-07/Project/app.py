import streamlit as st
from api import note_generator, audio_generator, quiz_generator
from PIL import Image

st.title("Note Summary & Quiz Generator")
st.markdown("Upload upto 3 images to generate note summary and quized")

st.divider()

with st.sidebar:
    st.header("controls")

    images = st.file_uploader(
        "Upload the photos of your note",
        ["jpg", "png", "jpeg"],
        accept_multiple_files=True,
    )

    pil_images = []
    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)

    if images:
        if len(images) > 3:
            st.error("Upload at max 3 images")
        else:
            st.subheader("Your uploaded image")
            colmn = st.columns(len(images))
            for i, img in enumerate(images):
                with colmn[i]:
                    st.image(img)

    selection = st.selectbox(
        "Select difficulty level of quiz", ("Easy", "Medium", "High"), index=None
    )

    button_pressed = st.button("Click to active the AI", type="primary")

if button_pressed:
    if not images:
        st.error("Upload image first")

    if not selection:
        st.error("Select difficulty")

    if images and selection:
        with st.container(border=True):
            st.subheader("Your note")
            with st.spinner("Cooking ..."):
                notes_generate = note_generator(pil_images)
                st.markdown(notes_generate)

        with st.container(border=True):
            st.subheader("Audio transcription")
            with st.spinner("Cooking"):
                notes_generate = notes_generate.replace("#", "")
                notes_generate = notes_generate.replace("*", "")
                notes_generate = notes_generate.replace("`", "")
                notes_generate = notes_generate.replace("-", "")

                audio_generate = audio_generator(notes_generate)
                st.audio(audio_generate)

        with st.container(border=True):
            with st.spinner("Cooking"):
                quiz = quiz_generator(pil_images, selection)
                st.markdown(quiz)
