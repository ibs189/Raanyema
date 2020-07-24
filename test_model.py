# import the necessary packages
import requests

# initialize the Keras REST API endpoint URL along with the input
# image path
KERAS_REST_API_URL = "http://127.0.0.1:5000/predict"
IMAGE_PATH = "test_img/bathroom.jpg"

# load the input image and construct the payload for the request
image = open(IMAGE_PATH, "rb").read()
payload = {"image": image}

# submit the request
response = requests.post(KERAS_REST_API_URL, files=payload).json()

# ensure the request was successful
if response["success"]:
    # loop over the predictions and display them
    # for (i, result) in enumerate(r["predictions"]):
    #     print("{}. {}: {:.4f}".format(i + 1, result["label"],
    #         result["probability"]))
    print(response['predictions'])

# otherwise, the request failed
else:
    print("Request failed")