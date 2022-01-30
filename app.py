from flask import Flask, render_template, request, session, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import cv2
import numpy as np

UPLOAD_FOLDER = './flask app/assets/images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__, static_url_path='/assets',
            static_folder='./flask app/assets',
            template_folder='./flask app')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/upload.html')
def upload():
    return render_template('upload.html')


@app.route('/upload_chest.html')
def upload_chest():
    return render_template('upload_chest.html')


@app.route('/uploaded_chest', methods=['POST', 'GET'])
def uploaded_chest():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            # filename = secure_filename(file.filename)
            file.save(os.path.join(
                app.config['UPLOAD_FOLDER'], 'upload_chest.jpg'))

    vgg16Model = load_model(
        r'models\covid_model.h5')

    image = cv2.imread(
        r'C:\Users\inba2\Documents\TRI\TRINIT_Blank_ML01\flask app\assets\images\upload_chest.jpg')  # read file

   # arrange format as per keras
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224, 224))
    image = np.array(image) / 255
    image = np.expand_dims(image, axis=0)
    pred = vgg16Model.predict(image)
    print(pred)
    # label with corresponding largest predicted probability
    print(np.argmax(pred, axis=1)[0])
    probability = np.argmax(pred, axis=1)[0]
    print("Predictions:")
    if probability > 0.5:
        chest_pred = str('%.2f' % (probability*100) + '% COVID')
    else:
        chest_pred = str(
            '%.2f' % ((1-probability)*100) + '% NonCOVID')
        print(chest_pred)

    return render_template('results_chest.html', vgg_chest_pred=chest_pred)


if __name__ == '__main__':
    app.secret_key = ".."
    app.run()
