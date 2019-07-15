# Library Import
import Class_OCR as OCR
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory


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
subscription_key = ""
assert subscription_key
# You must use the same region in your REST call as you used to get your
# subscription keys. For example, if you got your subscription keys from
# westus, replace "westcentralus" in the URI below with "westus".
 # Free trial subscription keys are generated in the "westus" region.
# If you use a free trial subscription key, you shouldn't need to change
# this region.
vision_base_url = "https://francecentral.api.cognitive.microsoft.com/vision/v2.0/"
ocr_url = vision_base_url + "ocr"

# img url
IMG_URL = None

# Set image_url to the URL of an image that you want to analyze.

#### Flask server ####
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
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

#### Interpret order -----> Customer{}, Articles{} ####

#### Cosmos DB ####

#### EDI transformation ####

#### Order assistance interface (Web app) ####

#### Export to Order Systeme ####


if __name__ == '__main__':
    my_ocr = OCR.Ocr(subscription_key, ocr_url)
    my_ocr.ocr_system()
