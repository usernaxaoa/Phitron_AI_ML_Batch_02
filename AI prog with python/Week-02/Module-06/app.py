from google import genai
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

user_content = st.text_input("Ente a question: ")
pressed = st.button("Enter")

response = client.models.generate_content(
    model="gemini-3.1-pro-preview", contents=f"{user_content} in 100 words"
)

st.subheader(f"Question: {user_content}")

if pressed:
    st.subheader("Answer:")
    st.markdown(response.text)
