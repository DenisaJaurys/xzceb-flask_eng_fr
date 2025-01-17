import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
translator_instance = LanguageTranslatorV3(
    version='{2018-05-01}',
    authenticator=authenticator)

translator_instance.set_service_url(url)

def english_to_french(english_text):
    if len(english_text)!=0:
        french_text=translator_instance.translate(
            text=english_text,
            model_id='en-fr').get_result()["translations"][0]["translation"]
    else:
        french_text=""

    return french_text

def french_to_english(french_text):
    if len(french_text) != 0:
        english_text = translator_instance.translate(
            text=french_text,
            model_id='fr-en').get_result()["translations"][0]["translation"]
    else:
        english_text = ""

    return english_text
