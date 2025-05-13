
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the trained model
model = joblib.load("rf_model.joblib")

# Define input format using Pydantic
class InputData(BaseModel):
    data: list  # expects a list like [Pclass, Age, Fare]

# Create FastAPI app
app = FastAPI()

@app.post("/predict")
def predict(input_data: InputData):
    input_array = np.array([input_data.data])
    prediction = model.predict(input_array)
    return {"prediction": prediction.tolist()}
# test
# Test update: Triggering CI/CD on GitHub push
