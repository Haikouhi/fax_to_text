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
        self.response.raise_for_status()

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

        # OCR analysis file
        with open("text_analysis.json", "w") as f_write:
            json.dump(analysis, f_write, indent=4, ensure_ascii=False)

        # extracted text file
        with open("text_brut.txt", "w") as f:
            json.dump(text, f, indent=4, ensure_ascii=False)

        # output extracted keywords
        with open("dico_output.json", "w") as file:
            dico = {'no_commande': [],
                    'no_client': [],
                    'mails' : [],
                    'tel': []}

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

            json.dump(dico, file, indent=4, ensure_ascii=False)

        """
        # Display the image and overlay it with the extracted text.
        plt.figure(figsize=(5, 5))
        image = Image.open(BytesIO(requests.get(self.image_url).content))
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
        """
