# Library Import
import requests
import time
from O365 import Account
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
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/" + \
                "Atomist_quote_from_Democritus.png/338px-Atomist_quote_from_Democritus.png"
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params = {'language': 'unk', 'detectOrientation': 'true'}
data = {'url': image_url}
response = requests.post(ocr_url, headers=headers, params=params, json=data)
response.raise_for_status()

#### OCR ####
def ocr_systeme():

    analysis = response.json()

    # Extract the word bounding boxes and text.
    line_infos = [region["lines"] for region in analysis["regions"]]
    word_infos = []
    for line in line_infos:
        for word_metadata in line:
            for word_info in word_metadata["words"]:
                word_infos.append(word_info)

    # Display the image and overlay it with the extracted text.
    plt.figure(figsize=(5, 5))
    image = Image.open(BytesIO(requests.get(image_url).content))
    ax = plt.imshow(image, alpha=0.5)
    for word in word_infos:
        bbox = [int(num) for num in word["boundingBox"].split(",")]
        text = word["text"]
        origin = (bbox[0], bbox[1])
        patch = Rectangle(origin, bbox[2], bbox[3],
                          fill=False, linewidth=2, color='y')
        ax.axes.add_patch(patch)
        plt.text(origin[0], origin[1], text, fontsize=20, weight="bold", va="top")
        print(text)
    plt.axis("off")


#### Interpret order -----> Customer{}, Articles{} ####

#### Cosmos DB ####

#### EDI transformation ####

#### Order assistance interface (Web app) ####

#### Export to Order Systeme ####


if __name__ == '__main__':
    ocr_systeme()