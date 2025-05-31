# import base64
# import os
# from google import genai
# from google.genai import types
import modules
from modules import *
api = modules.api_key

while True:
    genai.configure(api_key=api)

    # Create the model
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(history=[])


    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source)
        print("Recognizing...")

        try:
            promt = r.recognize_google(audio)
            print("You said:", promt)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Could not request results from Google.")


    # Text to speech
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    response = chat_session.send_message(f"Please reply in not more than 30 words.\n{promt}")
    text_response = response.text
    engine.say(text_response)
    print(response.text)
    engine.runAndWait()


