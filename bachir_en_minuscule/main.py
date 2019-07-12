# Library Import
import requests
import time
from O365 import Account
from bachir_en_minuscule.myOcr import Ocr
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Polygon
from PIL import Image
from io import BytesIO
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials

#### Get File ---- Write ----> Storage ####

#### Connect to API Office Rest 365 ####
"""def AccountO365_Connexion():
    credentials = ('client_id', 'client_secret')

    account = Account(credentials)
    m = account.new_message()
    m.to.add('to_example@example.com')
    m.subject = 'Testing!'
    m.body = "Coucou on dirait que ça marche."
    m.send()
"""
#### Config ####
# Replace <Subscription Key> with your valid subscription key.
subscription_key = "3bb1e04945b14735ba122d3b0d946fd1"
assert subscription_key
# You must use the same region in your REST call as you used to get your
# subscription keys. For example, if you got your subscription keys from
# westus, replace "westcentralus" in the URI below with "westus".
 # Free trial subscription keys are generated in the "westus" region.
# If you use a free trial subscription key, you shouldn't need to change
# this region.
vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"

ocr_url = vision_base_url + "ocr"

# Set image_url to the URL of an image that you want to analyze.

#### Interpret order -----> Customer{}, Articles{} ####

#### Cosmos DB ####

#### EDI transformation ####

#### Order assistance interface (Web app) ####

#### Export to Order Systeme ####


if __name__ == '__main__':
    my_ocr = Ocr(subscription_key, ocr_url)
    my_ocr.ocr_systeme()