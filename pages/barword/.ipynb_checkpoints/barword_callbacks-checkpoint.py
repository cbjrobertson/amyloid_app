from dash.dependencies import Input, Output

import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import pandas as pd

from app import app
from data.amyloid_data import dataframe
from .barword_constants import CAT_MAP

# Logging and traceback
import logging
import traceback

# Gets or creates a logger
logger = logging.getLogger(__name__)

# set log level
logger.setLevel(logging.DEBUG)

# define file handler and set formatter
log_fp =  "./pages/barword/barword_log.txt"
file_handler = logging.FileHandler(log_fp)
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_handler)

@app.callback(
    Output("barword", "figure"),
    [
        Input("barword-pos", "value"),
        Input("barword-topn", "value"),
        Input("barword-target", "value"),
    ],
)
def make_barword(pos,
                  topn,
                  target,
                 ):
    # Load data
    df = dataframe()
    
    #cast to list
    if isinstance(pos,str):
        pos = [pos]
    logger.warning(f"target was {target}\n>>>>>>>>>>\n\n")
    # subset
    if len(pos) == 1 and pos[0] == "":
        df = df.loc[(df.target == target),:].copy()
        mean_cols = ["target","token"]
    else:
        df = df.loc[(df.alt_pos.isin(pos)) & (df.target == target),:].copy()
        mean_cols = ["target","alt_pos","token"]
    #aggregate
    dz = df\
        .groupby(mean_cols)\
        .agg(mean_weight=("weight","mean"))\
        .sort_values(by="mean_weight",ascending=False)\
        .groupby(["token"])\
        .head(topn)\
        .reset_index(drop=False)
    dz["direction"] = "Positive weights"
    dz = dz.iloc[:topn,:]
    
    dy = df\
        .groupby(mean_cols)\
        .agg(mean_weight=("weight","mean"))\
        .sort_values(by="mean_weight",ascending=True)\
        .groupby(["token"])\
        .head(topn)\
        .reset_index(drop=False)
    dy["direction"] = "Negative weights"
    dy = dy.iloc[:topn,:]
    
    #combine
    dx = pd.concat([dz,dy],axis=0)
    
    if len(pos) == 1 and pos[0] == "":
        x = "token"
    else:
        dx["comb_token"] = dx.apply(lambda S: f"{S.alt_pos}: {S.token}", axis=1)
        x = "comb_token"
    
    #title
    title = f"Top and bottom {topn} words for within the selected POS tags for {CAT_MAP[target]} people"
    #return fig
    fig = px.bar(dx,
                 x=x,
                 y="mean_weight",
                 facet_row="direction",
                 color="direction",
                 category_orders={"direction": ["Positive weights", "Negative weights"]},
                 facet_row_spacing=0.08
                )\
    .update_layout(autosize=True,height=1000)\
    .update_xaxes(matches=None)\
    .for_each_xaxis(lambda xaxis: xaxis.update(showticklabels=True))\
    .update_layout(title=dict(text=f'<b>{title}</b>',
                              font=dict(size=20
                                       )
                             ),
                   legend=dict(
                       font=dict(size=14),
                       title=dict(text="Weight direction", font=dict(size=16))
                   )
                  )
    return fig