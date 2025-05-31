# To run this code you need to install the following dependencies:
# pip install google-genai
import modules
from modules import *



def generate(promt):
    client = genai.Client(
        api_key=modules.API_KEY
    )
    model = "gemini-1.5-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=promt),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
