
# Standardowe biblioteki
import os
import pandas as pd
import datetime as dt

# Dash
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Plotly (jeśli potrzebujesz go do wykresów)
import plotly.graph_objects as go


import tab1
import tab2

import dash as dash_auth

class db:
    def __init__(self):
        self.transactions = self.transaction_init()
        self.cc= self.load_csv("country_codes.csv")
        self.customers = self.load_csv("customers.csv")
        path3 = os.path.join(os.path.dirname(__file__), "db", "prod_cat_info.csv")
        self.prod_info= pd.read_csv(path3)
        self.merged = None  # domyślnie brak scalonego df
    
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
        #src = r'db\transactions'
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
        # scalanie transactions z prod_info i customers
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
print(merged_df.head())

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([],
                    style={'height':'100%'})

app.layout = html.Div([html.Div([],style={'width':'80%','margin':'auto'})],
                    style={'height':'100%'})

app.layout = html.Div([
    dcc.Tabs(id='tabs', value='tab-1', children=[
        dcc.Tab(label='Sprzedaż globalna', value='tab-1'),
        dcc.Tab(label='Produkty', value='tab-2')
    ]),
    html.Div(id='tabs-content')
])

""" 
[dcc.Tabs(id='tabs',value='tab-1',children=[
                            dcc.Tab(label='Sprzedaż globalna',value='tab-1'),
                            dcc.Tab(label='Produkty',value='tab-2')
                            ]),
                            html.Div(id='tabs-content')]


"""


def tab1_bar_sales(start_date,end_date):

    truncated = df.merged[(df.merged['tran_date']>=start_date)&(df.merged['tran_date']<=end_date)]
    grouped = truncated[truncated['total_amt']>0].groupby([pd.Grouper(key='tran_date',freq='M'),'Store_type'])['total_amt'].sum().round(2).unstack()

    traces = []
    for col in grouped.columns:
        traces.append(go.Bar(x=grouped.index,y=grouped[col],name=col,hoverinfo='text',
        hovertext=[f'{y/1e3:.2f}k' for y in grouped[col].values]))

    data = traces
    fig = go.Figure(data=data,layout=go.Layout(title='Przychody',barmode='stack',legend=dict(x=0,y=-0.5)))

    return fig

if __name__ == '__main__':
    app.run(debug=True)


@app.callback(Output('tabs-content','children'),[Input('tabs','value')])
def render_content(tab):

    if tab == 'tab-1':
        return tab1.render_tab(df.merged)
    elif tab == 'tab-2':
        return tab2.render_tab(df.merged)

## tab1 callbacks
@app.callback(
    Output('id-wyjscia', 'figure'),
    [Input('sales-range','start_date'),
     Input('sales-range','end_date')]
)

@app.callback(
    Output('bar-sales', 'figure'),
    [Input('sales-range','start_date'),
     Input('sales-range','end_date')]
)
def update_bar_sales(start_date, end_date):
    return tab1_bar_sales(start_date, end_date)


@app.callback(Output('choropleth-sales','figure'),
            [Input('sales-range','start_date'),Input('sales-range','end_date')])
def tab1_choropleth_sales(start_date,end_date):

    truncated = df.merged[(df.merged['tran_date']>=start_date)&(df.merged['tran_date']<=end_date)]
    grouped = truncated[truncated['total_amt']>0].groupby('country')['total_amt'].sum().round(2)

    trace0 = go.Choropleth(colorscale='Viridis',reversescale=True,
                            locations=grouped.index,locationmode='country names',
                            z = grouped.values, colorbar=dict(title='Sales'))
    data = [trace0]
    fig = go.Figure(data=data,layout=go.Layout(title='Mapa',geo=dict(showframe=False,projection={'type':'natural earth'})))

    return fig


## tab2 callbacks
@app.callback(Output('barh-prod-subcat','figure'),
            [Input('prod_dropdown','value')])
def tab2_barh_prod_subcat(chosen_cat):

    grouped = df.merged[(df.merged['total_amt']>0)&(df.merged['prod_cat']==chosen_cat)].pivot_table(index='prod_subcat',columns='Gender',values='total_amt',aggfunc='sum').assign(_sum=lambda x: x['F']+x['M']).sort_values(by='_sum').round(2)

    traces = []
    for col in ['F','M']:
        traces.append(go.Bar(x=grouped[col],y=grouped.index,orientation='h',name=col))

    data = traces
    fig = go.Figure(data=data,layout=go.Layout(barmode='stack',margin={'t':20,}))
    return fig

USERNAME_PASSWORD = [['tomek','tomek']]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
auth = dash_auth.BasicAuth(app, USERNAME_PASSWORD)
