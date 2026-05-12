import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
get_api = os.environ.get("API_KEY")
client = genai.Client(api_key=get_api)

user_content = st.text_input("Enter your prompt: ")
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=f"Explain this question in 100 words {user_content}",
)
st.divider()

st.markdown(response.text)
