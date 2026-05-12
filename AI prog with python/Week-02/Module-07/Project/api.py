from google import genai
from dotenv import load_dotenv
import os
from gtts import gTTS
import io

load_dotenv()

api = os.getenv("Gemini_api_key")
client = genai.Client(api_key=api)

prompt = "Summarize the picture in note format at max 100 words, make sure to add all markdown to differentiate different section"


def note_generator(images):
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview", contents=[images, prompt]
    )
    return response.text


def audio_generator(text):
    speech = gTTS(text, lang="en", slow=False)

    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer


def quiz_generator(image, difficulty):
    prompt = f"Generate 3 quizzes based on the {difficulty}. make sure to add markdown to differentiate the options. also in every quiz show the answer in each question not in the last or fast."

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview", contents=[image, prompt]
    )
    return response.text
