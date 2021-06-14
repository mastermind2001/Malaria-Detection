import os
import re
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
import tensorflow as tf
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

MODEL_PATH ='model.h5'

model = load_model(MODEL_PATH)

def model_predict(img_path, model):
    image = Image.open(img_path)
    img = image.resize((100, 100))
    img = np.asarray(img).reshape((1, 100, 100, 3))/255
    prediction = np.squeeze(model.predict(img))
    if prediction < 0.5:
        prediction = 0
    else:
        prediction = 1
    
    classes = {0:"Normal",1:"Malaria"}
    
    return classes[(prediction)]


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, secure_filename(f.filename))
        f.save(file_path)

        preds = model_predict(file_path, model)
        return preds
    return None


if __name__ == '__main__':
    app.run(debug =True)
