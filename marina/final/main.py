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
subscription_key = "your key here"
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
print("UPLOAD_FOLDER= ", UPLOAD_FOLDER)
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
#DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'
DOWNLOAD_FOLDER = os.path.join(UPLOAD_FOLDER, 'static')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["DEBUG"] = True
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

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
            return redirect(url_for('getResult',
                                    filename=filename))
    return '''
    <!doctype html>
    <title><center>Fexte</center></title>
    <h1><center>Fexte</center></h1>
    </br>
    <p><center><form method=post enctype=multipart/form-data>
      Upload new File :
      <input type=file name=file>
      <input type=submit value=Upload>
    </form> </center></p>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    image_url = request.url
    print("image_url = ", image_url)
    my_ocr = OCR.Ocr(subscription_key, ocr_url, image_url)
    my_ocr.ocr_system()
    
@app.route('/uploads/<filename>/result')
def getResult(filename):
    image_url = request.url
    image_url = image_url.replace('/result', '')
    print("image_url 2 = ", image_url)
    my_ocr = OCR.Ocr(subscription_key, ocr_url, image_url)
    my_ocr.ocr_system()
    print("my_ocr.dico = ", my_ocr.dico)
    print("my_ocr.text = ", my_ocr.text)
    return my_ocr.dico


# TODO : download method in order to get text.txt file from uploaded image
"""
@app.route("/uploads/<filename>/download")
def download_file(filename):
    image_url = request.url
    image_url = image_url.replace('/download', '')
    print("image_url 3 = ", image_url)
    my_ocr = OCR.Ocr(subscription_key, ocr_url, image_url)
    my_ocr.ocr_system()
    #output_stream = open(app.config['DOWNLOAD_FOLDER'] + filename, 'wb')
    #output.write(output_stream)
    print("my_ocr.text = ", my_ocr.text)
    with open(app.config['DOWNLOAD_FOLDER'] + "TEST.txt", 'wb') as f:
        f.write(my_ocr.text)
        return send_file(f, as_attachement=True)
    #return send_file(f, as_attachment=True) 
"""

#### Interpret order -----> Customer{}, Articles{} ####

#### Cosmos DB ####

#### EDI transformation ####

#### Order assistance interface (Web app) ####

#### Export to Order Systeme ####


# NOT USE app.run with HEROKU !!!
"""
if __name__ == '__main__':
    app.run()
"""
