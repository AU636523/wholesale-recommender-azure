import os

from dash import Input, Output, State, html
from dash.exceptions import PreventUpdate
from app import app  # Import the Dash instance
from db_utils import load_customers

ROOT_PATH = "c:/sparkdata/wholesale-recommender"
MODEL_OUTPUT_PATH = os.path.join(ROOT_PATH, "results")

print("⚡ Callbacks module loaded")

@app.callback(
    Output('customer-id', 'options'),
    Input('init-trigger', 'n_intervals')
)
def update_customer_options(n):
    return load_customers()

@app.callback(
    Output("popular-items", "children"),
    Output("personal-recs", "children"),
    Output("similar-customer-recs", "children"),
    Input("search-button", "n_clicks"),
    State("customer-id", "value"),
    State("delivery-date", "date"),
)

def make_list(products : list[str]) -> list[str]:  
    return [html.Li(p) for p in products]

def dummy_list(title):
    return [html.Li(f"{title} Product {i+1}") for i in range(3)]

def get_popular_items_for_month(month):
    # Load from parquet 


def update_recommendations(n_clicks, customer_id, delivery_date):
    if not n_clicks or not customer_id or not delivery_date:
        raise PreventUpdate

    return (
        dummy_list("Popular"),
        dummy_list("Personalized"),
        dummy_list("Similar")
    )

