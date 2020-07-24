# Raanyema
Raanyema is full flegde deep learning-based image classifier. It could classifier images of bathrooms, bedrooms, kitchen, living-room, and frontal view of houses
The aim is to automate the processes of image verification, listing amenity verification and classification, etc.
## Running locally
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirement files

```bash
pip install requirements.txt
```

## usage 
```bash 
python server.py: runs a web server to recieve a sample image and returns a prediction/class of the image
test_model.py: Programmatically test server.py 
```

## For Reproduction Purposes
``` python
deka-multiclassifier.ipynb

Structure your training data images as such
training_data/
            class_a/
            class_b/
            class_c/
            ......

trained model will be save in models/