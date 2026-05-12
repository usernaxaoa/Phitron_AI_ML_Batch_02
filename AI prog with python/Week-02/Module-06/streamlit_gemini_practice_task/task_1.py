import streamlit as st

user_name = st.text_input("Enter your name: ")
user_age = st.number_input("Enter your age: ", value=None)
user_occupation = st.selectbox(
    "Choose your occupaton",
    ("Student", "Employee", "Businessman", "Freelancer"),
    index=None,
)

data_entered = st.button("Upload Informatin")

if data_entered:
    if user_name == "" or user_age == None or user_occupation == None:
        st.warning("Fill every info")
    else:
        st.success("Successfull")
