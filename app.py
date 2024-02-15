import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("/home/cygnus/Documentos/khorda_data/spingo/dashboard/data/base_clean.csv")
df = df.fillna(0)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], meta_tags=[
                {"name": "viewport", "content": "width=device-width, initial-scale=1.0, maximum-scale=3.0, minimum-scale=0.2"}])
app.css.append_css({'external_url': '/assets/styles.css'})
app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})


card_contents = [
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/person.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_1', n_clicks=0
            ),"ID's"]),
        dbc.CardBody(
            [
                html.H3("119", className="card-title text-center"),
                html.H6("Número de ID's", className="card-text text-center")
            ]
        ),
    ],
    [
        dbc.CardHeader(
            [
            html.Button(
            html.Img(src='/assets/person.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_2', n_clicks=0
            ),"Edad"]
        ),
        dbc.CardBody(
            [
                html.H3("32.18", className="card-title text-center"),
                html.H6("Promedio de edad", className="card-text text-center")
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/car-front.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_3', n_clicks=0
            ),"Marca"]),
        dbc.CardBody(
            [
                html.H5("Chevrolet, Nissan, Volkswagen", className="card-title text-center"),
                html.H5("Principales marcas de autos", className="card-text text-center"),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/car-front.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_4', n_clicks=0
            ),"Modelo"
            
        ]),
        dbc.CardBody(
            [
                html.H3("2017, 2013, 2019", className="card-title text-center"),
                html.H6(
                    "Principales modelos de autos",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/car-front.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_5', n_clicks=0
            ),"Tipo"]),
        dbc.CardBody(
            [
                html.H5("Tipo", className="card-title text-center"),
                html.H6(
                    "Principales tipos de autos",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/speedometer2.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_6', n_clicks=0
            ),"Kilometraje"]),
        dbc.CardBody(
            [
                html.H3("102, 745 km", className="card-title text-center"),
                html.H6(
                    "Promedio de Kilometraje",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/car-front.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_7', n_clicks=0
            ),"Transmisión"
        ]),
        dbc.CardBody(
            [
                html.H5("71 manuales/ 48 automáticos", className="card-title text-center"),
                html.H5(
                    "Transmisión",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/taxi-front.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_8', n_clicks=0
            ),"Plataforma"]),
        dbc.CardBody(
            [
                html.H3("11.8%", className="card-title text-center"),
                html.H6(
                    "En plataforma",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/currency-dollar.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_9', n_clicks=0
            ),"Deducción Total Descuentos"]),
        dbc.CardBody(
            [
                html.H3("$ 2,898.00", className="card-title text-center"),
                html.H6(
                    "Promedio de deducciones",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/currency-dollar.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_10', n_clicks=0
            ),"Ajuste Total"]),
        dbc.CardBody(
            [
                html.H5("Ajuste Total", className="card-title text-center"),
                html.P(
                    "Promedio de ajuste total",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/currency-dollar.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_11', n_clicks=0
            ),"Deducción tenencias"]),
        dbc.CardBody(
            [
                html.H3("$ 786.00", className="card-title text-center"),
                html.P(
                    "Promedio deducción tenencias",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/currency-dollar.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_12', n_clicks=0
            ),"Deducción kilometraje"]),
        dbc.CardBody(
            [
                html.H3("$ 4.62", className="card-title text-center"),
                html.P(
                    "Promedio deducción kilometraje",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/currency-dollar.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_13', n_clicks=0
            ),"Deducción mecánica"]),
        dbc.CardBody(
            [
                html.H3("$ 4000.00", className="card-title text-center"),
                html.P(
                    "Solo tenemos un valor",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/currency-dollar.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_14', n_clicks=0
            ),"Deducción suspensión"]),
        dbc.CardBody(
            [
                html.H3("$ 0", className="card-title text-center"),
                html.P(
                    "Tenemos valores ceros",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/currency-dollar.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_15', n_clicks=0
            ),"Deducción vehículo"]),
        dbc.CardBody(
            [
                html.H3("$ 8.47", className="card-title text-center"),
                html.P(
                    "Promedio deducción tipo vehículo",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/currency-dollar.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_16', n_clicks=0
            ),"Deducción neumáticos"]),
        dbc.CardBody(
            [
                html.H3("$ 3,600", className="card-title text-center"),
                html.P(
                    "Solo tenemos un valor",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/currency-dollar.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_17', n_clicks=0
            ),"Deducción cristales"]),
        dbc.CardBody(
            [
                html.H3("$95,276 $2,500", className="card-title text-center"),
                html.P(
                    "Solo tenemos dos valores",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/currency-dollar.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_18', n_clicks=0
            ),"Deducción propietario"]),
        dbc.CardBody(
            [
                html.H3("$423.21", className="card-title text-center"),
                html.P(
                    "Promedio deducción propietario",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/currency-dollar.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_19', n_clicks=0
            ),"Deducción extemporanea"]),
        dbc.CardBody(
            [
                html.H3("$ 2,075", className="card-title text-center"),
                html.P(
                    "Tenemos 5 datos con este valor",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/currency-dollar.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_19_1', n_clicks=0
            ),"Deducción infracciones"]),
        dbc.CardBody(
            [
                html.H3("$ 551.38", className="card-title text-center"),
                html.P(
                    "Promedio deducción infracciones",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/currency-dollar.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_20', n_clicks=0
            ),"Monto solicitado cliente"]),
        dbc.CardBody(
            [
                html.H3("$ 13,687", className="card-title text-center"),
                html.P(
                    "Promedio monto solicitado",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/currency-dollar.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_21', n_clicks=0
            ),"Precio guía autométrica"]),
        dbc.CardBody(
            [
                html.H3("$ 209,457", className="card-title text-center"),
                html.P(
                    "Promedio guía autométrica",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/currency-dollar.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_22', n_clicks=0
            ),"Ajuste valor avalúo"]),
        dbc.CardBody(
            [
                html.H3("$ 146,620", className="card-title text-center"),
                html.P(
                    "Promedio valor avalúo",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/currency-dollar.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_23', n_clicks=0
            ),"Ajuste tipo vehículo"]),
        dbc.CardBody(
            [
                html.H3("$ 0.0", className="card-title text-center"),
                html.P(
                    "Tenemos valores en ceros",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/currency-dollar.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_24', n_clicks=0
            ),"Ajuste avalúo km"]),
        dbc.CardBody(
            [
                html.H3("$ 7,768", className="card-title text-center"),
                html.P(
                    "Promedio avalúo km",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/currency-dollar.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_25', n_clicks=0
            ),"Avalúo tipo vehículo"]),
        dbc.CardBody(
            [
                html.H3("$ 0.0", className="card-title text-center"),
                html.P(
                    "Tenemos valores ceros",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/currency-dollar.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_26', n_clicks=0
            ),"Ajuste multas"]),
        dbc.CardBody(
            [
                html.H3("$ 1,424", className="card-title text-center"),
                html.P(
                    "Promedio ajuste multas",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/currency-dollar.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_27', n_clicks=0
            ),"Ajuste trámites"]),
        dbc.CardBody(
            [
                html.H3("$ 423.21", className="card-title text-center"),
                html.P(
                    "Promedio ajuste tramites",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/currency-dollar.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_28', n_clicks=0
            ),"Avería estética mecánica"]),
        dbc.CardBody(
            [
                html.H3("$ 1,050", className="card-title text-center"),
                html.H6(
                    "Prom. Avería estética mecánica",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/currency-dollar.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_29', n_clicks=0
            ),"Ajuste monto prestar"]),
        dbc.CardBody(
            [
                html.H3("$ 127,034", className="card-title text-center"),
                html.H6(
                    "Promedio ajuste monto prestar",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/currency-dollar.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_30', n_clicks=0
            ),"Ajuste margen favor"]),
        dbc.CardBody(
            [
                html.H3("$ 113,347", className="card-title text-center"),
                html.H6(
                    "Promedio ajuste margen favor",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
    [
        dbc.CardHeader([
            html.Button(
            html.Img(src='/assets/currency-dollar.svg', style={'margin-right': '8px', 'width': '20px', 'height': '20px'}),
            className="btn btn-light", id='button_31', n_clicks=0
            ),"Ajuste avalúo ajustado"]),
        dbc.CardBody(
            [
                html.H3("$ 129,932", className="card-title text-center"),
                html.H6(
                    "Prom. ajuste avalúo ajustado",
                    className="card-text text-center",
                ),
            ]
        ),
    ],
]


app.layout = html.Div([
    dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src='/assets/logo.png', height='30px')),
                        ],
                        align='center'
                    ),
                    href='/',
                ),
            ],
            fluid=True,
        ),
        color='#3340e3',
        dark=True,
    ),
    dcc.Tabs([
        dcc.Tab(
            label='Análisis General',
            style={'backgroundColor': 'rgba(58,214,155,1)', 'color': 'white'},
            children=[
                html.Br(),
                html.Div(
                    className='row',  # Clase Flexbox para contenedor flexible
                    children=[

        dbc.Row(
            [
                                dbc.Col(dbc.Card(card_contents[0], color="primary", outline=True), style={'margin': '10px'}),
                                dbc.Col(dbc.Card(card_contents[1], color="primary", outline=True), style={'margin': '10px'}),
                                dbc.Col(dbc.Card(card_contents[2], color="primary", outline=True), style={'margin': '10px'}),
                                dbc.Col(dbc.Card(card_contents[3], color="primary", outline=True), style={'margin': '10px'}),
                                dbc.Col(dbc.Card(card_contents[4], color="primary", outline=True), style={'margin': '10px'}),
            ],
            className="mb-4",
        ),
        dbc.Row(
            [
                                dbc.Col(dbc.Card(card_contents[5], color="primary", outline=True), style={'margin': '10px'}),
                                dbc.Col(dbc.Card(card_contents[6], color="primary", outline=True), style={'margin': '10px'}),
                                dbc.Col(dbc.Card(card_contents[7], color="primary", outline=True), style={'margin': '10px'}),
                                dbc.Col(dbc.Card(card_contents[8], color="primary", outline=True), style={'margin': '10px'}),
                                dbc.Col(dbc.Card(card_contents[9], color="danger", outline=True), style={'margin': '10px'}),
            ],
            className="mb-4",
        ),


                    ]
                ),
                html.Div(
                    className='d-flex flex-row',
                    style={'padding': '20px'},  
                    children=[
                        dcc.Graph(id='graph1',
                                  style={'width': '100%', 'height': '100%'}),
                    ]
                ),
            ]
        ),
        dcc.Tab(
            label='Análisis Descuentos',
            style={'backgroundColor': 'rgba(58,214,155,1)', 'color': 'white'},
            children=[
                html.Br(),
                html.Div(
                    className='row',
                    children=[
        dbc.Row(
            [
                                dbc.Col(dbc.Card(card_contents[10], color="primary", outline=True), style={'margin': '10px'}),
                                dbc.Col(dbc.Card(card_contents[11], color="primary", outline=True), style={'margin': '10px'}),
                                dbc.Col(dbc.Card(card_contents[12], color="primary", outline=True), style={'margin': '10px'}),
                                dbc.Col(dbc.Card(card_contents[13], color="primary", outline=True), style={'margin': '10px'}),
                                dbc.Col(dbc.Card(card_contents[14], color="primary", outline=True), style={'margin': '10px'}),
            ],
            className="mb-4",
        ),
        dbc.Row(
            [
                                dbc.Col(dbc.Card(card_contents[15], color="primary", outline=True), style={'margin': '10px'}),
                                dbc.Col(dbc.Card(card_contents[16], color="primary", outline=True), style={'margin': '10px'}),
                                dbc.Col(dbc.Card(card_contents[17], color="primary", outline=True), style={'margin': '10px'}),
                                dbc.Col(dbc.Card(card_contents[18], color="primary", outline=True), style={'margin': '10px'}),
                                dbc.Col(dbc.Card(card_contents[19], color="primary", outline=True), style={'margin': '10px'}),
            ],
            className="mb-4",
        ),

                ]),
                html.Div(
                    className='d-flex flex-row',
                    style={'padding': '20px'},  
                    children=[
                        dcc.Graph(id='graph2',
                                  style={'width': '100%', 'height': '100%'}),
                    ]
                ),

            ]
        ),
        dcc.Tab(
            label='Análisis Ajuste',
            style={'backgroundColor': 'rgba(58,214,155,1)', 'color': 'white'},
            children=[
                html.Br(),
                html.Div(
                    className='row',
                    children=[
        dbc.Row(
            [
                                dbc.Col(dbc.Card(card_contents[20], color="primary", outline=True), style={'margin': '10px'}),
                                dbc.Col(dbc.Card(card_contents[21], color="primary", outline=True), style={'margin': '10px'}),
                                dbc.Col(dbc.Card(card_contents[22], color="primary", outline=True), style={'margin': '10px'}),
                                dbc.Col(dbc.Card(card_contents[23], color="primary", outline=True), style={'margin': '10px'}),
                                dbc.Col(dbc.Card(card_contents[24], color="primary", outline=True), style={'margin': '10px'}),
                                dbc.Col(dbc.Card(card_contents[25], color="primary", outline=True), style={'margin': '10px'}),
            ],
            className="mb-4",
        ),
        dbc.Row(
            [
                                dbc.Col(dbc.Card(card_contents[26], color="primary", outline=True), style={'margin': '10px'}),
                                dbc.Col(dbc.Card(card_contents[27], color="primary", outline=True), style={'margin': '10px'}),
                                dbc.Col(dbc.Card(card_contents[28], color="primary", outline=True), style={'margin': '10px'}),
                                dbc.Col(dbc.Card(card_contents[29], color="primary", outline=True), style={'margin': '10px'}),
                                dbc.Col(dbc.Card(card_contents[30], color="primary", outline=True), style={'margin': '10px'}),
                                dbc.Col(dbc.Card(card_contents[31], color="primary", outline=True), style={'margin': '10px'}),
            ],
            className="mb-4",
        ),

                ]),
                html.Div(
                    className='d-flex flex-row',
                    style={'padding': '20px'},  
                    children=[
                        dcc.Graph(id='graph3',
                                  style={'width': '100%', 'height': '100%'}),
                    ]
                ),
            ]
        ),
    ]),
])






@app.callback(
    Output('graph1', 'figure'),
    [Input('button_1', 'n_clicks'),
    Input('button_2', 'n_clicks'),
    Input('button_3', 'n_clicks'),
    Input('button_4', 'n_clicks'),
    Input('button_5', 'n_clicks'),
    Input('button_6', 'n_clicks'),
    Input('button_7', 'n_clicks'),
    Input('button_8', 'n_clicks'),
    Input('button_9', 'n_clicks')]
)
def update_graph(button1_clicks, button2_clicks, button3_clicks, button4_clicks, button5_clicks, button6_clicks, button7_clicks, button8_clicks, button9_clicks):
    ctx = dash.callback_context
    clicked_button_id = ctx.triggered_id.split('.')[0] if ctx.triggered_id else None
    figure = {}

    # Crear el gráfico correspondiente
    if clicked_button_id == 'button_1':
        pass
    elif clicked_button_id == 'button_2':
        figure = px.histogram(
            df,
            x='user_edad',
            nbins=30,
            marginal='rug',
            labels={'user_edad': 'Edad', 'count': 'Frecuencia'},
            template='plotly_white',
            color_discrete_sequence=['#3340e3']
        )

        # Personalizar la apariencia del gráfico
        figure.update_traces(marker_line_color='magenta', marker_line_width=1.5)

        figure.update_xaxes(tickvals=list(range(0, 101, 5)))  # Ajustar las marcas del eje x
        figure.update_xaxes(tickfont=dict(size=16))
        figure.update_yaxes(tickfont=dict(size=16))

        # Ajustar el diseño general del gráfico
        figure.update_layout(
            title_font_size=16,
            xaxis_title_font_size=20,
            yaxis_title_font_size=20,
            margin=dict(l=0, r=0, b=0, t=30),  # Ajustar los márgenes
            paper_bgcolor='white',  # Cambiar el color de fondo a blanco
        )

        # Añadir leyenda y ajustar su posición
        figure.update_layout(
            legend=dict(itemsizing='constant'),
            showlegend=True
        )

        
    elif clicked_button_id == 'button_3':
        counts = df['car_marca'].value_counts()

        top_10_counts = counts.head(10).sort_values(ascending=True)

        # Crear la gráfica de barras horizontales
        figure = px.bar(
            x=top_10_counts.values,
            y=top_10_counts.index,
            orientation='h',
            labels={'x': 'Número de Modelos', 'y': ''},
            template='plotly_white',
            color_discrete_sequence=['#3340e3'],
        )
        figure.update_xaxes(tickfont=dict(size=16))
        figure.update_yaxes(tickfont=dict(size=20))
        figure.update_traces(text=top_10_counts.values, textposition='outside')
        figure.update_layout(
        title_font_size=20,
        xaxis_title_font_size=18,
        yaxis_title_font_size=18,
        margin=dict(l=0, r=0, b=0, t=60),  # Ajustar los márgenes
        )


    elif clicked_button_id == 'button_4':
        conteo_autos_por_ano =  df['car_modelo'].value_counts().reset_index()

        figure = px.bar(conteo_autos_por_ano, x='car_modelo', y=conteo_autos_por_ano.index,
                     labels={'car_modelo': '', 'count': ''},
                     template='plotly_white',  # Cambiar el estilo del fondo
                     color_discrete_sequence=['#3340e3'],  # Cambiar el color de las barras
                     )
        
        # Personalizar los ejes y las marcas
        figure.update_xaxes(
            tickmode='linear',  # Ajustar las marcas de los ejes
            tick0=2010,  # Punto de inicio de las marcas
            dtick=1,  # Espaciado entre marcas
            tickangle=45,  # Ángulo de las marcas
            tickfont=dict(size=20),  # Tamaño de la fuente de las marcas
        )
        figure.update_traces(textposition='outside')
        figure.update_yaxes(tickfont=dict(size=16))
        figure.update_layout(
        xaxis_title_font_size=20,
        yaxis_title_font_size=18,
        margin=dict(l=0, r=0, b=0, t=60),  # Ajustar los márgenes
        )
    elif clicked_button_id == 'button_5':
        counts = df['car_tipo'].value_counts()

        top_10_counts = counts.head(10).sort_values(ascending=True)

        # Crear la gráfica de barras horizontales
        figure = px.bar(
            x=top_10_counts.values,
            y=top_10_counts.index,
            orientation='h',
            labels={'x': 'Total', 'y': ''},
            template='plotly_white',
            color_discrete_sequence=['#3340e3'],
        )
        figure.update_xaxes(tickfont=dict(size=16))
        figure.update_yaxes(tickfont=dict(size=20))
        figure.update_traces(text=top_10_counts.values, textposition='outside')
        figure.update_layout(
        title_font_size=20,
        xaxis_title_font_size=20,
        yaxis_title_font_size=18,
        margin=dict(l=0, r=0, b=0, t=60),  # Ajustar los márgenes
        )
    elif clicked_button_id == 'button_6':
        figure = px.histogram(df, x="car_kilometraje",
                   marginal="box", # or violin, rug
                   hover_data=df.columns,   
                   template='plotly_white',
                   color_discrete_sequence=['#3340e3'])
        figure.update_layout(
            title_font_size=22,
            xaxis_title_font_size=18,
            yaxis_title_font_size=20,
            legend_title_font_size=16,
            margin=dict(l=0, r=0, b=50, t=60),  # Ajustar los márgenes
        )

        # Aumentar el tamaño de la fuente de los ticks
        figure.update_xaxes(tickfont=dict(size=20))
        figure.update_yaxes(tickfont=dict(size=14))

        
    elif clicked_button_id == 'button_7':
        transmision_counts = df['car_transmision'].value_counts().reset_index()
        transmision_counts.columns = ['Transmisión', 'Count']

        # Crear la gráfica de dona con mejor diseño
        figure = px.pie(transmision_counts, names='Transmisión', values='Count',
                     hole=0.6,  # Configurar el tamaño del agujero para convertirlo en dona
                     color_discrete_sequence=['#3498db', '#3340e3'],  # Cambiar los colores
                     labels={'Count': 'Cantidad'},
                     )

        figure.update_layout(
            margin=dict(l=0, r=0, t=40, b=0),  # Ajustar los márgenes
            showlegend=True,  # Mostrar la leyenda
            legend=dict(x=0.45, y=0, orientation='h'),  # Posicionar la leyenda en el centro inferior
            annotations=[
                dict(
                    x=0.5,
                    y=0.5,
                    text='Transmisión',
                    showarrow=False,
                    font=dict(size=20),
                    xref='paper',
                    yref='paper'
                )
            ]
        )
        
    elif clicked_button_id == 'button_8':
        plataforma_counts = df['car_plataforma'].value_counts().reset_index()
        plataforma_counts.columns = ['Plataforma', 'Count']

        # Crear la gráfica de dona con mejor diseño
        figure = px.pie(plataforma_counts, names='Plataforma', values='Count',
                     hole=0.6,  # Configurar el tamaño del agujero para convertirlo en dona
                     color_discrete_sequence=['#3498db', '#3340e3'],  # Cambiar los colores
                     labels={'Count': 'Cantidad'},
                     )

        figure.update_layout(
            margin=dict(l=0, r=0, t=40, b=0),  # Ajustar los márgenes
            showlegend=True,  # Mostrar la leyenda
            legend=dict(x=0.48, y=0, orientation='h'),  # Posicionar la leyenda en el centro inferior
            annotations=[
                dict(
                    x=0.5,
                    y=0.5,
                    text='En plataforma',
                    showarrow=False,
                    font=dict(size=20),
                    xref='paper',
                    yref='paper'
                )
            ]
        )
        
    elif clicked_button_id == 'button_9':
        figure = px.histogram(df, x="deduccion_totalDescuentos",
                   marginal="box", # or violin, rug
                   hover_data=df.columns,   
                   template='plotly_white',
                   color_discrete_sequence=['#3340e3'])
        figure.update_layout(
            xaxis_title='Deducción Total de Descuentos',
            yaxis_title='Frecuencia',
            showlegend=False,
            font=dict(size=12),
        )
        
    else:
        pass

    return figure


@app.callback(
    Output('graph2', 'figure'),
    [Input('button_11', 'n_clicks'),
     Input('button_12', 'n_clicks'),
     Input('button_13', 'n_clicks'),
     Input('button_14', 'n_clicks'),
     Input('button_15', 'n_clicks'),
     Input('button_16', 'n_clicks'),
     Input('button_17', 'n_clicks'),
     Input('button_18', 'n_clicks'),
     Input('button_19', 'n_clicks'),
     Input('button_19_1', 'n_clicks'),],
     
)
def update_graph(button11_clicks, button12_clicks, button13_clicks, button14_clicks, button15_clicks, button16_clicks, button17_clicks, button18_clicks, button19_clicks, button19_1_clicks):
    ctx = dash.callback_context
    clicked_button_id = ctx.triggered_id.split('.')[0] if ctx.triggered_id else None
    figure = {}

    # Crear el gráfico correspondiente
    if clicked_button_id == 'button_11':
        figure = px.histogram(
        df,
        x='deduccion_tenencias',
        nbins=30,
        marginal='rug',
        labels={'deduccion_tenencias': 'Deducción Tenencia', 'count': 'Frecuencia'},
        template='plotly_white',
        color_discrete_sequence=['#3340e3']
        )

        # Personalizar la apariencia del gráfico
        figure.update_traces(marker_line_color='magenta', marker_line_width=2)

        figure.update_xaxes(tickfont=dict(size=16))
        figure.update_yaxes(tickfont=dict(size=16))
        # Ajustar el diseño general del gráfico
        figure.update_layout(
            title_font_size=16,
            xaxis_title_font_size=20,
            yaxis_title_font_size=20,
            margin=dict(l=0, r=0, b=0, t=30),  # Ajustar los márgenes
        )

        # Añadir leyenda y ajustar su posición
        figure.update_layout(
            legend=dict(itemsizing='constant'),
            showlegend=True
        )
    if clicked_button_id == 'button_12':
        figure = px.histogram(
        df,
        x='deduccion_deduccion_kilometraje',
        nbins=30,
        marginal='rug',
        labels={'deduccion_deduccion_kilometraje': 'Deducción kilometraje', 'count': 'Frecuencia'},
        template='plotly_white',
        color_discrete_sequence=['#3340e3']
        )

        # Personalizar la apariencia del gráfico
        figure.update_traces(marker_line_color='magenta', marker_line_width=2)

        figure.update_xaxes(tickfont=dict(size=16))
        figure.update_yaxes(tickfont=dict(size=16))
        # Ajustar el diseño general del gráfico
        figure.update_layout(
            title_font_size=16,
            xaxis_title_font_size=20,
            yaxis_title_font_size=20,
            margin=dict(l=0, r=0, b=0, t=30),  # Ajustar los márgenes
        )

        # Añadir leyenda y ajustar su posición
        figure.update_layout(
            legend=dict(itemsizing='constant'),
            showlegend=True
        )
    if clicked_button_id == 'button_13':
        figure = px.histogram(
        df,
        x='deduccion_mecanica',
        nbins=30,
        marginal='rug',
        labels={'deduccion_mecanica': 'Deducción mecánica', 'count': 'Frecuencia'},
        template='plotly_white',
        color_discrete_sequence=['#3340e3']
        )

        # Personalizar la apariencia del gráfico
        figure.update_traces(marker_line_color='magenta', marker_line_width=2)

        figure.update_xaxes(tickfont=dict(size=16))
        figure.update_yaxes(tickfont=dict(size=16))
        # Ajustar el diseño general del gráfico
        figure.update_layout(
            title_font_size=16,
            xaxis_title_font_size=20,
            yaxis_title_font_size=20,
            margin=dict(l=0, r=0, b=0, t=30),  # Ajustar los márgenes
        )

        # Añadir leyenda y ajustar su posición
        figure.update_layout(
            legend=dict(itemsizing='constant'),
            showlegend=True
        )
    if clicked_button_id == 'button_14':
        pass
    if clicked_button_id == 'button_15':
        figure = px.histogram(
        df,
        x='deduccion_tipo_vehiculo',
        nbins=30,
        marginal='rug',
        labels={'deduccion_tipo_vehiculo': 'Deducción tipo vehículo', 'count': 'Frecuencia'},
        template='plotly_white',
        color_discrete_sequence=['#3340e3']
        )

        # Personalizar la apariencia del gráfico
        figure.update_traces(marker_line_color='magenta', marker_line_width=2)

        figure.update_xaxes(tickfont=dict(size=16))
        figure.update_yaxes(tickfont=dict(size=16))
        # Ajustar el diseño general del gráfico
        figure.update_layout(
            title_font_size=16,
            xaxis_title_font_size=20,
            yaxis_title_font_size=20,
            margin=dict(l=0, r=0, b=0, t=30),  # Ajustar los márgenes
        )

        # Añadir leyenda y ajustar su posición
        figure.update_layout(
            legend=dict(itemsizing='constant'),
            showlegend=True
        )
    if clicked_button_id == 'button_16':
        figure = px.histogram(
            df,
            x='deduccion_neumaticos',
            nbins=30,
            marginal='rug',
            labels={'deduccion_neumaticos': 'Deducción neumáticos', 'count': 'Frecuencia'},
            template='plotly_white',
            color_discrete_sequence=['#3340e3'],
        )

        # Personalizar la apariencia del gráfico
        figure.update_traces(marker_line_color='magenta', marker_line_width=2)

        figure.update_xaxes(tickfont=dict(size=16))
        figure.update_yaxes(tickfont=dict(size=16))
        # Ajustar el diseño general del gráfico
        figure.update_layout(
            title_font_size=16,
            xaxis_title_font_size=20,
            yaxis_title_font_size=20,
            margin=dict(l=0, r=0, b=0, t=30),  # Ajustar los márgenes
        )

        # Añadir leyenda y ajustar su posición
        figure.update_layout(
            legend=dict(itemsizing='constant'),
            showlegend=True
        )
    if clicked_button_id == 'button_17':
        figure = px.histogram(
            df,
            x='deduccion_cristales',
            nbins=30,
            marginal='rug',
            labels={'deduccion_cristales': 'Deducción cristales', 'count': 'Frecuencia'},
            template='plotly_white',
            color_discrete_sequence=['#3340e3']
        )

        # Personalizar la apariencia del gráfico
        figure.update_traces(marker_line_color='magenta', marker_line_width=2)

        figure.update_xaxes(tickfont=dict(size=16))
        figure.update_yaxes(tickfont=dict(size=16))
        # Ajustar el diseño general del gráfico
        figure.update_layout(
            title_font_size=16,
            xaxis_title_font_size=20,
            yaxis_title_font_size=20,
            margin=dict(l=0, r=0, b=0, t=30),  # Ajustar los márgenes
        )

        # Añadir leyenda y ajustar su posición
        figure.update_layout(
            legend=dict(itemsizing='constant'),
            showlegend=True
        )
    if clicked_button_id == 'button_18':
        figure = px.histogram(
        df,
        x='deduccion_propietario',
        nbins=30,
        marginal='rug',
        labels={'deduccion_propietario': 'Deducción propietario', 'count': 'Frecuencia'},
        template='plotly_white',
        color_discrete_sequence=['#3340e3']
        )

        # Personalizar la apariencia del gráfico
        figure.update_traces(marker_line_color='magenta', marker_line_width=2)

        figure.update_xaxes(tickfont=dict(size=16))
        figure.update_yaxes(tickfont=dict(size=16))
        # Ajustar el diseño general del gráfico
        figure.update_layout(
            title_font_size=16,
            xaxis_title_font_size=20,
            yaxis_title_font_size=20,
            margin=dict(l=0, r=0, b=0, t=30),  # Ajustar los márgenes
        )

        # Añadir leyenda y ajustar su posición
        figure.update_layout(
            legend=dict(itemsizing='constant'),
            showlegend=True
        )
    if clicked_button_id == 'button_19':
        figure = px.histogram(
        df,
        x='deduccion_extemporanea',
        nbins=30,
        marginal='rug',
        labels={'deduccion_extemporanea': 'Deducción extemporanea', 'count': 'Frecuencia'},
        template='plotly_white',
        color_discrete_sequence=['#3340e3']
        )

        # Personalizar la apariencia del gráfico
        figure.update_traces(marker_line_color='magenta', marker_line_width=2)

        figure.update_xaxes(tickfont=dict(size=16))
        figure.update_yaxes(tickfont=dict(size=16))
        # Ajustar el diseño general del gráfico
        figure.update_layout(
            title_font_size=16,
            xaxis_title_font_size=20,
            yaxis_title_font_size=20,
            margin=dict(l=0, r=0, b=0, t=30),  # Ajustar los márgenes
        )

        # Añadir leyenda y ajustar su posición
        figure.update_layout(
            legend=dict(itemsizing='constant'),
            showlegend=True
        )
    if clicked_button_id == 'button_19_1':
        figure = px.histogram(
        df,
        x='deduccion_infracciones',
        nbins=30,
        marginal='rug',
        labels={'deduccion_infracciones': 'Deducción infracciones', 'count': 'Frecuencia'},
        template='plotly_white',
        color_discrete_sequence=['#3340e3']
        )

        # Personalizar la apariencia del gráfico
        figure.update_traces(marker_line_color='magenta', marker_line_width=2)

        figure.update_xaxes(tickfont=dict(size=16))
        figure.update_yaxes(tickfont=dict(size=16))
        # Ajustar el diseño general del gráfico
        figure.update_layout(
            title_font_size=16,
            xaxis_title_font_size=20,
            yaxis_title_font_size=20,
            margin=dict(l=0, r=0, b=0, t=30),  # Ajustar los márgenes
        )

        # Añadir leyenda y ajustar su posición
        figure.update_layout(
            legend=dict(itemsizing='constant'),
            showlegend=True
        )

    else:
        pass

    return figure


@app.callback(
    Output('graph3', 'figure'),
    [Input('button_20', 'n_clicks'),
     Input('button_21', 'n_clicks'),
     Input('button_22', 'n_clicks'),
     Input('button_23', 'n_clicks'),
     Input('button_24', 'n_clicks'),
     Input('button_25', 'n_clicks'),
     Input('button_26', 'n_clicks'),
     Input('button_27', 'n_clicks'),
     Input('button_28', 'n_clicks'),
     Input('button_29', 'n_clicks'),
     Input('button_30', 'n_clicks'),
     Input('button_31', 'n_clicks')],
     
)
def update_graph(button20_clicks, button21_clicks, button22_clicks, button23_clicks, button24_clicks, button25_clicks, button26_clicks, button27_clicks, button28_clicks, button29_clicks, button30_clicks, button31_clicks):
    ctx = dash.callback_context
    clicked_button_id = ctx.triggered_id.split('.')[0] if ctx.triggered_id else None
    figure = {}

    # Crear el gráfico correspondiente
    if clicked_button_id == 'button_20':
        figure = px.histogram(
        df,
        x='ajuste_monto_solicitado_cliente',
        nbins=30,
        marginal='rug',
        labels={'ajuste_monto_solicitado_cliente': 'Monto solicitado', 'count': 'Frecuencia'},
        template='plotly_white',
        color_discrete_sequence=['#3340e3']
        )

        # Personalizar la apariencia del gráfico
        figure.update_traces(marker_line_color='magenta', marker_line_width=2)

        figure.update_xaxes(tickfont=dict(size=16))
        figure.update_yaxes(tickfont=dict(size=16))
        # Ajustar el diseño general del gráfico
        figure.update_layout(
            title_font_size=16,
            xaxis_title_font_size=20,
            yaxis_title_font_size=20,
            margin=dict(l=0, r=0, b=0, t=30),  # Ajustar los márgenes
        )

        # Añadir leyenda y ajustar su posición
        figure.update_layout(
            legend=dict(itemsizing='constant'),
            showlegend=True
        )
    elif clicked_button_id == 'button_21':
        figure = px.histogram(
        df,
        x='ajuste_precio_guia_autometrica',
        nbins=30,
        marginal='rug',
        labels={'ajuste_precio_guia_autometrica': 'Precio guía autométrica', 'count': 'Frecuencia'},
        template='plotly_white',
        color_discrete_sequence=['#3340e3']
        )

        # Personalizar la apariencia del gráfico
        figure.update_traces(marker_line_color='magenta', marker_line_width=2)

        figure.update_xaxes(tickfont=dict(size=16))
        figure.update_yaxes(tickfont=dict(size=16))
        # Ajustar el diseño general del gráfico
        figure.update_layout(
            title_font_size=16,
            xaxis_title_font_size=20,
            yaxis_title_font_size=20,
            margin=dict(l=0, r=0, b=0, t=30),  # Ajustar los márgenes
        )

        # Añadir leyenda y ajustar su posición
        figure.update_layout(
            legend=dict(itemsizing='constant'),
            showlegend=True
        )
    elif clicked_button_id == 'button_22':
        figure = px.histogram(
        df,
        x='ajuste_valor_avaluo',
        nbins=30,
        marginal='rug',
        labels={'ajuste_valor_avaluo': 'valor avalúo', 'count': 'Frecuencia'},
        template='plotly_white',
        color_discrete_sequence=['#3340e3']
        )

        # Personalizar la apariencia del gráfico
        figure.update_traces(marker_line_color='magenta', marker_line_width=2)

        figure.update_xaxes(tickfont=dict(size=16))
        figure.update_yaxes(tickfont=dict(size=16))
        # Ajustar el diseño general del gráfico
        figure.update_layout(
            title_font_size=16,
            xaxis_title_font_size=20,
            yaxis_title_font_size=20,
            margin=dict(l=0, r=0, b=0, t=30),  # Ajustar los márgenes
        )

        # Añadir leyenda y ajustar su posición
        figure.update_layout(
            legend=dict(itemsizing='constant'),
            showlegend=True
        )
    elif clicked_button_id == 'button_23':
        pass
    elif clicked_button_id == 'button_24':
        figure = px.histogram(
        df,
        x='ajuste_avaluo_km',
        nbins=30,
        marginal='rug',
        labels={'ajuste_avaluo_km': 'valor km', 'count': 'Frecuencia'},
        template='plotly_white',
        color_discrete_sequence=['#3340e3']
        )

        # Personalizar la apariencia del gráfico
        figure.update_traces(marker_line_color='magenta', marker_line_width=2)

        figure.update_xaxes(tickfont=dict(size=16))
        figure.update_yaxes(tickfont=dict(size=16))
        # Ajustar el diseño general del gráfico
        figure.update_layout(
            title_font_size=16,
            xaxis_title_font_size=20,
            yaxis_title_font_size=20,
            margin=dict(l=0, r=0, b=0, t=30),  # Ajustar los márgenes
        )

        # Añadir leyenda y ajustar su posición
        figure.update_layout(
            legend=dict(itemsizing='constant'),
            showlegend=True
        )
    elif clicked_button_id == 'button_25':
        pass
    elif clicked_button_id == 'button_26':
        figure = px.histogram(
        df,
        x='ajuste_multas',
        nbins=30,
        marginal='rug',
        labels={'ajuste_multas': 'Ajuste multas', 'count': 'Frecuencia'},
        template='plotly_white',
        color_discrete_sequence=['#3340e3']
        )

        # Personalizar la apariencia del gráfico
        figure.update_traces(marker_line_color='magenta', marker_line_width=2)

        figure.update_xaxes(tickfont=dict(size=16))
        figure.update_yaxes(tickfont=dict(size=16))
        # Ajustar el diseño general del gráfico
        figure.update_layout(
            title_font_size=16,
            xaxis_title_font_size=20,
            yaxis_title_font_size=20,
            margin=dict(l=0, r=0, b=0, t=30),  # Ajustar los márgenes
        )

        # Añadir leyenda y ajustar su posición
        figure.update_layout(
            legend=dict(itemsizing='constant'),
            showlegend=True
        )
    elif clicked_button_id == 'button_27':
        figure = px.histogram(
        df,
        x='ajuste_tramites',
        nbins=30,
        marginal='rug',
        labels={'ajuste_tramites': 'Ajuste tramites', 'count': 'Frecuencia'},
        template='plotly_white',
        color_discrete_sequence=['#3340e3']
        )

        # Personalizar la apariencia del gráfico
        figure.update_traces(marker_line_color='magenta', marker_line_width=2)

        figure.update_xaxes(tickfont=dict(size=16))
        figure.update_yaxes(tickfont=dict(size=16))
        # Ajustar el diseño general del gráfico
        figure.update_layout(
            title_font_size=16,
            xaxis_title_font_size=20,
            yaxis_title_font_size=20,
            margin=dict(l=0, r=0, b=0, t=30),  # Ajustar los márgenes
        )

        # Añadir leyenda y ajustar su posición
        figure.update_layout(
            legend=dict(itemsizing='constant'),
            showlegend=True
        )
    elif clicked_button_id == 'button_28':
        figure = px.histogram(
        df,
        x='ajuste_averia_estetica_mecanica',
        nbins=30,
        marginal='rug',
        labels={'ajuste_averia_estetica_mecanica': 'Ajuste avería estética mecánica', 'count': 'Frecuencia'},
        template='plotly_white',
        color_discrete_sequence=['#3340e3']
        )

        # Personalizar la apariencia del gráfico
        figure.update_traces(marker_line_color='magenta', marker_line_width=2)

        figure.update_xaxes(tickfont=dict(size=16))
        figure.update_yaxes(tickfont=dict(size=16))
        # Ajustar el diseño general del gráfico
        figure.update_layout(
            title_font_size=16,
            xaxis_title_font_size=20,
            yaxis_title_font_size=20,
            margin=dict(l=0, r=0, b=0, t=30),  # Ajustar los márgenes
        )

        # Añadir leyenda y ajustar su posición
        figure.update_layout(
            legend=dict(itemsizing='constant'),
            showlegend=True
        )
    elif clicked_button_id == 'button_29':
        figure = px.histogram(
        df,
        x='ajuste_monto_prestar',
        nbins=30,
        marginal='rug',
        labels={'ajuste_monto_prestar': 'Ajuste monto prestar', 'count': 'Frecuencia'},
        template='plotly_white',
        color_discrete_sequence=['#3340e3']
        )

        # Personalizar la apariencia del gráfico
        figure.update_traces(marker_line_color='magenta', marker_line_width=2)

        figure.update_xaxes(tickfont=dict(size=16))
        figure.update_yaxes(tickfont=dict(size=16))
        # Ajustar el diseño general del gráfico
        figure.update_layout(
            title_font_size=16,
            xaxis_title_font_size=20,
            yaxis_title_font_size=20,
            margin=dict(l=0, r=0, b=0, t=30),  # Ajustar los márgenes
        )

        # Añadir leyenda y ajustar su posición
        figure.update_layout(
            legend=dict(itemsizing='constant'),
            showlegend=True
        )
    elif clicked_button_id == 'button_30':
        figure = px.histogram(
        df,
        x='ajuste_margen_favor',
        nbins=30,
        marginal='rug',
        labels={'ajuste_margen_favor': 'Ajuste margen favor', 'count': 'Frecuencia'},
        template='plotly_white',
        color_discrete_sequence=['#3340e3']
        )

        # Personalizar la apariencia del gráfico
        figure.update_traces(marker_line_color='magenta', marker_line_width=2)

        figure.update_xaxes(tickfont=dict(size=16))
        figure.update_yaxes(tickfont=dict(size=16))
        # Ajustar el diseño general del gráfico
        figure.update_layout(
            title_font_size=16,
            xaxis_title_font_size=20,
            yaxis_title_font_size=20,
            margin=dict(l=0, r=0, b=0, t=30),  # Ajustar los márgenes
        )

        # Añadir leyenda y ajustar su posición
        figure.update_layout(
            legend=dict(itemsizing='constant'),
            showlegend=True
        )
    elif clicked_button_id == 'button_31':
        figure = px.histogram(
        df,
        x='ajuste_avaluo_ajustado',
        nbins=30,
        marginal='rug',
        labels={'ajuste_avaluo_ajustado': 'Ajuste avalúo ajustado', 'count': 'Frecuencia'},
        template='plotly_white',
        color_discrete_sequence=['#3340e3']
        )

        # Personalizar la apariencia del gráfico
        figure.update_traces(marker_line_color='magenta', marker_line_width=2)

        figure.update_xaxes(tickfont=dict(size=16))
        figure.update_yaxes(tickfont=dict(size=16))
        # Ajustar el diseño general del gráfico
        figure.update_layout(
            title_font_size=16,
            xaxis_title_font_size=20,
            yaxis_title_font_size=20,
            margin=dict(l=0, r=0, b=0, t=30),  # Ajustar los márgenes
        )

        # Añadir leyenda y ajustar su posición
        figure.update_layout(
            legend=dict(itemsizing='constant'),
            showlegend=True
        )
    else:
        pass
    return figure

if __name__ == '__main__':
    app.run_server(debug=True)
