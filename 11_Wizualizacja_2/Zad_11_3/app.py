# Standardowe biblioteki
import os
import pandas as pd
import datetime as dt

# Dash
import dash
from dash import dcc, html

from dash.dependencies import Input, Output
import dash_auth

# Plotly
import plotly.graph_objects as go

# Twoje moduły z zakładkami
import tab1
import tab2
import tab3

# ---------------------------
# Klasa DB i wczytywanie danych
# ---------------------------
class db:
    def __init__(self):
        self.transactions = self.transaction_init()
        self.cc = self.load_csv("country_codes.csv")
        self.customers = self.load_csv("customers.csv")
        path3 = os.path.join(os.path.dirname(__file__), "db", "prod_cat_info.csv")
        self.prod_info = pd.read_csv(path3)
        self.merged = None
    
    def load_csv(self, filename):
        path = os.path.join(os.path.dirname(__file__), "db", filename)
        df = pd.read_csv(path)
        df = df.drop(columns=["Unnamed: 0"], errors="ignore")
        return df

    def transaction_init(self):
        def convert_dates(x):
            try:
                return dt.datetime.strptime(x,'%d-%m-%Y')
            except:
                return dt.datetime.strptime(x,'%d/%m/%Y')

        transactions = []
        src = os.path.join(os.path.dirname(__file__), "db", "transactions")
        for filename in os.listdir(src):
            filepath = os.path.join(src, filename)
            df = pd.read_csv(filepath, index_col=0)
            if 'tran_date' in df.columns:
                df['tran_date'] = df['tran_date'].apply(convert_dates)
            transactions.append(df)

        if transactions:
            return pd.concat(transactions, ignore_index=True)
        else:
            return pd.DataFrame()

    def merge(self):
        df = self.transactions.join(
            self.prod_info.drop_duplicates(subset=['prod_cat_code'])
            .set_index('prod_cat_code')['prod_cat'],
            on='prod_cat_code',
            how='left'
        )

        df = df.join(
            self.prod_info.drop_duplicates(subset=['prod_sub_cat_code'])
            .set_index('prod_sub_cat_code')['prod_subcat'],
            on='prod_subcat_code',
            how='left'
        )

        df = df.join(
            self.customers.join(self.cc, on='country_code')
            .set_index('customer_Id'),
            on='cust_id'
        )

        self.merged = df
        return df

# Tworzymy obiekt i scalamy
db_obj = db()
merged_df = db_obj.merge()


# Konfiguracja Dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
USERNAME_PASSWORD = [['tomek','tomek']]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)
auth = dash_auth.BasicAuth(app, USERNAME_PASSWORD)


# Layout z Tabs

app.layout = html.Div([
    dcc.Tabs(id='tabs', value='tab-1', children=[
        dcc.Tab(label='Sprzedaż globalna', value='tab-1'),
        dcc.Tab(label='Produkty', value='tab-2'),
        dcc.Tab(label='Kanały sprzedaży', value='tab-3') 
    ]),
    html.Div(id='tabs-content')
])


# Callback renderujący zakładki

@app.callback(Output('tabs-content', 'children'), [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return tab1.render_tab(merged_df)
    elif tab == 'tab-2':
        return tab2.render_tab(merged_df)
    elif tab == 'tab-3':
        return tab3.render_tab(merged_df)

# Funkcja dla wykresu słupkowego w tab1
# ---------------------------
def tab1_bar_sales(start_date, end_date):
    truncated = merged_df[(merged_df['tran_date'] >= start_date) & (merged_df['tran_date'] <= end_date)]
    grouped = truncated[truncated['total_amt'] > 0].groupby([pd.Grouper(key='tran_date', freq='M'), 'Store_type'])['total_amt'].sum().round(2).unstack()

    traces = []
    for col in grouped.columns:
        traces.append(go.Bar(
            x=grouped.index,
            y=grouped[col],
            name=col,
            hoverinfo='text',
            hovertext=[f'{y/1e3:.2f}k' for y in grouped[col].values]
        ))

    fig = go.Figure(data=traces, layout=go.Layout(title='Przychody', barmode='stack', legend=dict(x=0, y=-0.5)))
    return fig


# Callbacki tab1

@app.callback(
    Output('bar-sales', 'figure'),
    [Input('sales-range', 'start_date'), Input('sales-range', 'end_date')]
)
def update_bar_sales(start_date, end_date):
    return tab1_bar_sales(start_date, end_date)

@app.callback(
    Output('choropleth-sales', 'figure'),
    [Input('sales-range', 'start_date'), Input('sales-range', 'end_date')]
)
def tab1_choropleth_sales(start_date, end_date):
    truncated = merged_df[(merged_df['tran_date'] >= start_date) & (merged_df['tran_date'] <= end_date)]
    grouped = truncated[truncated['total_amt'] > 0].groupby('country')['total_amt'].sum().round(2)

    trace0 = go.Choropleth(
        colorscale='Viridis',
        reversescale=True,
        locations=grouped.index,
        locationmode='country names',
        z=grouped.values,
        colorbar=dict(title='Sales')
    )

    fig = go.Figure(data=[trace0], layout=go.Layout(title='Mapa', geo=dict(showframe=False, projection={'type':'natural earth'})))
    return fig


# Callbacki tab2

@app.callback(
    Output('barh-prod-subcat', 'figure'),
    [Input('prod_dropdown', 'value')]
)
def tab2_barh_prod_subcat(chosen_cat):
    grouped = merged_df[(merged_df['total_amt']>0) & (merged_df['prod_cat']==chosen_cat)].pivot_table(
        index='prod_subcat', columns='Gender', values='total_amt', aggfunc='sum'
    ).assign(_sum=lambda x: x['F'] + x['M']).sort_values(by='_sum').round(2)

    traces = []
    for col in ['F','M']:
        traces.append(go.Bar(x=grouped[col], y=grouped.index, orientation='h', name=col))

    fig = go.Figure(data=traces, layout=go.Layout(barmode='stack', margin={'t':20}))
    return fig

# Callbacki tab3
@app.callback(
    Output('sales_by_period', 'figure'),
    [Input('store_type_dropdown', 'value'),
     Input('time_aggregation', 'value')]
)
def tab_update_sales_by_period(selected_store, agg):
    df_filtered = merged_df[merged_df['Store_type'] == selected_store]

    if agg == 'weekday':
        grouped = df_filtered.groupby('weekday')['total_amt'].sum().reindex([
            'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
        x_axis = grouped.index
    elif agg == 'month':
        grouped = df_filtered.groupby(df_filtered['tran_date'].dt.to_period('M'))['total_amt'].sum()
        grouped.index = grouped.index.to_timestamp()
        x_axis = grouped.index
    elif agg == 'quarter':
        grouped = df_filtered.groupby(df_filtered['tran_date'].dt.to_period('Q'))['total_amt'].sum()
        grouped.index = grouped.index.to_timestamp()
        x_axis = grouped.index
    elif agg == 'year':
        grouped = df_filtered.groupby(df_filtered['tran_date'].dt.year)['total_amt'].sum()
        x_axis = grouped.index

    fig = go.Figure(data=[go.Bar(x=x_axis, y=grouped.values, name='Sprzedaż')])
    fig.update_layout(title=f'Sprzedaż ({agg}) - {selected_store}',
                      xaxis_title=agg.capitalize(),
                      yaxis_title='Suma sprzedaży')
    return fig


"""
# Callback do wykresu sprzedaży w poszczególne dni tygodnia
@app.callback(
    Output('weekday_sales', 'figure'),
    [Input('store_type_dropdown', 'value')]
)
def update_weekday_sales(selected_store):
    df_filtered = merged_df[merged_df['Store_type'] == selected_store]
    grouped = df_filtered.groupby('weekday')['total_amt'].sum().reindex([
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
    ])

    fig = go.Figure(data=[
        go.Bar(x=grouped.index, y=grouped.values, name='Sprzedaż')
    ])
    fig.update_layout(title=f'Sprzedaż w zależności od dnia tygodnia: {selected_store}')
    return fig

# Callback do analizy klientów w wybranym kanale
@app.callback(
    Output('customer_info', 'figure'),
    [Input('store_type_dropdown', 'value')]
)
def update_customer_info(selected_store):
    df_filtered = merged_df[merged_df['Store_type'] == selected_store]
    grouped_gender = df_filtered.groupby('Gender')['total_amt'].sum()

    fig = go.Figure(data=[
        go.Pie(labels=grouped_gender.index, values=grouped_gender.values)
    ])
    fig.update_layout(title=f'Skład klientów w kanale: {selected_store}')
    return fig





"""

# Uruchomienie aplikacji

if __name__ == '__main__':
    app.run(debug=True)
