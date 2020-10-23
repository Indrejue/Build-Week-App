from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
### Evaluate

Based on the data provided by far the most important factor in getting a pet to a home is to have the pet fixed.  This might be problematic if there is already an owner for the animal but if the animal does not have a chip or has not been claimed for over a month the shelter should consider getting the pet fixed or at least providing a fixing service for a small fee.  There is a caviate though to my conclusion as this data only covers animal shelters in the Austin area these conclusions might not apply the same elsewhere.

"""),
]