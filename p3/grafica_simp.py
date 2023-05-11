import matplotlib.pyplot as plt
import numpy as np
from simpson import dateX, replaceX, numINTER
import os
from math import e
from tabulate import tabulate

print('\n')

with open("funcion.txt", "r") as archivo:
    funcion = archivo.read()

def f(x):
    return eval(funcion)

x = np.linspace(dateX[0], dateX[-1], 100)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, color='blue')
ax.axhline(y=0, color='black')
ax.axvline(x=0, color='black')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Grafica de f(x) = ' + funcion)

# Aplicar metodo de Simpson 1/3 en cada subintervalo
n = len(dateX) - 1
integral = 0
for i in range(n):
    a = dateX[i]
    b = dateX[i+1]
    h = (b-a)/2
    x_sub = np.linspace(a, b, 3)
    y_sub = f(x_sub)
    area_i = (h/3) * (y_sub[0] + 4*y_sub[1] + y_sub[2])
    integral += area_i
    ax.fill_between(x_sub, y_sub, color='yellow', alpha=0.3)
    ax.plot([a, a], [0, f(a)], linestyle='--', color='red')
    ax.plot([b, b], [0, f(b)], linestyle='--', color='red')


plt.show()
