import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output

from app import app

from utils import constants as const 

from pages.scatter_3d import scatter_3d
from pages.barword import barword
from pages.barpos import barpos

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == const.scatter_3d_page_location:
        return scatter_3d.layout
    elif pathname == const.barword_page_location:
        return barword.layout
    elif pathname == const.barpos_page_location:
        return barpos.layout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )