import dash_bootstrap_components as dbc
from dash import dcc 
from dash import html

from data.amyloid_data import dataframe
from .scatter_3d_constants import NAME_MAP
from components.table import make_dash_table


controls = dbc.Card(
    dbc.Row(
            [
                dbc.Col(
                dbc.FormGroup(
                    [
                        dbc.Label("Part of speech"),
                        dcc.Dropdown(
                            id="3d_scatter-pos",
                            options=[
                                {"label": NAME_MAP[val], "value": val} for val in sorted(list(set(dataframe().alt_pos)))
                            ],
                            value=["VERB"],
                            multi=True
                        ),
                    ]
                ),
                md=3),
                
                dbc.Col(
                    dbc.FormGroup(
                        [
                            dbc.Label("Top N examples"),
                            dcc.Slider(1,20,1,
                                       value=3,
                                       id='3d_scatter-topn'
                                      )
                        ]
                    ),
                md=3),
                
                dbc.Col(
                    dbc.FormGroup(
                        [
                            dbc.Label("Smoothing factor (LIME weights)"),
                            dcc.Slider(1,10,1,
                                       value=5,
                                       id='3d_scatter-smooth'
                                      )
                        ]
                    ),
                md=2),
                
                dbc.Col(
                dbc.FormGroup(
                    [
                        dbc.Label("Max point size"),
                        dcc.Slider(0,150,25,
                                   value=75,
                                   id='3d_scatter-max_size'
                                  )
                    ]
                ),
                md=2),
                
                dbc.Col(
                dbc.FormGroup(
                    [
                        dbc.Label("Text size"),
                        dcc.Slider(10,50,2,
                                   value=12,
                                   id='3d_scatter-text_size'
                                  )
                    ]
                ),
                md=2),
            ],
    ),
    body=True,
)

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="3d_scatter",
                                 style={"height": "80vh"}), 
                        md=12,
                        ),
            ],
            align="center",
        ),
        dbc.Row(
            dbc.Col(controls, md=12),
            align="center",
        )
    ],
    fluid=True,
    style={"height": "100vh"}
)