import dash_bootstrap_components as dbc
from dash import dcc 
from dash import html
import dash_daq as daq

from data.amyloid_data import pos_dataframe
from .barpos_constants import AGG_MAP


controls = dbc.Card(
    dbc.Row(
            [
                dbc.Col(
                dbc.FormGroup(
                    [
                        dbc.Label("Word type"),
                        dcc.Dropdown(
                            id="barpos-y_var",
                            options=  [
                                {"label": val, "value": key} for key,val in AGG_MAP.items()
                            ],
                            value="weight_prod",
                            multi=False
                        ),
                    ]
                ),
                md=3),
            ],
    ),
    body=True,
)

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="barpos"), 
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