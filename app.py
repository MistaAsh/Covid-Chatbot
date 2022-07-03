from flask import Flask, render_template, request
from model import getPrediction
import os

UPLOAD_FOLDER = 'static/pic'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__, static_folder = 'static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html')
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            destination = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(destination)
            message = getPrediction(destination)
            os.remove(destination)
            return render_template('index.html', user_name = message)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080, debug = True)