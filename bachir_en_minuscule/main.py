# -*- coding: utf-8 -*-
# Library Import
import requests
import time
from O365 import Account
from bachir_en_minuscule.myOcr import Ocr

from matplotlib.patches import Polygon

from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
from pprint import pprint
from bachir_en_minuscule.myTextAnalyze import Analyze_Text
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
subscription_key = "f7c364054f6740d385e57fb37df8e34c"
assert subscription_key
# You must use the same region in your REST call as you used to get your
# subscription keys. For example, if you got your subscription keys from
# westus, replace "westcentralus" in the URI below with "westus".
 # Free trial subscription keys are generated in the "westus" region.
# If you use a free trial subscription key, you shouldn't need to change
# this region.
vision_base_url = "https://exakisfexte.cognitiveservices.azure.com//vision/v2.0/"

ocr_url = vision_base_url + "ocr"

#### Interpret order -----> Customer{}, Articles{} ####

#### Cosmos DB ####

#### EDI transformation ####

#### Order assistance interface (Web app) ####

#### Export to Order Systeme ####


if __name__ == '__main__':
    my_ocr = Ocr(subscription_key, ocr_url)
    my_ocr.ocr_systeme()