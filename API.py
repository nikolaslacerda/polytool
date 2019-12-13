from flask import Flask, render_template,request, jsonify
from Functions import complex_roots_tests, derivate, descartes, fujiwara, getDegreePoly, newton, pipeline, poly_array_to_string, poly_evaluate, poly_evaluate_list, poly_mult_aux, poly_sub_aux, separate_roots, string_to_poly_array
from Graph import create_plot, create_plot_with_point, create_plot_with_roots
import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sum', methods=['POST'])
def poly_sum():
	"""Calcula a soma de dois polinomios."""
	poly_1 = request.form['name']
	poly_2 = request.form['email']

	poly_array_1 = string_to_poly_array(poly_1)
	poly_array_2 = string_to_poly_array(poly_2)

	if(len(poly_array_1) > len(poly_array_2)):
		poly_result = [0] * len(poly_array_1)
		while(len(poly_array_2) < len(poly_array_1)):
			poly_array_2.append(0)
	else :
		poly_result = [0] * len(poly_array_2)
		while(len(poly_array_1) < len(poly_array_2)):
			poly_array_1.append(0)   
    
	for i in range(0, len(poly_result)):
		poly_result[i] = poly_array_1[i] + poly_array_2[i]

	return jsonify({'name' : poly_array_to_string(poly_result)})


@app.route('/sub', methods=['POST'])
def poly_sub():
	"""Calcula a subtracao de dois polinomios."""
	poly_1 = request.form['name']
	poly_2 = request.form['email']

	poly_array_1 = string_to_poly_array(poly_1)
	poly_array_2 = string_to_poly_array(poly_2)

	if(len(poly_array_1) > len(poly_array_2)):
		poly_result = [0] * len(poly_array_1)
		while(len(poly_array_2) < len(poly_array_1)):
			poly_array_2.append(0)
	else :
		poly_result = [0] * len(poly_array_2)
		while(len(poly_array_1) < len(poly_array_2)):
			poly_array_1.append(0)   
    
	for i in range(0, len(poly_result)):
		poly_result[i] = poly_array_1[i] - poly_array_2[i]

	return jsonify({'name' : poly_array_to_string(poly_result)})


@app.route('/mul', methods=['POST'])
def poly_mult():
	"""Calcula a multiplicacao de dois polinomios."""
	poly_1 = request.form['name']
	poly_2 = request.form['email']

	poly_array_1 = string_to_poly_array(poly_1)
	poly_array_2 = string_to_poly_array(poly_2)

	poly_result = [0] * ((len(poly_array_1)-1) + (len(poly_array_2)-1) + 1)
	for i in range(0, len(poly_array_1)):
		for j in range(0, len(poly_array_2)):
			poly_result[i+j] += poly_array_1[i] * poly_array_2[j]
    
	return jsonify({'name' : poly_array_to_string(poly_result)})


@app.route('/div', methods=['POST'])
def poly_div():
    """Calcula a divisao de dois polinomios."""
    poly_1 = request.form['name']
    poly_2 = request.form['email']
    poly_array_1 = string_to_poly_array(poly_1)
    poly_array_2 = string_to_poly_array(poly_2)
    poly_result = [0] * ((len(poly_array_1)-1) - (len(poly_array_2)-1) + 1)
    poly_actual = poly_array_1

    while len(poly_actual) >= len(poly_array_2):
        if len(poly_actual) == 1 and poly_actual[0] == 0:
            break
        aux = [0] * ((len(poly_array_1)-1) - (len(poly_array_2)-1) + 1)
        dividendo = poly_actual[-1]
        divisor = poly_array_2[-1]
        aux[(len(poly_actual) - 1) - (len(poly_array_2) - 1)] = dividendo // divisor
        poly_result[(len(poly_actual) - 1) - (len(poly_array_2) - 1)] = dividendo // divisor
        poly_actual2 = poly_mult_aux(aux, poly_array_2)
        poly_actual = poly_sub_aux(poly_actual, poly_actual2)
        if len(poly_actual) == 0:
            break
        else:
            while poly_actual[-1] == 0 and len(poly_actual) > 1:
                poly_actual.pop()

    return jsonify({'name' : poly_array_to_string(poly_result)})


@app.route('/plot', methods=['GET', 'POST'])
def change_features_1():
    '''Cria o grafico da funcao do polinomio'''
    feature = request.args['selected']  
    print(string_to_poly_array(feature))
    
    graphJSON= create_plot(string_to_poly_array(feature))

    return graphJSON


@app.route('/bar', methods=['GET', 'POST'])
def change_features_2():
    '''Cria o grafico da funcao do polinomio e marca os pontos das raizes'''
    feature = request.args['selected']  
    print("raz",string_to_poly_array(feature))
    
    graphJSON= create_plot_with_roots(string_to_poly_array(feature), pipeline(string_to_poly_array(feature)))

    return graphJSON


@app.route('/bar2', methods=['GET', 'POST'])
def change_features_3():
    '''Cria o grafico da funcao do polinomio e marca um ponto especifico'''
    feature = request.args['selected']  
    points = request.args['points']

    graphJSON= create_plot_with_point(string_to_poly_array(feature), int(points))
    
    return graphJSON

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
