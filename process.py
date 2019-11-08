from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

### Funcoes Auxiliares ###

def getDegreePoly(poly_array):
    i = 0
    degree = 0
    while i < len(poly_array):
        aux = poly_array[i]
        if aux == '^':
            if int(poly_array[i+1]) > degree:
                degree = int(poly_array[i+1])
        i += 1
    return degree


def string_to_poly_array(poly_str):
    """Converte um polinomio representado por string em um polinomio representado por vetor."""
    vector = [0] * (getDegreePoly(poly_str) + 1)
    # print(vector)
    poly_str = poly_str.replace(" ", "")
    current_monomium = ''
    i = 0
    while i < len(poly_str):
        if poly_str[i] == 'x':
            if(current_monomium == '' or current_monomium == '+'):
                if poly_str[i+1] == '^':
                    vector[int(poly_str[i+2])] = 1
                    i = i + 3
                else:
                    vector[1] = 1
                    i = i + 2
            elif(current_monomium == '-'):
                if poly_str[i+1] == '^':
                    vector[int(poly_str[i+2])] = -1
                    i = i + 3
                else:
                    vector[1] = 1
                    i = i + 2
            else:
                if poly_str[i+1] == '^':
                    vector[int(poly_str[i+2])] = int(current_monomium)
                    i = i + 3
                else:
                    vector[i] = int(current_monomium)
                    i = i + 2
            current_monomium = ""
        else:
            current_monomium = current_monomium + poly_str[i]
            i = i + 1
    if(current_monomium != ''):
        vector[0]= int(current_monomium)
  
    return vector

def poly_array_to_string(poly_array):
	"""Converte um polinomio representado por vetor em um polinomio representado por string."""
	i = len(poly_array)
	str_result = ""

	for i in range(i-1, -1, -1):
		if i == 0:
			if(poly_array[0] > 0):
				str_result = str_result + '+' + str(poly_array[0])
			elif(poly_array[0] < 0):
				str_result = str_result + str(poly_array[0])
			break

		elif i == 1:
			if (poly_array[i] > 1):
				str_result += "+{}x".format(poly_array[i])
			elif(poly_array[i] < -1):
				str_result += "{}x^".format(poly_array[i])
			elif(poly_array[i] == 1):
				str_result += "+x"
			elif(poly_array[i] == -1):
				str_result += "-x"

		else:
			if (poly_array[i] > 1):
				str_result += "+{}x^{}".format(poly_array[i], i)
			elif(poly_array[i] < -1):
				str_result += "{}x^{}".format(poly_array[i], i)
			elif(poly_array[i] == 1):
				str_result += "+x^{}".format(i)
			elif(poly_array[i] == -1):
				str_result += "-x^{}".format(i)

		if str_result[0] == '+':
			str_result = str_result[1:]

	return str_result


def poly_sub_aux(poly_array_1, poly_array_2):
	"""Calcula a subtracao de dois polinomios."""

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

	print(poly_result)
	return poly_result


def poly_mult_aux(poly_array_1, poly_array_2):
	"""Calcula a subtracao de dois polinomios."""
	print("mulr")
	poly_result = [0] * ((len(poly_array_1)-1) + (len(poly_array_2)-1) + 1)
	for i in range(0, len(poly_array_1)):
		for j in range(0, len(poly_array_2)):
			poly_result[i+j] += poly_array_1[i] * poly_array_2[j]
    
	return poly_result

### Fim das funcoes auxiliares ###

@app.route('/')
def index():
	return render_template('form.html')

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

	print(poly_result)
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
	"""Calcula a subtracao de dois polinomios."""
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
    
	while(len(poly_actual) >= len(poly_array_2)):
		aux = [0] * ((len(poly_array_1)-1) - (len(poly_array_2)-1) + 1)
		dividendo = poly_actual[-1]
		divisor = poly_array_2[-1]
		aux[(len(poly_actual) - 1) - (len(poly_array_2) - 1)] = dividendo // divisor
		poly_result[(len(poly_actual) - 1) - (len(poly_array_2) - 1)] = dividendo // divisor
		poly_actual2 = poly_mult_aux(aux, poly_array_2)
        poly_actual = poly_sub_aux(poly_actual, poly_actual2)
        while poly_actual[-1] == 0:
            poly_actual.pop()
    
	return jsonify({'name' : poly_array_to_string(poly_result)})


if __name__ == '__main__':
	app.run(debug=True)