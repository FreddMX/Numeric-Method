from tabulate import tabulate
from sympy import *

print('\n')

table = []
headers = ["X", "Y", "f(x,y)"]

print("METODO DE EULER (FUNCIONAL)\n")
coordinateX = float(input("Coordenada x del punto inicial (x0): "))
finalValue = float(input("Coordenada x del punto final (xf): "))
coordinateY = float(input("Coordenada y del punto inicial (y0): "))
increment = float(input("Incrementos (h): "))
function = input("Función (dy/dx): ")

x = Symbol('x')  # Definir la variable x
y = Symbol('y')  # Definir la variable y
funcOne = lambdify((x, y), eval(function))  # Convertir la función en una función numérica
cont = 0  # Contador
table.append([coordinateX, coordinateY, funcOne(coordinateX, coordinateY)])  # Evaluar la función en x0 y y0
tableFull = [[coordinateX, coordinateY, funcOne(coordinateX, coordinateY)]]  # Evaluar la función en x0 y y0

for i in range(int((finalValue-coordinateX)/increment)):
    x, y = (cont+1)*increment, tableFull[cont][1] + increment * funcOne(tableFull[cont][0], tableFull[cont][1])  # Actualizar x y y
    funcTwo = funcOne(x, y)  # Evaluar la función en x y y
    table.append([x, y, funcTwo])
    tableFull.append([x, y, funcTwo])
    cont += 1

print(tabulate(table, headers, tablefmt="fancy_grid", floatfmt=".8f"))
