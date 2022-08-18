from logging import PlaceHolder
import os
from turtle import width
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
    html.P("By JOHNNY", className="text-info"),
    html.Hr(),
# seção perfil -----------------------------------
    dbc.Button(id='botao_avatar', children=[html.Img(src='/assets/img_hom.png', id='avatar_change', alt='Avatar', className='perfil_avatar')
    ], style={'background-color': 'transparent', 'border-color': 'transparent' }),

# seção novo --------------------------------------
    dbc.Row([
        dbc.Col([
            dbc.Button(color='success', id='open-novo-receita',
            children=['+Receita'])
        ], width=6),
        dbc.Col([
            dbc.Button(color='danger', id='open-novo-despesa',
            children=['-Despesa'])
        ], width=6)    
    ]),
    #Modal da receita -----------------------------
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle('Adicionar receita')),
        dbc.ModalBody([
            dbc.Row([
                dbc.Col([
                    dbc.Label('Descrição: '),
                    dbc.Input(placeholder='EX: Dividendos, Herança DE ETC...', id='txt_receita')
                ], width=6),
                dbc.Col([
                    dbc.Label('Valor: '),
                    dbc.Input(placeholder="$100.00", id="valor_receita", value="")
                ], width=6)
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Data: "),
                    dcc.DatePickerSingle(id='date-receitas',
                        min_date_allowed=date(2020, 1, 1),
                        max_date_allowed=date(2030, 12, 31),
                        date=datetime.today(),
                        style={"width":"100%"}
                        ),

                ], width=4),
                dbc.Col([
                    dbc.Label("Extras"),
                    dbc.Checklist(
                        options=[],
                        value=[],
                        id='switches-input-receita',
                        switch=True
                    )
                ], width=4),
                dbc.Col([
                    dbc.Label('Categoria da receita'),
                    dbc.Select(id='select_receita', options=[], value=[])
                ], width=4)
                    
            ], style={'margin-top':'25px'}),
            dbc.Row([
                dbc.Accordion([
                    dbc.AccordionItem(children=[
                        dbc.Row([
                            dbc.Col([
                                html.Legend("Adicionar categoria", style={'color':'green'}),
                                dbc.Input(type="text", placeholder="Nova categoria...", id="input-add-receita"),
                                html.Br(),
                                dbc.Button("Adicionar", className="btn btn-success", id="add-category-receita", style={"margin-top":"20px"}),
                                html.Br(),
                                html.Div(id="category-div-add-receita", style={}),
                            ], width=6),
                            dbc.Col([
                                html.Legend('Excluir categoria', style={'color': 'red'}),
                                dbc.Checklist(
                                            id='checklist-selected-style-receita',
                                            options=[],
                                            value=[],
                                            label_checked_style={'color':'red'},
                                            input_checked_style={'backgroundColor':'blue', 'borderColor':'orange'}
                                ),
                                dbc.Button('Remover',color='warning', id='remove-category-receita', style={'margin-top':'20px'})
                            ], width=6)
                        ])
                    ], title='Adicionar/Remover categorias')

                ], flush=True, start_collapsed=True, id='accordion-receita'),
                html.Div(id='id_teste_receita', style={'padding-top':'20px'}),
                dbc.ModalFooter([
                    dbc.Button("Adicionar receita", id="salvar_receita", color="success"),
                    dbc.Popover(dbc.PopoverBody("Receita salva"), target="salvar_receita", placement="left", trigger="click")
                ])
            ], style={'margin-top':'25px'})

        ])

    ], style={"background-color":"rgba(17, 140, 79, 0.05)"},
     id='modal-novo-receita',
     size="lg",
     is_open=False,
     centered=True,
     backdrop=True),

    #Modal da despesa -----------------------------
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle('Adicionar despesa')),
        dbc.ModalBody([
            dbc.Row([
                dbc.Col([
                    dbc.Label('Descrição: '),
                    dbc.Input(placeholder='EX: contas, compras E ETC...', id='txt-despesa')
                ], width=6),
                dbc.Col([
                    dbc.Label('Valor: '),
                    dbc.Input(placeholder="$100.00", id="valor-despesa", value="")
                ], width=6)
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Data: "),
                    dcc.DatePickerSingle(id='date-despesas',
                        min_date_allowed=date(2020, 1, 1),
                        max_date_allowed=date(2030, 12, 31),
                        date=datetime.today(),
                        style={"width":"100%"}
                        ),

                ], width=4),
                dbc.Col([
                    dbc.Label("Extras"),
                    dbc.Checklist(
                        options=[],
                        value=[],
                        id='switches-input-despesa',
                        switch=True
                    )
                ], width=4),
                dbc.Col([
                    dbc.Label('Categoria da despesa'),
                    dbc.Select(id='select-despesa', options=[], value=[])
                ], width=4)
                    
            ], style={'margin-top':'25px'}),
            dbc.Row([
                dbc.Accordion([
                    dbc.AccordionItem(children=[
                        dbc.Row([
                            dbc.Col([
                                html.Legend("Adicionar categoria", style={'color':'green'}),
                                dbc.Input(type="text", placeholder="Nova categoria...", id="input-add-despesa"),
                                html.Br(),
                                dbc.Button("Adicionar", className="btn btn-success", id="add-category-despesa", style={"margin-top":"20px"}),
                                html.Br(),
                                html.Div(id="category-div-add-despesa", style={}),
                            ], width=6),
                            dbc.Col([
                                html.Legend('Excluir categoria', style={'color': 'red'}),
                                dbc.Checklist(
                                            id='checklist-selected-style-despesa',
                                            options=[],
                                            value=[],
                                            label_checked_style={'color':'red'},
                                            input_checked_style={'backgroundColor':'blue', 'borderColor':'orange'}
                                ),
                                dbc.Button('Remover',color='warning', id='remove-category-despesa', style={'margin-top':'20px'})
                            ], width=6)
                        ])
                    ], title='Adicionar/Remover categorias')

                ], flush=True, start_collapsed=True, id='accordion-despesa'),
                html.Div(id='id_teste_despesa', style={'padding-top':'20px'}),
                dbc.ModalFooter([
                    dbc.Button("Adicionar despesa", id="salvar_despesa", color="success"),
                    dbc.Popover(dbc.PopoverBody("despesa salva"), target="salvar_despesa", placement="left", trigger="click")
                ])
            ], style={'margin-top':'25px'})

        ])

    ], style={"background-color":"rgba(17, 140, 79, 0.05)"},
     id='modal-novo-despesa',
     size="lg",
     is_open=False,
     centered=True,
     backdrop=True),




# seção Nav ----------------------------------------
    html.Hr(),
    dbc.Nav([
        dbc.NavLink("Dashboards", href="/dashboards", active="exact"),
        dbc.NavLink("Extratos", href="/extratos", active="exact")
    ], vertical=True, pills=True, id='nav_buttons', style={"margin-bottom": "50px"})


            ], id='sidebar_completa')





# =========  Callbacks  =========== #
# Pop-up receita
@app.callback(
    Output('modal-novo-receita', 'is_open'),
    Input('open-novo-receita', 'n_clicks'),
    State('modal-novo-receita', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open

# Pop-up despesa
@app.callback(
    Output('modal-novo-despesa', 'is_open'),
    Input('open-novo-despesa', 'n_clicks'),
    State('modal-novo-despesa', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open

