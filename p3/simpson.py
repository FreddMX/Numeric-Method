import sympy as sp
import matplotlib.pyplot as plt
from numpy import e
from tabulate import tabulate
from sympy import E as e

print('\n')

# Definimos la función para evaluar los valores de y
def evaluar_y(f, x):
    f_lambdified = sp.lambdify(sp.Symbol('x'), f)
    # f_lambdified = sp.lambdify(sp.Symbol('x'), f, modules={"x": np})
    return f_lambdified(x)

# Pedimos los datos al usuario
numINTER = int(input("Ingrese el numero de intervalos: "))  #15 12 4
interXI = float(input("Ingrese el valor de xi: "))          #1 -1
interXF = float(input("Ingrese el valor de xf: "))          #5 1
funcion = input("Ingrese la función en términos de x: ")    #5 * x**2 - (x/3)  e**(-x**2)
# f = sp.sympify(funcion)
f = sp.sympify(funcion.replace("e", str(e)))
with open("funcion.txt", "w") as archivo:
    archivo.write(funcion)

# Calculamos el tamaño de los subintervalos
tempH = (interXF-interXI)/numINTER

# Calculamos los valores de y para cada subintervalo
num = []
dateX = []
replaceX = []
for startINTER in range(numINTER+1):
    startINTER + 1
    num.append(startINTER)
    if startINTER == 0:
        dateX.append(interXI)
    else:
        interXI += tempH
        dateX.append(interXI)    
    replaceX.append(evaluar_y(f, dateX[startINTER]))

# Mostramos la tabla de valores
data = []
for i in range(numINTER+1):
    data.append([i+1, dateX[i], replaceX[i]])

headers = ["Iteracion", "X", "Y"]
print(tabulate(data, headers=headers, tablefmt="fancy_grid", floatfmt=".10f"))

# Calculamos la integral usando la fórmula que mencionaste
suma_pares = sum([replaceX[i] for i in range(2, numINTER, 2)])
suma_impares = sum([replaceX[i] for i in range(3, numINTER, 2)])
integral = (tempH/3) * (replaceX[0] + 4*suma_pares + 2*suma_impares + replaceX[-1])

# Mostramos el resultado
print("El valor de la integral es:", integral)

