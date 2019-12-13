import numpy as np

### Funcoes Auxiliares ###

def getDegreePoly(poly_array):
    i = 0
    degree = 1
    while i < len(poly_array):
        aux = poly_array[i]
        if aux == '^':
          i+=1
          grau = ""
          while i < len(poly_array):
            if(poly_array[i] == '1' or poly_array[i] == '2' or poly_array[i] == '3' or poly_array[i] == '4' or poly_array[i] == '5' or poly_array[i] == '6' or poly_array[i] == '7' or poly_array[i] == '8' or poly_array[i] == '9' or poly_array[i] == '0'):
              grau = grau + poly_array[i]
              i += 1
            else:
              break
          if int(grau) > degree:
            degree = int(grau)
        i += 1
    return degree

def string_to_poly_array(poly_str):
    """Converte um polinomio representado por string em um polinomio representado por vetor."""
    if(poly_str == 'x' or poly_str == 'X'):
        return [0,1]
        
    vector = [0] * (getDegreePoly(poly_str) + 1)
    # print(vector)
    poly_str = poly_str.replace(" ", "")
    current_monomium = ''
    i = 0 #x^4+5x^3-4x^2-44x-48
    while i < len(poly_str):
        if poly_str[i] == 'x' or poly_str[i] == 'X':
            if(current_monomium == '' or current_monomium == '+'):
                if poly_str[i+1] == '^':
                    pos = ""
                    i = i + 2
                    while i < len(poly_str):
                      if poly_str[i] == '1' or poly_str[i] == '2' or poly_str[i] == '3' or poly_str[i] == '4' or poly_str[i] == '5' or poly_str[i] == '6' or poly_str[i] == '7' or poly_str[i] == '8' or poly_str[i] == '9' or poly_str[i] == '0':
                        pos = pos + poly_str[i]
                        i += 1
                      else:
                        break
                    vector[int(pos)] = 1
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
                    pos = ""
                    i = i + 1
                    while i < len(poly_str):
                      if poly_str[i] == '1' or poly_str[i] == '2' or poly_str[i] == '3' or poly_str[i] == '4' or poly_str[i] == '5' or poly_str[i] == '6' or poly_str[i] == '7' or poly_str[i] == '8' or poly_str[i] == '9' or poly_str[i] == '0':
                        pos = pos + poly_str[i]
                        i += 1
                      else:
                        break
                    vector[int(pos)] = int(current_monomium)
                    i = i + 3
                else:
                    vector[1] = int(current_monomium)
                    i = i + 1
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
    print(poly_array)
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
    
    if len(str_result) == 0:
        return 0
        
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

	return poly_result


def poly_mult_aux(poly_array_1, poly_array_2):
	"""Calcula a subtracao de dois polinomios."""
	poly_result = [0] * ((len(poly_array_1)-1) + (len(poly_array_2)-1) + 1)
	for i in range(0, len(poly_array_1)):
		for j in range(0, len(poly_array_2)):
			poly_result[i+j] += poly_array_1[i] * poly_array_2[j]
    
	return poly_result


def descartes(poly_array):
    """ Retorna uma matriz de possibilidades de raizes reais positivas (coluna 0) / reais negativas (coluna 1) / complexas  (coluna 2) """
    poly_array_aux = [ x for x in poly_array if x is not 0 ]

    positive_alternate_signs = 0
    i = 0
    while i <= len(poly_array_aux) - 2:
        aux_1 = poly_array_aux[i]
        aux_2 = poly_array_aux[i+1]
        if (aux_1 > 0 and aux_2 < 0) or (aux_1 < 0 and aux_2 > 0):
            positive_alternate_signs += 1
        i += 1
 
    negative_alternate_signs = 0
    i = 0
    poly_array_aux = poly_array[:]
    for i in range(len(poly_array_aux)):
        if (i % 2) != 0:
            poly_array_aux[i] = - poly_array_aux[i]
    poly_array_aux = [ x for x in poly_array_aux if x is not 0 ]
    i = 0
    while i <= len(poly_array_aux) - 2:
        aux_1 = poly_array_aux[i]
        aux_2 = poly_array_aux[i+1]
        if (aux_1 > 0 and aux_2 < 0) or (aux_1 < 0 and aux_2 > 0):
            negative_alternate_signs += 1    
        i += 1

    degree = len(poly_array) - 1
    x = (positive_alternate_signs // 2) + 1
    y = (negative_alternate_signs // 2) + 1
    possible_pos_roots = [positive_alternate_signs - 2*i for i in range(x) if (positive_alternate_signs - 2*i) >= 0]
    possible_neg_roots = [negative_alternate_signs - 2*i for i in range(y) if (negative_alternate_signs - 2*i) >= 0]
    possibility_matrix = [[ 0 for i in range(3) ] for j in range(x*y)]

    k = 0
    for i in possible_pos_roots:
        for j in possible_neg_roots:
            possibility_matrix[k][0] = i
            possibility_matrix[k][1] = j
            possibility_matrix[k][2] = degree - (i+j)
            k += 1
    
    return possibility_matrix


def complex_roots_tests(poly_array):
    t = len(poly_array)
    if poly_array[0] == 0 and poly_array[1] == 0:
            return True
    for i in range(1, t-2):
        if poly_array[i]**2 <= poly_array[i-1] * poly_array[i+1]:
            return True
        if poly_array[i] == 0 and poly_array[i-1] * poly_array[i+1] > 0:
            return True
        if poly_array[i] == 0 and poly_array[i+1] == 0:
            return True
    return False
    

def fujiwara(poly_array):
        t = len(poly_array)
        n = t - 1
        d = poly_array[n]
        partial_results =  [0] * t
        for i in range(0, n):
            partial_results[i] = abs(poly_array[i]/d) ** (1/(n-i))
        return 2*max(partial_results)

def poly_evaluate(poly_array, value):
        result = 0
        for i in range(0, len(poly_array)):
            result += poly_array[i] * (value ** i)
        return result

def poly_evaluate_list(poly_array, values):
        result = []
        sum = 0
        for value in values:
            for i in range(1, len(poly_array)):
                sum += poly_array[i] * (value ** i)
            result.append(sum + poly_array[0])
            sum = 0
        return result

def derivate(poly_array):
    poly_result = poly_array[:]
    poly_result.pop(0)
    for i in range(len(poly_result)):
        poly_result[i] = poly_result[i] * (i+1)
    return poly_result

def separate_roots(poly_array, bound1, bound2):
    values_for_x0 = []
    step = (bound1*2) / 1000
    previous_eval = poly_evaluate(poly_array, bound1)
    if (previous_eval == 0):
        values_for_x0.append(bound1)

    for x in np.arange(bound1, bound2, abs(step)):
        current_eval = poly_evaluate(poly_array, x)
        if (previous_eval > 0 and current_eval < 0)  or (previous_eval < 0 and current_eval > 0) :
            values_for_x0.append(x)
        if (current_eval == 0):
            values_for_x0.append(x)
        previous_eval = current_eval
    
    return values_for_x0

def newton(poly_array, derivate_array, x0, epsilon, max_iter):
    curr_x = x0
    new_x = 0
    iter_count = 0
    while iter_count < max_iter:
        func_eval = poly_evaluate(poly_array, curr_x)
        der_eval = poly_evaluate(derivate_array, curr_x)
        if(func_eval == 0):
            return curr_x
        if der_eval != 0:
            new_x = curr_x - (func_eval / der_eval)
            if abs(new_x - curr_x) <= epsilon:
                return new_x
        curr_x = new_x
        iter_count += 1
    
    return curr_x    

def pipeline(poly_array):

    print("Pipeline starting...")

    complex_bool = complex_roots_tests(poly_array)
    descartes_matrix = descartes(poly_array)
    alpha = fujiwara(poly_array)
    derivate_array = derivate(poly_array)

    descartes_matrix_m = "[+, -, c]<br>"

    for item in descartes_matrix:
        descartes_matrix_m += "                  " + str(item)

    print(descartes_matrix)
    print(descartes_matrix_m)

    x0_list = separate_roots(poly_array, -alpha, alpha)
    found_roots = []
    epsilon = 0.00000001 # HARD-CODED
    max_iter = 100       # HARD-CODED
    for x0 in x0_list :
        found_roots.append(newton(poly_array, derivate_array, x0, epsilon, max_iter))

    for i in range(len(found_roots)):
        if (abs(found_roots[i] - round(found_roots[i]))) <= 0.001:
            found_roots[i] = round(found_roots[i])

    # TODO not using descartes so far

    return [complex_bool, descartes_matrix_m, alpha, derivate_array, x0_list, found_roots]