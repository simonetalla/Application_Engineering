import json
var=4
from my_library.test_lib import fake_data
from my_library import __version__
#from emoji import emojize

#from flask import Flask

"""app = Flask(__name__)

@app.route("/")
def hello():
    return f"Hello World!!!!!"
def automa():
    return f"AUTOMATIC UPDATE"

@app.route("/fakedata")
def fakedata():
    return json.dumps(fake_data())
"""
import logging
import os

import pickle
from flask import Flask, request
from google.cloud import storage

MODEL_BUCKET = os.environ['MODEL_BUCKET']
MODEL_FILENAME = os.environ['MODEL_FILENAME']
MODEL = None

app = Flask(__name__)


@app.before_first_request
def _load_model():
    global MODEL
    client = storage.Client()
    bucket = client.get_bucket(MODEL_BUCKET)
    blob = bucket.get_blob(MODEL_FILENAME)
    s = blob.download_as_string()

    # Note: Change the save/load mechanism according to the framework
    # used to build the model.
    MODEL = pickle.loads(s)


@app.route('/', methods=['GET'])
def index():
    return str(MODEL), 200


@app.route('/predict', methods=['POST'])
def predict():
    X = request.get_json()['X']
    y = MODEL.predict(X).tolist()
    return json.dumps({'y': y}), 200


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == "__main__":
    app.run()
