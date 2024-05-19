from dotenv import find_dotenv, load_dotenv
from transformers import pipeline

import google.generativeai as genai
import os

import requests

load_dotenv(find_dotenv())

## image to text model
def imgtotext(url):
    img_to_text = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base")
    response = img_to_text(url)
    response_text = response[0]['generated_text']
    print(response_text)
    return response_text

##text to story
def textToStory(text):
    genai.configure(api_key=os.environ["API_KEY"])
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("You are a story teller. You can generate a short story based on a simple narrative, the story should not be more than 50 words, minimum 30 words and use simple english. The topic is {text}")
    print(response.text)
    return response.text

##story to speech
def storyToSpeech(story):
    API_TOKEN = os.getenv("API_Token")
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    payload = {
        "inputs" : story
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    with open('audio.flac','wb') as file:
        file.write(response.content)


# topic = imgtotext("boys.jpg")
# story = textToStory(topic)
# storyToSpeech(story)