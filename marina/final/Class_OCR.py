import re
import json
import requests


class Ocr:
    def __init__(self, subscription_key, ocr_url, img_url="https://cdn.discordapp.com/attachments/595952680330068003/"
                                                          "600263216593109003/test_bon_de_commande1.jpg"):

        self.image_url = img_url
        self.headers = {'Ocp-Apim-Subscription-Key': subscription_key}
        self.params = {'language': 'unk', 'detectOrientation': 'true'}
        self.data = {'url': self.image_url}
        self.response = requests.post(ocr_url, headers=self.headers, params=self.params, json=self.data)
        print("self.response = ", self.response)
        self.response.raise_for_status()
        self.analysis = None
        self.text = None
        self.dico = None

    #### OCR ####
    def ocr_system(self):

        analysis = self.response.json()

        # Extract the word bounding boxes and text.
        line_infos = [region["lines"] for region in analysis["regions"]]
        word_infos = []
        text = ""
        for line in line_infos:
            for word_metadata in line:
                for word_info in word_metadata["words"]:
                    word_infos.append(word_info)
                    text = text + " " + word_info["text"]

        self.analysis = analysis
        self.text = text
        # OCR analysis file
        with open("text_analysis_HEROKU.json", "w") as f_write:
            json.dump(analysis, f_write, indent=4, ensure_ascii=False)

        # extracted text file
        with open("text_brut_HEROKU.txt", "w") as f:
            json.dump(text, f, indent=4, ensure_ascii=False)

        # output extracted keywords
        with open("dico_output_HEROKU.json", "w") as file:
            dico = {'no_commande': [],
                    'no_client': [],
                    'mails' : [],
                    'tel': [],
                    'no_ref': ""}

            # regex for output extraction
            mails = re.search(r"([a-zA-Z][a-zA-Z0-9-._]*@[a-zA-Z]+.[a-zA-Z]{1,4})", str(text))
            if mails:
                dico['mails'].append( mails.group())
            telephones = re.search(r"(\s[0\+33](\d{9}|[0-9. ]{13}))", text)
            if telephones:
                dico['tel'].append(telephones.group())
            no_commande = re.search(r"(\d{2}-\d{3}-\d{2})", text)
            if no_commande:
                dico['no_commande'].append(no_commande.group())
            no_client = re.search(r"([A-Z]\d{6})", text)
            if no_client:
                dico['no_client'].append(no_client.group())
            no_ref = re.findall(r"(\s\d{6})", text)
            if no_ref:
                dico['no_ref'] = no_ref

            self.dico = dico
            print("DICO = ", dico)
            json.dump(dico, file, indent=4, ensure_ascii=False)
