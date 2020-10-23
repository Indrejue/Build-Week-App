from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
### Intro

There are aproxamatly 6.5 million animals taken in by shelters every year. Of those about 1.5 million wind up euthanized 
because they could not be addopted or the shelter had no other option. The goal is o determain what factors are likely 
to lead to a happy outcome of our four legged friends finding a good home.
"""),
html.Img(src='https://raw.githubusercontent.com/Indrejue/Build-Week-App/master/model/cat.png', style={'width':'50%'}),

html.Img(src='https://raw.githubusercontent.com/Indrejue/Build-Week-App/master/model/dog.png', style={'width':'50%'}),

]