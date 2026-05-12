import streamlit as st

usr_inp = st.text_input("Enter text here: ")
butt = st.button("Enter")
if usr_inp:
    st.title(usr_inp)
    st.divider()
    st.header(usr_inp)
    st.divider()
    st.subheader(usr_inp)
    st.divider()
    st.text(usr_inp)
    st.divider()
