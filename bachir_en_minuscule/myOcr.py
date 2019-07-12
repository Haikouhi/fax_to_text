import requests

class Ocr:
    def __init__(self, subscription_key, ocr_url):

        self.image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/" + \
                "Atomist_quote_from_Democritus.png/338px-Atomist_quote_from_Democritus.png"
        self.headers = {'Ocp-Apim-Subscription-Key': subscription_key}
        self.params = {'language': 'unk', 'detectOrientation': 'true'}
        self.data = {'url': self.image_url}
        self.response = requests.post(ocr_url, headers=self.headers, params=self.params, json=self.data)
        self.response.raise_for_status()

        #### OCR ####
    def ocr_systeme(self):

        analysis = self.response.json()

        # Extract the word bounding boxes and text.
        line_infos = [region["lines"] for region in analysis["regions"]]
        word_infos = []
        for line in line_infos:
            for word_metadata in line:
                for word_info in word_metadata["words"]:
                    word_infos.append(word_info)

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

