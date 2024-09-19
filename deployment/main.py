import pandas as pd
import pickle
from fastapi import FastAPI

from fastapi.encoders import jsonable_encoder
import uvicorn
from pydantic import BaseModel


app = FastAPI()

COLUMNS_PATH = "../src/categorias_ohe.pkl"
with open(COLUMNS_PATH, 'rb') as handle:
    ohe_tr = pickle.load(handle)

BINS1_PATH = "../src/saved_bins/ph_bins.pkl"
with open(BINS1_PATH, 'rb') as handle:
    ph_bins = pickle.load(handle)

BINS2_PATH = "../src/saved_bins/Trihalomethanes_bins.pkl"
with open(BINS2_PATH, 'rb') as handle:
    Trihalomethanes_bins = pickle.load(handle)

BINS3_PATH = "../src/saved_bins/Sulfate_bins.pkl"
with open(BINS3_PATH, 'rb') as handle:
    Sulfate_bins = pickle.load(handle)

MODEL_PATH = "../src/model/rf.pkl"
model = pickle.load(open(MODEL_PATH, 'rb'))

class Answer(BaseModel):
    ph: float
    Hardness: float
    Solids: float
    Chloramines: float
    Sulfate: float
    Conductivity: float
    Organic_carbon: float
    Trihalomethanes: float
    Turbidity: float

@app.get("/")
async def root():
    return {"message":"Model Deployment Bootcamp"}

@app.post("/prediction")
def predict_water_potability(answer:Answer):
    answer_dict = jsonable_encoder(answer)

    for key, value in answer_dict.items():
        answer_dict[key] = [value]

    single_instance = pd.DataFrame.from_dict(answer_dict) 

    single_instance["ph_discretized"] = pd.cut(single_instance["ph"],bins = ph_bins,include_lowest = True)
    single_instance["Trihalomethanes_ph_discretized"] = pd.cut(single_instance["Trihalomethanes"],bins = Trihalomethanes_bins,include_lowest = True)
    single_instance["Sulfate_discretized"] = pd.cut(single_instance["Sulfate"],bins = Sulfate_bins,include_lowest = True)
    
    single_instance = single_instance.drop(columns=["ph","Trihalomethanes","Sulfate"],axis=1)
    
    single_instance_ohe = pd.get_dummies(single_instance).reindex(columns = ohe_tr).fillna(0)

    prediction = model.predict(single_instance_ohe)
    
    score = "no" if int(prediction[0]) == 0 else "yes"
 
    response = {"Potable Water: ": score}

    return response


if __name__ == "__main__":

    uvicorn.run(app, host="127.0.0.1", port=8000)