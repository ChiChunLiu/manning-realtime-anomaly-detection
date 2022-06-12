from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_client import make_asgi_app, Counter, Histogram
import numpy as np
import joblib
import time

app = FastAPI()
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

model = joblib.load('./model.joblib')

counter_predict = Counter('predict', 'count predict call count')
counter_get_model_info = Counter('get_model_info', 'get_model_info call count')
histogram_output = Histogram('prediction_output', 'prediction output')
histogram_scores = Histogram('prediction_score', 'prediction score')
histogram_latency = Histogram('prediction_latency', 'prediction latency')

class Input(BaseModel):
    feature_vector: List[float]
    score: Optional[bool]


@app.post("/prediction")
async def predict(input: Input):
    time_start = time.perf_counter()
    response = {}
    feature_reshaped = np.array(input.feature_vector).reshape(1, -1)
    response['is_inliner'] = int(model.predict(feature_reshaped)[0])
    histogram_output.observe(response['is_inliner'])
    if input.score:
        response['anomaly_score'] = round(model.score_samples(feature_reshaped)[0], 4)
        histogram_scores.observe(response['anomaly_score'])
    counter_predict.inc()
    time_end = time.perf_counter()
    time_delta = time_end - time_start
    histogram_latency.observe(time_delta)
    return response

@app.get("/model_information")
async def get_model_info():
    counter_get_model_info.inc()
    return model.get_params()

