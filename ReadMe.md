# Raanyema
Raanyema is full flegde deep learning-based image classifier

## Running locally
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirement files

```bash
pip install requirements.txt
```

## usage 
```bash 
run:
python server.py
use:
test_model.py: to send a sample image to get a classification
```

## For Reproduction purposes
``` python
run:
deka-multiclassifier.ipynb

Structure your training data images as such
training_data/
            class_a/
            class_b/
            class_c/
            ......

trained model will be save in models/