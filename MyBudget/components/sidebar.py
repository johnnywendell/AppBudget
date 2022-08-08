import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd






# ========= Layout ========= #
layout = dbc.Col([ 
    html.H1("Mybudget", className="text-primary"),
    html.P("By ASIMOV", className="text-info"),
    html.Hr(),
# seção perfil -----------------------------------
    dbc.Button(id='botao_avatar', children=[html.Img(src='/assets/img_hom.png', id='avatar_change', alt='Avatar', className='perfil_avatar')
    ], style={'background-color': 'transparent', 'bordercolor': 'transparent' })
                
            ])





# =========  Callbacks  =========== #
# Pop-up receita
