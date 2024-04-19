from fastapi import FastAPI

import requests

app = FastAPI()

@app.get("/")
def root():
    URL = "http://bigdata.kepco.co.kr/openapi/v1/powerUsage/industryType.do?year=2020&month=11&metroCd=11&cityCd=12&apiKey=0A1vJmnneiyX5MA432Vw0ZNicz9NOLcICnnpuYau0A1vJmnneiyX5MA432Vw0ZNicz9NOLcICnnpuYau&returnType=json"

    contents = requests.get(URL).text

    return { "message": "Hello Root!" }

@app.get("/home")
def home():
    return {"message":"Home!"}