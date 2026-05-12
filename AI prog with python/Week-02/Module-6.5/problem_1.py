import streamlit as st

n1 = st.number_input("Enter first number: ", value=None)
n2 = st.number_input("Enter second number: ", value=None)

operation = st.selectbox("Choose operation", ("+", "-", "*", "/"), index=None)

butt = st.button("Calculate")
if butt:
    if operation == "+":
        st.write(f"sum is {n1 + n2}")
    elif operation == "-":
        st.write(f"sub is {n1 - n2}")
    elif operation == "*":
        st.write(f"mul is {n1 * n2}")
    elif operation == "/":
        st.write(f"div is {n1 / n2}")
