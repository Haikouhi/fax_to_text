import os
import json
import requests

API_KEY = 'KEY'
ENDPOINT = 'https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/ocr'
DIR = os.getcwd()

def handler():
    text = ''
    for filename in sorted(os.listdir(DIR)):
        if filename.endswith("BdC.jpg"):
            pathToImage = '{0}/{1}'.format(DIR, filename)
            results = get_text(pathToImage)
            text += parse_text(results)

    open('test_output.txt', 'w').write(text)

def parse_text(results):
    text = ''
    for region in results['regions']:
        for line in region['lines']:
            for word in line['words']:
                text += word['text'] + ' '
            text += '\n'
    return text

def get_text(pathToImage):
    print('Processing: ' + pathToImage)
    headers = {
        'Ocp-Apim-Subscription-Key': API_KEY,
        'Content-Type': 'application/octet-stream'
    }
    params = {
        'language': 'en',
        'detectOrientation ': 'true'
    }
    payload = open(pathToImage, 'rb').read()
    response = requests.post(ENDPOINT, headers=headers, params=params, data=payload)
    results = json.loads(response.content)
    return results

if __name__ == '__main__':
    handler()