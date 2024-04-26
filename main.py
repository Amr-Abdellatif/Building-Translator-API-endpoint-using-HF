from fastapi import FastAPI
from transformers import pipeline
import uvicorn

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello World"}


@app.post("/translate")
def translate_text(text: str):
    """
    Translate text from English to French using a custom translation model.
    
    Args:
        text (str): The text to be translated.
    
    Returns:
        dict: A dictionary containing the translated text.
    """
    translator = pipeline("translation_en_to_fr", model="my_awesome_opus_books_model")
    translated_text = translator(text)
    return {"translated_text": translated_text}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True) 