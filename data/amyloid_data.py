import pandas as pd

from app import cache
from utils.constants import TIMEOUT


@cache.memoize(timeout=TIMEOUT)
def query_data():
    # This could be an expensive data querying step
    amyloid_raw = pd.read_csv("./data/amyloid_data.csv")
    return amyloid_raw.to_json(date_format='iso', orient='split')

def dataframe():    
    return pd.read_json(query_data(), orient='split')


@cache.memoize(timeout=TIMEOUT)
def query_pos_data():
    # This could be an expensive data querying step
    amyloid_raw = pd.read_csv("./data/amyloid_data_pos.csv")
    return amyloid_raw.to_json(date_format='iso', orient='split')

def pos_dataframe():    
    return pd.read_json(query_pos_data(), orient='split')