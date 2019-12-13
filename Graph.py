from Functions import poly_evaluate, poly_evaluate_list, poly_array_to_string
import plotly
import plotly.graph_objs as go
import json
import numpy as np


def create_plot(feature):

    p1 = feature

    valores = [i for i in range(-50,51)]
    p1_valuete = poly_evaluate_list(p1, valores)

    fig = go.Figure(
        data=[
            go.Scatter(
                x= valores,
                y= p1_valuete,
                mode='lines',
                line=dict(color='#673ab7'),
                name='Polinomio'
            )           
        ],
        layout=go.Layout(
           
            plot_bgcolor='rgba(0,0,0,0)',
             xaxis=dict(
                autorange=True,
                showgrid=True,
                zeroline=True,
                showline=False,
                ticks='',
                showticklabels=True,
                zerolinewidth=1,
                zerolinecolor='#333',
                gridcolor='#d3d3d3',
                gridwidth=1
            ),
            yaxis=dict(
                autorange=True,
                showgrid=True,
                zeroline=True,
                showline=True,
                ticks='',
                showticklabels=True,
                zerolinewidth=1,
                zerolinecolor='#333',
                gridcolor='#d3d3d3',
                gridwidth=1
            ),          
        )
    )

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


def create_plot_with_roots(feature, pipeline):

    roots = pipeline[5]
    x0_list = pipeline[4]
    derivate_array = pipeline[3]
    alpha = pipeline[2]
    descartes_matrix = pipeline[1]
    complex_bool = pipeline[0]

    points = []
    
    for i in range(0, len(roots)):
       points.append((round(roots[i]), poly_evaluate(feature, round(roots[i]))))
       
    
    print(points)
    
    x = [x[0] for x in points]
    y = [x[1] for x in points]

    p1 = feature

    valores = [i for i in range(-100,100)]
    p1_valuete = poly_evaluate_list(p1, valores)


    fig = go.Figure(
        data=[
            go.Scatter(
                x= valores,
                y= p1_valuete,
                mode='lines',
                line=dict(color='#673ab7'),
                name='Polinomio'
            ),
            go.Scatter(
                x=x,
                y=y,
                mode='markers',
                name='Raizes',
                marker=dict(
                    size=12,
                    color='#673ab7'
                )
            )
        ],
        layout=go.Layout(
           
            plot_bgcolor='rgba(0,0,0,0)',
             xaxis=dict(
                autorange=True,
                showgrid=True,
                zeroline=True,
                showline=False,
                ticks='',
                showticklabels=True,
                zerolinewidth=1,
                zerolinecolor='#333',
                gridcolor='#d3d3d3',
                gridwidth=1
            ),
            yaxis=dict(
                autorange=True,
                showgrid=True,
                zeroline=True,
                showline=True,
                ticks='',
                showticklabels=True,
                zerolinewidth=1,
                zerolinecolor='#333',
                gridcolor='#d3d3d3',
                gridwidth=1
            ),
            annotations=[
                go.layout.Annotation(
                    text="Teste de raizes complexas: "+str(complex_bool)+"<br>"+"Descartes: "+str(descartes_matrix)+"<br>"+"Fujiwara: "+str(alpha)+"<br>"+"Derivada: "+poly_array_to_string(derivate_array)+"<br>"+"Separação das Raízes: "+str(x0_list)+"<br>",
                    align='left',
                    showarrow=False,
                    xref='paper',
                    yref='paper',
                    x=0.0,
                    y=1.4
                    #bordercolor='#673ab7',
                    #borderwidth=1
                )
            ]
        )
    )

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

def create_plot_with_point(feature, point):
    
    point = [(point, poly_evaluate(feature, point))] # point

    x = [point[0][0]]
    y = [point[0][1]]

    p1 = feature

    valores = [i for i in range(-x[0]-100, x[0]+100)]
    p1_valuete = poly_evaluate_list(p1, valores)
    
    fig = go.Figure(
        data=[
            go.Scatter(
                x= valores,
                y= p1_valuete,
                mode='lines',
                line=dict(color='#673ab7'),
                name='Polinomio'
            ) ,
            go.Scatter(
                x=x,
                y=y,
                mode='markers',
                name='Ponto',
                marker=dict(
                 size=12,
                    color='#673ab7'
                )
            )          
        ],
        layout=go.Layout(
           
            plot_bgcolor='rgba(0,0,0,0)',
             xaxis=dict(
                autorange=True,
                showgrid=True,
                zeroline=True,
                showline=False,
                ticks='',
                showticklabels=True,
                zerolinewidth=1,
                zerolinecolor='#333',
                gridcolor='#d3d3d3',
                gridwidth=1
            ),
            yaxis=dict(
                autorange=True,
                showgrid=True,
                zeroline=True,
                showline=True,
                ticks='',
                showticklabels=True,
                zerolinewidth=1,
                zerolinecolor='#333',
                gridcolor='#d3d3d3',
                gridwidth=1
            ),          
        )
    )

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON