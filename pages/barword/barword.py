import dash_bootstrap_components as dbc
from dash import dcc 
from dash import html
import dash_daq as daq

from data.amyloid_data import dataframe
from .barword_constants import NAME_MAP, CAT_MAP
from components.table import make_dash_table

controls = dbc.Card(
    dbc.Row(
            [
                dbc.Col(
                dbc.FormGroup(
                    [
                        dbc.Label("Word type"),
                        dcc.Dropdown(
                            id="barword-pos",
                            options= [{"label": "All", "value": ""}] + [
                                {"label": NAME_MAP[val], "value": val} for val in sorted(list(set(dataframe().alt_pos)))
                            ],
                            value="",
                            multi=True
                        ),
                    ]
                ),
                md=3),
                
                dbc.Col(
                    dbc.FormGroup(
                        [
                            dbc.Label("Number of words"),
                            dcc.Slider(0,40,5,
                                       value=20,
                                       id='barword-topn'
                                      )
                        ]
                    ),
                md=3),
                
                dbc.Col(
                    dbc.FormGroup(
                        [
                            dbc.Label("CTR category"),
                            dcc.Dropdown(id='barword-target',
                                         options = [
                                             {"label": CAT_MAP[key], "value": key} for key in CAT_MAP
                                         ],
                                         value="1-high-CTR"
                                      )
                        ]
                    ),
                md=2),
                
                dbc.Col(
                    dbc.FormGroup(
                        [
                            dbc.Label("Aggregation method"),
                            dcc.Dropdown(id='barword-agg_meth',
                                         options = [
                                             {"label": "Mean", "value": "mean"}, 
                                             {"label": "Sum", "value": "sum"},
                                         ],
                                         value="mean"
                                      )
                        ]
                    ),
                md=2)
                
            ],
    ),
    body=True,
)

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="barword"), 
                        md=12,
                        style={"height": "80vh"}),
            ],
            align="center",
            style={"height": "80vh"}
        ),
        dbc.Row(
            dbc.Col(controls, md=12),
            align="center",
        )
    ],
    fluid=True,
    style={"height": "100vh"}
)