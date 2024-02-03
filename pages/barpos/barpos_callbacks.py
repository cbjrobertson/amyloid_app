from dash.dependencies import Input, Output

import plotly.express as px

from app import app
from data.amyloid_data import pos_dataframe
from .barpos_constants import NAME_MAP, AGG_MAP


@app.callback(
    Output("barpos", "figure"),
    [
        Input("barpos-y_var", "value"),
    ],
)
def make_barpos(
    y_var
):
    # Load data
    df = pos_dataframe() #dataframe()
    df = df.sort_values(by=["label",y_var],ascending=False)
    df["alt_pos"] = df.alt_pos.apply(lambda pos: NAME_MAP[pos])
    
    #title
    title = f"Word type ranked by: {AGG_MAP[y_var]}"
    _map = {**{"0-low-CTR": "Low-CTR", "1-high-CTR": "High CTR"},**{"alt_pos": "Word type", "weight_prod": "Product impact score", "weight_mean": "Mean of impact score", "weight_sum": "Sum of impact score"}}

    #return fig
    fig = px.bar(df,
                 x="alt_pos",
                 y=y_var,
                 facet_row="label",
                 color="label",
                 category_orders={"label": ["1-high-CTR", "0-low-CTR"]},
                 facet_row_spacing=0.125,
                 labels=_map
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
                       title=dict(text="CTR", font=dict(size=16))
                   )
                  )\
    .for_each_trace(lambda t: t.update(name = _map[t.name],
                                       legendgroup = _map[t.name]))
                    
    return fig