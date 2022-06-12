import requests
import random
import pandas as pd
import logging

ENDPOINT= "http://0.0.0.0:8889"
logging.basicConfig(level=logging.INFO)

def predict(x):
    rn = random.uniform(0, 1) 
    score = True if rn > 0.57 else False
    data = {"feature_vector": x, "score": score}
    logging.info(data)
    response = requests.post(f"{ENDPOINT}/prediction", json=data)
    logging.info(response.json())
    return response.json()


def get_model_info():
    response = requests.get(f"{ENDPOINT}/model_information")

    return response.json()


if __name__ == '__main__':
    X_test = pd.read_csv("./anomaly_detection/Datasets/test.csv")
    for row in X_test.itertuples():
        predict([row.mean, row.sd])
    get_model_info()
