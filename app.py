from inspect import trace
from dash import *
from iexfinance.stocks import *
import datetime
from dateutil.relativedelta import relativedelta
import plotly.graph_objs as go

start = datetime.datetime.today() - relativedelta(years=1)
end = datetime.datetime.today() - relativedelta(days=1)

inputStock = "VZ"
#a = Stock(inputStock,token = "<pk_42cdcecaff544134a674c0926e9e327a>")
df = get_historical_data(inputStock, start = start, end = end, output_format = "pandas")


trace_close = go.Scatter(
    x = list(df.index),
    y = list(df.close),
    name = "Close",
    line = dict(color = "#f44242")
)

trace_high = go.Scatter(
    x = list(df.index),
    y = list(df.high),
    name = "Close",
    line = dict(color = "#f44242")
)

#trace_close = 

app  = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(
        children  = 'Hello Dash!',
        style = {
            'textAlign' : 'center',
            'color' : '#456ABC'
        }
    ),

    html.Div('Dash - A data product development framework from plotly'),

    # this is adding an image and a CSS style sheet by hand
    html.Div([
        html.H2("Stock App"),
        html.Img(src = "/assets/Hat.png")
    ], className= "banner"
    ),

    html.Div([
        html.Div([
            dcc.Graph (
                id = "graph_close",
                figure  = {
                    "data" : [trace_close],
                    "layout": {
                        "title" : "Close Graph"
                    }
                }
            )
        ], className = "six columns"),

        html.Div([
            dcc.Graph (
                id = "graph_high",
                figure  = {
                    "data" : [trace_close],
                    "layout": {
                        "title" : "High Graph"
                    }
                }
            )
        ], className = "six columns"),

    ]),


    dcc.Graph(
        id = 'sample-graph',
        figure = {

            'data' : [
                {'x' : [5, 6, 7], 'y' : [12, 15, 18], 'type' : 'bar', 'name' : 'SF'},
                {'x' : [5, 6, 7], 'y' : [20, 25, 28], 'type' : 'bar', 'name' : 'SF'}
            ],

            'layout' : {
                'title' : 'Simple Barchart'
            }




        }
    )
])

app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

if __name__ == '__main__':
    app.run_server(port = 4050)




