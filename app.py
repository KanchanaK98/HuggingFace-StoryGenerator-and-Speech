from dotenv import find_dotenv, load_dotenv
from transformers import pipeline

import google.generativeai as genai
import os


load_dotenv(find_dotenv())

## image to text model
def imgtotext(url):
    img_to_text = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base")
    response = img_to_text(url)
    response_text = response[0]['generated_text']
    print(response_text)
    return response_text

##text to story
def textToSpeech(text):
    genai.configure(api_key=os.environ["API_KEY"])
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(text)
    print(response.text)
    return response.text


##imgtotext("boys.jpg")
textToSpeech("Hi there?")