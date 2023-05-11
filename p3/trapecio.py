import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

print('\n')

def calcular_error(a, b, f):
    x = sp.Symbol('x')
    secondDerivative = sp.diff(f, x, 2)

    if secondDerivative == 0:  # La segunda derivada es cero
        print("La función es lineal, no se puede calcular el error.") 
    else:  # La función no es lineal
        biEI = b - a
        stepFour = -(1/12) * secondDerivative.evalf(subs={x: biEI}) * (biEI)**3
        print("Error calculado: " + str(round(stepFour,5)))

x = sp.Symbol('x')
funcion = input("Ingrese la función en términos de x: ") # x**3 - 6*x**2 + 11*x - 6        #2*x + 3
f = sp.sympify(funcion) # Convierte la entrada en una expresión simbólica

a = float(input("Ingrese el valor de a: ")) #1.3                                           #1
b = float(input("Ingrese el valor de b: ")) #1.8                                           #5

stepOneA = f.subs(x, a)   # paso 1
stepOneB = f.subs(x, b)
stepTwo = (b-a)/2 # paso 2
stepThree = stepTwo*(stepOneA + stepOneB) # paso 3

print("""
    El valor del intervalo 'a' es: {}
    El valor del intervalo 'b' es: {}
    Resultado obtenido al aplicar la regla del trapecio: {}
""".format(round(stepOneA, 5), round(stepOneB, 5), round(stepThree, 5)))

calcular_error(a, b, f)

# Graficar la función
expr = sp.lambdify(x, f, "numpy")
x_vals = np.linspace(a - 1, b + 1, 1000)
y_vals = expr(x_vals)

fig, ax = plt.subplots()
ax.plot(x_vals, y_vals)

# Marcar los intervalos a y b
ax.axvline(x=a, color='r', linestyle='--', label='a')
ax.axvline(x=b, color='y', linestyle='--', label='b')
ax.legend()

plt.show()