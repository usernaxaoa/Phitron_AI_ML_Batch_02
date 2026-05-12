import streamlit as st

audio_upload = st.file_uploader("Enter audio file", ["mp3", "ogg"])

play_audio = st.button("Play audio")
if play_audio:
    if audio_upload:
        st.audio(audio_upload)
    else:
        st.error("Can't play audio")

video_upload = st.file_uploader("Enter video file", ["mp4", "mkv"])

play_video = st.button("Play video")
if play_video:
    if video_upload:
        st.video(video_upload)
    else:
        st.error("Can't play video")
