from dash import dcc, html
import plotly.graph_objects as go
import pandas as pd

def render_tab(df):
    # Dodaj kolumnę z dniami tygodnia i okresami
    df['weekday'] = df['tran_date'].dt.day_name()
    df['month'] = df['tran_date'].dt.to_period('M').dt.to_timestamp()
    df['quarter'] = df['tran_date'].dt.to_period('Q').dt.to_timestamp()
    df['year'] = df['tran_date'].dt.year

    store_types = df['Store_type'].dropna().unique()

    layout = html.Div([
        html.H1('Kanały sprzedaży', style={'text-align':'center'}),

        # Dropdown do wyboru kanału sprzedaży
        html.Div([
            html.Label('Wybierz kanał sprzedaży:'),
            dcc.Dropdown(
                id='store_type_dropdown',
                options=[{'label': st, 'value': st} for st in store_types],
                value=store_types[0] if len(store_types) > 0 else None
            )
        ], style={'width':'40%', 'margin':'auto'}),

        # RadioItems do wyboru agregacji czasowej
        html.Div([
            html.Label('Agregacja danych:'),
            dcc.RadioItems(
                id='time_aggregation',
                options=[
                    {'label':'Dni tygodnia', 'value':'weekday'},
                    {'label':'Miesięcznie', 'value':'month'},
                    {'label':'Kwartalnie', 'value':'quarter'},
                    {'label':'Rocznie', 'value':'year'}
                ],
                value='weekday',
                labelStyle={'display':'inline-block', 'margin-right':'20px'}
            )
        ], style={'width':'60%', 'margin':'20px auto', 'text-align':'center'}),

        # Wykres sprzedaży
        html.Div([
            dcc.Graph(id='sales_by_period')
        ], style={'width':'80%', 'margin':'auto'}),

        # Dodatkowe informacje o klientach
        html.Div([
            dcc.Graph(id='customer_info')
        ], style={'width':'80%', 'margin':'auto', 'marginTop':'50px'})
    ])

    return layout
