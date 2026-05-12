# import streamlit as st
# from google import genai
# from dotenv import load_dotenv
# import os
# from PIL import Image
# load_dotenv()

# api = os.getenv("Gemini_api_key")
# client = genai.Client(api_key=api)

# images = st.file_uploader(
#     "Upload the photos of your note",
#     ["jpg", "png", "jpeg"],
#     accept_multiple_files=True
# )

# if images:
#     pil_images = []
#     for img in images:
#         pil_img = Image.open(img)
#         pil_images.append(pil_img)

#     prompt = "Summarize the picture in note format at max 100 words, make sure to add all markdown to differentiate different section"

#     response = client.models.generate_content(
#         model = "gemini-2.5-flash",
#         contents = [pil_images, prompt]
#     )

#     st.markdown(response.text)


