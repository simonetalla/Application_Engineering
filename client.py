import requests
import numpy as np

class ModelServiceClient(object):
    def __init__(self, host, api_key):
        self.host = host
        self.api_key = api_key

    def predict(self, X):
        if type(X) is np.ndarray:
            X = X.tolist()

        response = requests.post(self.host + '/predict', json={'X': X},
            params={'key': self.api_key})

        response_json = response.json()
        if 'y' in response_json:
            return response_json['y']
        else:
            print(response_json)
