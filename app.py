from dotenv import find_dotenv, load_dotenv
from transformers import pipeline

load_dotenv(find_dotenv())

## image to text model
def imgtotext(url):
    img_to_text = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base")
    response = img_to_text(url)
    response_text = response[0]['generated_text']
    print(response_text)
    return response_text


imgtotext("boys.jpg")