'''import dependencies'''
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
load_dotenv()
apikey = os.environ['apikey']
''''hide a url with os.environ'''
url = os.environ['url']
'''This class provides an Authenticator implementation for IAM'''
authenticator=IAMAuthenticator("L4EJOY3v1JwOiSH41JAciUlPkfaEoQuloiLl2RZDllQz")
'''setup service'''
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)
'''translating using this url'''
language_translator.set_service_url(url)
def english_to_french(englishtext):
    '''code to translate english to french'''
    translation = language_translator.translate(text=englishtext, model_id = 'en-fr').get_result()
    french_text = translation["translations"][0]["translation"]
    return french_text
def french_to_english(frenchtext):
    '''code to translate french to english'''
    translation = language_translator.translate(text=frenchtext, model_id = 'fr-en').get_result()
    english_text = translation["translations"][0]["translation"]
    return english_text
