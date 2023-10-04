# from dash import Dash, html

# app = Dash(__name__)

# # app.layout =html.Div('Hello World')
# #app layout UI
# app.layout=html.Div([
#     html.Div(children='Hello World')
# ])

# if __name__ == '__main__':
#     app.run(host="0.0.0.0",debug=True,port=5000)
    

# # Import packages
# from dash import Dash, html, dash_table
# import pandas as pd

# # Incorporate data
# # df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
# df=pd.read_csv("data/bert.csv")

# # Initialize the app
# app = Dash(__name__)

# # App layout
# app.layout = html.Div([
#     html.Div(children='My First App with Data'),
#     dash_table.DataTable(data=df.to_dict('records'), page_size=10,style_table={'overflowX': 'auto'} )
# ])

# # Run the app
# if __name__ == '__main__':
#     app.run(host="0.0.0.0",debug=True,port=5000)

# from dash import Dash, html, dash_table, dcc
# import pandas as pd
# import plotly.express as px

# # Incorporate data
# # df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
# df=pd.read_csv("data/bert.csv")

# # Initialize the app
# app = Dash(__name__)

# # App layout
# app.layout = html.Div([
#     html.Div(children='My First App with Data and a Graph'),
#     dash_table.DataTable(data=df.to_dict('records'), page_size=10,style_table={'overflowX': 'auto'}),
#     dcc.Graph(figure=px.histogram(df, x='Country', y='Weight', histfunc='avg'))
# ])

# # Run the app
# if __name__ == '__main__':
#     app.run(host="0.0.0.0",debug=True,port=5000)


# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
df=pd.read_csv("data/bert.csv")

# Initialize the app
app1 = Dash(__name__)
server=app1.server
app=app1

# App layout
app.layout = html.Div([
    html.Div(children='My First App with Data, Graph, and Controls'),
    html.Hr(),
    dcc.RadioItems(options=['Weight', 'Height', 'Age'], value='Height', id='controls-and-radio-item'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10,style_table={'overflowX': 'auto'}),
    dcc.Graph(figure={}, id='controls-and-graph')
])

# Add controls to build the interaction
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='Country', y=col_chosen, histfunc='avg')
    return fig

# Run the app
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=5000)

# app_main.py

# import dash

# # meta_tags are required for the app layout to be mobile responsive
# app = dash.Dash(__name__, suppress_callback_exceptions=True,
#                 meta_tags=[{'name': 'viewport',
#                             'content': 'width=device-width, initial-scale=1.0'}]
#                 )
# server = app.server
