# imports
import os

import pandas as pd
from fastapi import FastAPI

# path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE_DIR = os.path.join(BASE_DIR, 'cache')
dataset = os.path.join(CACHE_DIR, 'movies-boxoffice-dataset-cleaned.csv')

# API
app = FastAPI()

# root


@app.get('/')
def read_root():
    return {"hello": "world", "goto": "/box-office"}

# Data as API


@app.get("/box-office")
def box_office_data():
    df = pd.read_csv(dataset)
    return df.to_dict('Rank')
