
from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

model = pickle.load(open("models/model.pkl","rb"))

@app.get("/predict")
def predict(x1: float, x2: float, x3: float):

    prediction = model.predict([[x1,x2,x3]])

    return {"prediction": int(prediction[0])}
