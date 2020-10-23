from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from joblib import load
import numpy as np
import pandas as pd
import shap

from app import app

pet_colors = ['black white',
                'black',
                'brown tabby',
                'brown white',
                'tan white',
                'brown tabby white',
                'white',
                'black tan',
                'orange tabby',
                'blue white',
                'black brown',
                'tricolor',
                'other',
                'brown',
                'tan',
                'brindle brown white',
                'tortie',
                'calico',
                'orange tabby white',
                'blue',
                'blue tabby',
                'red white',
                'red',
                'torbie',
                'chocolate white',
                'blue tabby white',
                'brindle brown',
                'buff',
                'sable',
                'cream tabby',
                'yellow',
                'lynx point',
                'cream',
                'gray white',
                'chocolate',
                'point seal',
                'fawn white',
                'gray',
                'sable white',
                'flame point',
                'cream tabby white',
                'black brindle white',
                'buff white',
                'black red',
                'blue merle',
                'brown tan',
                'cream white',
                'fawn',
                'tricolor white',
                'chocolate tan',
                'torbie white',
                'black brindle brown',
                'orange white',
                'black gray',
                'gold',
                'blue merle white',
                'black tricolor',
                'black smoke',
                'white yellow',
                'black tabby',
                'lilac point',
                'blue tan',
                'brown merle white',
                'brown merle',
                'gray tabby',
                'tortie white',
                'point tortie',
                'silver tan',
                'red tan',
                'blue point',
                'silver tabby',
                'gray tan',
                'merle red white',
                'black cream',
                'blue merle tan',
                'merle red',
                'calico white',
                'calico point',
                'liver white',
                'black tabby white',
                'gold white',
                'red tick white',
                'apricot',
                'brindle white yellow',
                'black brindle',
                'buff tan'
]

pet_fixed = ['fixed',
            'not fixed'
]
pet_gender = ['male',
            'female'
]
pet_type = ['Cat',
            'Dog'
]

style = {'padding': '1.5em'}

layout = html.Div([
    dcc.Markdown("""
        ### Predict

        Is the pet going to a home?
    
    """), 

    html.Div([
        dcc.Markdown('###### Is the animal fixed'), 
        dcc.Dropdown(
            id='Fixed', 
            options=[{'label': fixed, 'value': fixed} for fixed in pet_fixed], 
            value=Fixed[0]
        ), 
    ], style=style), 

    html.Div([
        dcc.Markdown('###### Gender'), 
        dcc.Dropdown(
            id='Gender', 
            options=[{'label': gender, 'value': gender} for gender in pet_gender], 
            value=Gender[0]
        ), 
    ], style=style), 

    html.Div([
        dcc.Markdown('###### Pet Type'), 
        dcc.Dropdown(
            id='AnimalType', 
            options=[{'label': pet, 'value': pet} for pet in pet_type], 
            value=AnimalType[0]
        ), 
    ], style=style), 

    html.Div([
        dcc.Markdown('###### Month Came In'), 
        dcc.Slider(
            id='Month', 
            min=0,
            max=12, 
            step=1, 
            value=1, 
            marks={n: str(n) for n in range(1,12,1)}
        ),
    ], style=style), 

    html.Div([
        dcc.Markdown('###### Age In Months'), 
        dcc.Slider(
            id='Age', 
            min=0, 
            max=240, 
            step=1, 
            value=12, 
            marks={n: str(n) for n in range(0,240,12)}
        ),  
    ], style=style),

    html.Div([
        dcc.Markdown('###### The Pets Color'), 
        dcc.Dropdown(
            id='Color', 
            options=[{'label': colors, 'value': colors} for colors in pet_colors], 
            value=Color[0]
        ), 
    ], style=style),

   
    dcc.Markdown('### Prediction'), 
    html.Div(id='prediction-content', style={'marginBottom': '5em'}), 

])

@app.callback(
    Output('prediction-content', 'children'),
    [Input('Fixed', 'value'),
     Input('Gender', 'value'),
     Input('AnimalType', 'value'),
     Input('Month', 'value'),
     Input('Age', 'value'),
     Input('Color', 'value')])
def predict(Fixed, Gender, AnimalType, Month, Age, Color):

    df = pd.DataFrame(
        columns=['Fixed', 'Gender', 'AnimalType', 'Month', 'Age','Color','Name','Breed', 'Year'], 
        data=[[Fixed, Gender, AnimalType, Month, Age, Color, 'other', 'other', np.NaN]]
    )

    pipeline = load('model/pipeline.joblib')
    y_pred = pipeline.predict(df)[0]
    if y_pred == 0:
        return html.H3('Pet is not likely to go to a home', className ='mb-5'),
    else:
        return html.H3('Pet will likely go to a home', className ='mb-5')
