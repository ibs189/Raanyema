import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing import image
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from keras.applications.imagenet_utils import preprocess_input

def instantiate_model():
    global model
    model = load_model('models/deka-multiclassifier.X.h5')

def prepare_image(image, target):
    if image.mode != 'RGB':
        image = image.convert('RGB')
	
    resized_img = image.resize(target)
    img_as_array = image.img_to_array(resized_img)
    expanded_img = np.expand_dims(img_as_array, axis=0)
    processed_img = preprocess_input(expanded_img)

    return processed_img

app = Flask(__name__)

@app.route('/predict', methods = ['POST', 'GET'])
def predict():
	
    data = {
        'success': False,
        'predictions': [],
    }

    img_labels = {
        1: 'bedroom',
        0: 'bathroom',
        2: 'kitchen',
        3: 'living-room',
        4: 'view',
    }

    if request.method == 'POST':
        if request.files.get('image'):
            image = request.files['image'].read()
            image = Image.open(io.BytesIO(image))
            
            image = prepare_image(image, target = (224, 224))
            prediction = model.predict(image)        

            correct_pred = np.argmax(prediction)
            results = img_labels[correct_pred]
            data['prediction'].append(results)
            data['success'] = True

    return jsonify(data)


if __name__ == '__main__':
    print(("* Loading Keras model and Flask starting server..."
        "please wait until server has fully started"))
    instantiate_model()
    app.run()
