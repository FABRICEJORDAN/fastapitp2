# main.py
from typing import List
from fastapi import FastAPI
import pandas as pd
import json
from typing import Union, Optional

app = FastAPI()

impression = pd.read_csv('impressions.csv',sep=",")
clic = pd.read_csv('clics.csv',sep=",")
achat = pd.read_csv('achats.csv',sep=",")
fusion1 = pd.merge(impression, clic, on='cookie_id')
fusion2 = pd.merge(fusion1, achat, on='cookie_id')

def parse_csv(fusion2):
    res = fusion2.to_json(orient="records")
    parsed = json.loads(res)
    return parsed   


@app.get("/get_data")
def load_questions():
    return parse_csv(fusion2)

@app.get("/get_data_campaign/{campaign_id}")
async def read_item(campaign_id: int):
     
    resultat = fusion2[(fusion2.campaign_id == campaign_id)]

    return parse_csv(resultat)