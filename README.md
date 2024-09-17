# Model Deployment with FastAPI
Project made for Data Science & MLOPS Bootcamp from Edvai

## Project description
In this project I built a Random Forest Classification model that predicts wether the water is potable or not based on the next 9 variables:
- **ph**
- **Hardness**
- **Solids**
- **Chloramines**
- **Sulfate**
- **Conductivity**
- **Organic_carbon**
- **Trihalomethanes**
- **Turbidity**
  
This model is deployed with FastAPI on a local server and it uses Uvicorn to allow the API to comunicate with the server.


## Methods used
- Data visualization
- Data preparation
- Model training
- Model evaluation
- Model deployment with API 

## Technologies
- <ins>**Data Preparation**</ins>: funpymodeling and pandas.
- <ins>**Model Training**</ins>: sklearn.
- <ins>**Data Visualization**</ins>: seaborn, matplotlib and yellowbrick.
- <ins>**API**</ins>: FastAPI, uvicorn, pydantic, and requests.
- <ins>**Others**</ins>: numpy and pickles.

## Installation
1. Clone the repository:  
`gh repo clone https://github.com/ITRoselloSignoris/Data-Science-Model-Deployment-`

2. Install the necessary libraries inside the requirements.txt:  
`pip install -r requirements.txt`

3. Run the "main.py" file to comunicate with the web server:  
`python main.py`

4. Run the "call_api.py" file to call the api:   
`python call_api.py` 


## Results
### Confusion Matrix

### ROC curve

## To-Do list
- [ ] Make and save model's validation error plots
- [ ] Add ROC curve and Confusion Matrix plots in the README.md file
- [ ] Add information about the process of the doing the model (data preparation, model chosen, parameters, etc)