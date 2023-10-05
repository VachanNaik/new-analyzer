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


# # Import packages
# from dash import Dash, html, dash_table, dcc, callback, Output, Input
# import pandas as pd
# import plotly.express as px

# # Incorporate data
# # df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
# df=pd.read_csv("data/bert.csv")

# # Initialize the app
# app1 = Dash(__name__)
# server=app1.server
# app=app1

# # App layout
# app.layout = html.Div([
#     html.Div(children='My First App with Data, Graph, and Controls'),
#     html.Hr(),
#     dcc.RadioItems(options=['Weight', 'Height', 'Age'], value='Height', id='controls-and-radio-item'),
#     dash_table.DataTable(data=df.to_dict('records'), page_size=10,style_table={'overflowX': 'auto'}),
#     dcc.Graph(figure={}, id='controls-and-graph')
# ])

# # Add controls to build the interaction
# @callback(
#     Output(component_id='controls-and-graph', component_property='figure'),
#     Input(component_id='controls-and-radio-item', component_property='value')
# )
# def update_graph(col_chosen):
#     fig = px.histogram(df, x='Country', y=col_chosen, histfunc='avg')
#     return fig

# # Run the app
# if __name__ == '__main__':
#     app.run(host="0.0.0.0",debug=True,port=5000)

# app_main.py

# import dash

# # meta_tags are required for the app layout to be mobile responsive
# app = dash.Dash(__name__, suppress_callback_exceptions=True,
#                 meta_tags=[{'name': 'viewport',
#                             'content': 'width=device-width, initial-scale=1.0'}]
#                 )
# server = app.server


# import dash
# from dash import Dash, html, dash_table, dcc, callback, Output, Input
# import plotly.express as px
# import pandas as pd
# import plotly.figure_factory as ff
# # import seaborn as sns
# # import matplotlib.pyplot as plt



# df = pd.read_csv("data/mod.csv")

# # Create a static Plotly Express figure for the bar plot
# static_fig_bar = px.bar(
#     df,
#     x='Country',
#     color='Description of AE',
#     facet_col='Drug Name',
#     title='Country vs Drug Name vs Description of AE',
#     labels={'count': 'Count of AE Description'}
# )

# static_fig_bar.update_layout(autosize=False, width=1200, height=800)
# static_fig_bar.update_xaxes(title_text='Country', tickangle=45)
# static_fig_bar.update_yaxes(title_text='Count')



# # Create a static Plotly Express figure for Drug Name vs Sentiment
# static_fig_sentiment = px.bar(
#     df, 
#     x='Drug Name', 
#     color='Sentiment',
#     title='Drug Name vs Sentiment',
#     labels={'count': 'Count of Sentiments'}
# )


# # Create a Dash app
# app1 = dash.Dash(__name__)
# server=app1.server
# app=app1

# # Define the layout of the web app
# app.layout = html.Div([
#      html.H1("PMS Analyzer", 
#             style={
#                 'textAlign': 'center', 
#                 'color': '#4CAF50',  # You can use hex codes, rgb, etc.
#                 'fontSize': 36,  # size of font
#                 'background': '#E0F7FA',  # background color of title
#                 'borderRadius': '5px',  # rounded corners
#                 'margin': '10px',  # space around the title
#                 'padding': '10px'  # space inside the title area
#             }
#            ),

#     dash_table.DataTable(
#     id='table',
#     columns=[{"name": i, "id": i} for i in df.columns],
#     data=df.to_dict('records'),  # Show all rows
#     page_size=10,  # Number of rows per page
#     style_table={'height': '300px', 'overflowY': 'auto'}
#     ),
#     dcc.RadioItems(
#         id='gender-radio',
#         options=[{'label': i, 'value': i} for i in df['Gender'].unique()],
#         value=df['Gender'].unique()[0],
#         labelStyle={'display': 'inline-block'}
#     ),
#     dcc.RadioItems(
#         id='dosage-radio',
#         options=[{'label': i, 'value': i} for i in df['Dosage'].unique()],
#         value=df['Dosage'].unique()[0],
#         labelStyle={'display': 'inline-block'}
#     ),
#     dcc.RadioItems(
#         id='frequency-radio',
#         options=[{'label': i, 'value': i} for i in df['Frequency of intake'].unique()],
#         value=df['Frequency of intake'].unique()[0],  # default value
#         labelStyle={'display': 'inline-block'}
#     ),
#     dcc.Graph(id='histogram'),
#     dcc.Graph(id='barplot', figure=static_fig_bar),  # set the figure directly here
#     dcc.Graph(id='sentimentplot', figure=static_fig_sentiment),  # static sentiment plot
#    # Added the map to the layout here

# ]
# )

# # Define callback to update first graph
# @app.callback(
#     Output('histogram', 'figure'),
#     [
#         Input('gender-radio', 'value'),
#         Input('dosage-radio', 'value'),
#         Input('frequency-radio', 'value')
#     ]
# )
# def update_histogram(selected_gender, selected_dosage, selected_frequency):
#     filtered_df = df[(df['Gender'] == selected_gender) 
#                      & (df['Dosage'] == selected_dosage) 
#                      & (df['Frequency of intake'] == selected_frequency)]
    
#     fig = px.histogram(filtered_df, 
#                        x='Medical History', 
#                        color='Drug Name',
#                        facet_col='Description of AE',
#                        title=f'Distribution of Drug Names across Medical History and AE Description\n'
#                              f'for {selected_gender}s with Dosage: {selected_dosage} and Frequency: {selected_frequency}',
#                        labels={'Medical History': 'Medical History', 'count': 'Count'}
#                       )

#     fig.update_layout(autosize=False, width=1200, height=800)
#     fig.update_xaxes(title_text='Medical History', tickangle=45)
#     fig.update_yaxes(title_text='Count')
    
#     return fig

# # Run the app
# if __name__ == '__main__':
#     app.run(host="0.0.0.0",debug=True,port=5000)


import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff
# import seaborn as sns
# import matplotlib.pyplot as plt



df = pd.read_csv("data/mod.csv")

# Create a static Plotly Express figure for the bar plot
static_fig_bar = px.bar(
    df,
    x='Country',
    color='Description of AE',
    facet_col='Drug Name',
    title='Country vs Drug Name vs Description of AE',
    labels={'count': 'Count of AE Description'}
)

static_fig_bar.update_layout(autosize=False, width=1200, height=800)
static_fig_bar.update_xaxes(title_text='Country', tickangle=45)
static_fig_bar.update_yaxes(title_text='Count')


# (Optional) Generate a static bar plot: Drug Name vs Outcome of AE
static_fig_outcome = px.bar(
    df, 
    x='Drug Name', 
    color='Outcome of AE',
    title='Drug Name vs Outcome of AE',
    labels={'count': 'Count of Outcomes'}
)
static_fig_outcome.update_layout(autosize=False, width=1200, height=800)
static_fig_outcome.update_xaxes(title_text='Drug Name', tickangle=45)
static_fig_outcome.update_yaxes(title_text='Count')



# Create a static Plotly Express figure for Drug Name vs Sentiment
static_fig_sentiment = px.bar(
    df, 
    x='Drug Name', 
    color='Sentiment',
    title='Drug Name vs Sentiment',
    labels={'count': 'Count of Sentiments'}
)


# Create a Dash app
app1 = dash.Dash(__name__)
server=app1.server
app=app1

# Define the layout of the web app
app.layout = html.Div([
     html.H1("PMS Analyzer", 
            style={
                'textAlign': 'center', 
                'color': '#4CAF50',  # You can use hex codes, rgb, etc.
                'fontSize': 36,  # size of font
                'background': '#E0F7FA',  # background color of title
                'borderRadius': '5px',  # rounded corners
                'margin': '10px',  # space around the title
                'padding': '10px'  # space inside the title area
            }
           ),

    dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),  # Show all rows
    page_size=10,  # Number of rows per page
    style_table={'height': '300px', 'overflowY': 'auto'}
    ),
    dcc.RadioItems(
        id='gender-radio',
        options=[{'label': i, 'value': i} for i in df['Gender'].unique()],
        value=df['Gender'].unique()[0],
        labelStyle={'display': 'inline-block'}
    ),
    dcc.RadioItems(
        id='dosage-radio',
        options=[{'label': i, 'value': i} for i in df['Dosage'].unique()],
        value=df['Dosage'].unique()[0],
        labelStyle={'display': 'inline-block'}
    ),
    dcc.RadioItems(
        id='frequency-radio',
        options=[{'label': i, 'value': i} for i in df['Frequency of intake'].unique()],
        value=df['Frequency of intake'].unique()[0],  # default value
        labelStyle={'display': 'inline-block'}
    ),
    dcc.Graph(id='histogram'),
    dcc.Graph(id='barplot', figure=static_fig_bar),  # set the figure directly here
    dcc.Graph(id='sentimentplot', figure=static_fig_sentiment),  # static sentiment plot
    dcc.Graph(id='outcomeplot', figure=static_fig_outcome),
   # Added the map to the layout here

]
)

# Define callback to update first graph
@app.callback(
    Output('histogram', 'figure'),
    [
        Input('gender-radio', 'value'),
        Input('dosage-radio', 'value'),
        Input('frequency-radio', 'value')
    ]
)
def update_histogram(selected_gender, selected_dosage, selected_frequency):
    filtered_df = df[(df['Gender'] == selected_gender) 
                     & (df['Dosage'] == selected_dosage) 
                     & (df['Frequency of intake'] == selected_frequency)]
    
    fig = px.histogram(filtered_df, 
                       x='Medical History', 
                       color='Drug Name',
                       facet_col='Description of AE',
                       title=f'Distribution of Drug Names across Medical History and AE Description\n'
                             f'for {selected_gender}s with Dosage: {selected_dosage} and Frequency: {selected_frequency}',
                       labels={'Medical History': 'Medical History', 'count': 'Count'}
                      )

    fig.update_layout(autosize=False, width=1200, height=800)
    fig.update_xaxes(title_text='Medical History', tickangle=45)
    fig.update_yaxes(title_text='Count')
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)



