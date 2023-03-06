import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Authenticate
authenticator = IAMAuthenticator(apikey)

# Create Translator instance
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    """
    This function translates English text to French
    """
    result = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    translations = result['translations']
    translation = translations[0]
    french_text = translation['translation']
    return french_text

def frenchToEnglish(french_text):
    """
    This function translates French text to English
    """
    result = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    translations = result['translations']
    translation = translations[0]
    english_text = translation['translation']
    return english_text
