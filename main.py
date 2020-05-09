import json
var=4
from my_library.test_lib import fake_data
from my_library import __version__
#from emoji import emojize

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return f"Hello World!!!!!"

@app.route("/fakedata")
def fakedata():
    return json.dumps(fake_data())


if __name__ == "__main__":
    app.run()
