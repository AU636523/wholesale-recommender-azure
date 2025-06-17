from dash import html, dcc
import dash_bootstrap_components as dbc


layout = dbc.Container(fluid=True, children=[
    
    dbc.Row([
        dbc.Col(width=3, children=[
            html.H4("🔍 Input"),

            dcc.Interval(id="init-trigger", interval=100, n_intervals=0, max_intervals=1),  # trigger on page load
            html.Label("Customer ID"),
            
            dcc.Dropdown(
                id="customer-id",
                options=[],
                placeholder="Select or type Customer ID",
                searchable=True,
                style={"width": "100%"}
            ),
            html.Br(),
            html.Label("Delivery Date"),
            dcc.DatePickerSingle(
                id='delivery-date',
                placeholder='Select Delivery Date',
                style={"width": "100%"}
            ),
            html.Br(), html.Br(),
            dbc.Button("Get Recommendations", id="search-button", color="primary", className="w-100"),
        ], style={"background-color": "#f8f9fa", "padding": "20px", "height": "100vh"}),

        dbc.Col(width=9, children=[
            html.H3("🛍️ Recommendations", className="mt-3"),

            dbc.Card([
                dbc.CardHeader("🔥 Popular Items for Delivery Date"),
                dbc.CardBody(html.Ul(id="popular-items"))
            ], className="mb-4"),

            dbc.Card([
                dbc.CardHeader("⭐ Based on Your History, You Might Like"),
                dbc.CardBody(html.Ul(id="personal-recs"))
            ], className="mb-4"),

            dbc.Card([
                dbc.CardHeader("🧑‍🤝‍🧑 Similar Customers Also Bought"),
                dbc.CardBody(html.Ul(id="similar-customer-recs"))
            ])
        ])
    ])
])
