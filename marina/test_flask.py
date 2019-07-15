import os
import re
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory
import requests
import json


UPLOAD_FOLDER = os.getcwd()
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["DEBUG"] = True


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@app.route('/uploads/<filename>')
def uploaded_file(filename):

    #URL = url_for('uploaded_file')
    #print(URL)
    # Replace <Subscription Key> with your valid subscription key.
    subscription_key = ""
    assert subscription_key

    # You must use the same region in your REST call as you used to get your
    # subscription keys. For example, if you got your subscription keys from
    # westus, replace "westcentralus" in the URI below with "westus".
    #
    # Free trial subscription keys are generated in the "westus" region.
    # If you use a free trial subscription key, you shouldn't need to change
    # this region.
    vision_base_url = "https://francecentral.api.cognitive.microsoft.com/vision/v2.0/"

    ocr_url = vision_base_url + "ocr"

    # Set image_url to the URL of an image that you want to analyze.
    image_url = request.url


    headers = {'Ocp-Apim-Subscription-Key': subscription_key}
    params = {'language': 'unk', 'detectOrientation': 'true'}
    data = {'url': "https://cdn.discordapp.com/attachments/595952680330068003/600263216593109003/test_bon_de_commande1.jpg"}
    #print("data = ", data) # "https://cdn-01.media-brady.com/store/sefr/media/wysiwyg/SEFR/content_pages/bon_commande/BdC.jpg"
    response = requests.post(ocr_url, headers=headers, params=params, json=data)
    response.raise_for_status()

    analysis = response.json()
    #print("analysis = ", analysis)

    # Extract the word bounding boxes and text.
    line_infos = [region["lines"] for region in analysis["regions"]]
    word_infos = []
    text = ""
    for line in line_infos:
        for word_metadata in line:
            for word_info in word_metadata["words"]:
                word_infos.append(word_info)
                #print(word_info["text"])
                text = text + " " + word_info["text"]
    #print(word_infos)

    with open("RESULT3.json", "w") as f_write:
        json.dump(analysis, f_write, indent=4)

    with open("TEXT3.json", "w") as f:
        print("text = ", text)
        mails = re.search(r"([a-zA-Z][a-zA-Z0-9-._]*@[a-zA-Z]+.[a-zA-Z]{1,4})", str(text))
        if mails:
            print("mails : ", mails.group())
        telephones = re.search(r"(\s[0\+33](\d{9}|[0-9. ]{13}))", text)
        if telephones:
            print("telephones : ", telephones.group())
        no_commande = re.search(r"(\d{2}-\d{3}-\d{2})", text)
        if no_commande:
            print("no_commande : ", no_commande.group())
        no_client = re.search(r"([A-Z]\d{6})", text)
        if no_client:
            print("no_client : ", no_client.group())
        json.dump(text, f, indent=4)

    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run()
