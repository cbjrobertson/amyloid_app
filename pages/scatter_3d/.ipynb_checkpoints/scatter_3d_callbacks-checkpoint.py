from dash.dependencies import Input, Output

import plotly.graph_objs as go
import plotly.express as px
import numpy as np

from app import app
from data.amyloid_data import dataframe
from .scatter_3d_constants import NAME_MAP, HOVER_MAP, CAT_MAP

def _norm_data(data,smooth):
    return np.exp(smooth*(data - np.min(data)) / (np.max(data) - np.min(data)))

@app.callback(
    Output("3d_scatter", "figure"),
    [
        Input("3d_scatter-pos", "value"),
        Input("3d_scatter-topn", "value"),
        Input("3d_scatter-smooth", "value"),
        Input("3d_scatter-max_size", "value"),
        Input("3d_scatter-text_size", "value")
    ],
)
def make_3d_scatter(
    pos,
    topn,
    smooth,
    max_size,
    text_size,
    symbol=None
):
    pdat = dataframe()
    if pos is not None:
        if isinstance(pos,str):
            pos = [pos]
        if len(pos) == 1:
            pos = pos[0]
            pdat = pdat.loc[pdat.alt_pos == pos,:].copy()
            pdat["weight_norm"] = _norm_data(pdat.weight.tolist(),smooth)
            symbol = None
            make_comb = False
        elif len(pos) > 1:
            pdat = pdat.loc[pdat.alt_pos.isin(pos),:].copy()
            pdat["weight_norm"] = _norm_data(pdat.weight.tolist(),smooth)
            symbol="alt_pos"
            make_comb = True
    if topn:
        pdat = pdat.sort_values(by="weight",ascending=False).\
            groupby(["label","hash_id"]).\
            head(topn).\
            sort_values(by=["weight"],ascending=False).\
            reset_index(drop=True,inplace=False)
        
    title="3D scatter in RoBERTa output layer vector space, weighted (dot size) by LIME weights"
     # make friendly labels
    if make_comb:
        comb_map = {f"{cat}, {pos}":f"{cat_val}: {val}" for cat,cat_val in CAT_MAP.items() for pos,val in NAME_MAP.items()}
    else:
        comb_map = {**NAME_MAP,**{"AMYLOID_NEG": "Negative", "AMYLOID_POS": "Positive"}}
    
    #make fig
    fig = px.scatter_3d(
        pdat,
        x="X",
        y="Y",
        z="Z",
        text="lemma",
        size="weight_norm",
        color="label",
        symbol=symbol,
        size_max=max_size,
        opacity=.6,
        category_orders={"label": ["AMYLOID_NEG", "AMYLOID_POS"]},
        hover_data=HOVER_MAP)\
    .for_each_trace(lambda t: t.update(textfont_color=t.marker.color, textposition='top center'))\
    .for_each_trace(lambda t: t.update(name = comb_map[t.name],
                                  legendgroup = comb_map[t.name],
                                  hovertemplate = t.hovertemplate.replace(t.name, comb_map[t.name])
                                 )
                      )\
    .update_layout(autosize=True)\
    .update_layout(
        font=dict(
            size=text_size,  # Set the font size here
        ),
    )\
    .update_layout(uniformtext_minsize=text_size,uniformtext_mode="show")\
    .update_layout(title=dict(text=f'<b>{title}</b>',
                              x=0.5,
                              y=0.95,
                              font=dict(size=20
                                       )
                             ),
                   legend=dict(
                       font=dict(size=14),
                       title=dict(text="Amyloid status", font=dict(size=16))
                   )
                  )\
    .update_layout(scene=dict(
                   xaxis=dict(showticklabels=False),
                   yaxis=dict(showticklabels=False),
                   zaxis=dict(showticklabels=False),
                   xaxis_title='',
                   yaxis_title='',
                   zaxis_title='')
                  )
    return fig