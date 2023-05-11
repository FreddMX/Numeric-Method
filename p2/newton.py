import math
import sympy
from tabulate import tabulate

print('\n')

x = sympy.Symbol('x') # declarar x como símbolo

expr = input("\nIngrese la ecuación: ")
f_ORIGINAL = sympy.sympify(expr) # convertir la cadena de entrada en una expresión simbólica de sympy

f_DERIVADA = sympy.diff(f_ORIGINAL, x) # calcular la derivada de f(x)

x0 = float(input("Ingrese el valor inicial: "))

tolerance = 1e-15
max_iterations = 100

results = [] # lista para almacenar los resultados de cada iteración

for i in range(max_iterations):

    x1 = x0 - f_ORIGINAL.subs(x, x0) / f_DERIVADA.subs(x, x0) # evaluar la derivada en x0

    row = [i+1, f_ORIGINAL.subs(x, x0), f_DERIVADA.subs(x, x0), x0] # fila de resultados para la iteración actual
    results.append(row) # agregar la fila de resultados a la lista
    
    if abs(f_ORIGINAL.subs(x, x1)) < tolerance:
        print("La raíz es:", x1)
        break

    x0 = x1

    if i == max_iterations - 1:
        print("Hubo un error de convergencia después de", max_iterations, "iteraciones.")

# imprimir los resultados en una tabla
headers = ["Iteración", "f(xn)", "f'(xn)", "xn"]
print(tabulate(results, headers=headers, tablefmt="fancy_grid", floatfmt=".10f"))