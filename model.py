from keras.models import load_model
from keras.utils import load_img, img_to_array

import os
import numpy as np

UPLOAD_FOLDER = 'static/pic'

def getPrediction(destination):
    new_model = load_model('lungImage/covid_model.h5')

    img_width, img_height = 224, 224
    img = load_img(destination, target_size = (img_width, img_height))
    x = img_to_array(img)
    img = np.expand_dims(x, axis = 0)

    pred = new_model.predict(img)
    print(pred)
    print(np.argmax(pred, axis=1)[0])

    if np.argmax(pred, axis=1)[0] == 1:
        message = "You are safe"
    else:
        message = "You have COVID-19"
    return message