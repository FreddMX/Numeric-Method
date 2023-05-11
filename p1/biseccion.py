import math
import pandas as pd
import matplotlib.pyplot as plt

print('\n')

def f(c, t):
    # return (((68.1 * 9.81) / c) * (1 - math.e ** ((-c / 68.1) * t)) - 40)
    return ((c**3) + (c**2) - (3*(c)) - (3))

c_inferior = float(input("\nIngrese el valor inferior de X: "))
c_superior = float(input("Ingrese el valor superior de X: "))
t = 10
max_iteraciones = int(input("Ingrese el número de iteraciones a realizar: "))
tolerancia = float(input("Ingrese la precision de la raiz: "))

list_c_medio = []
list_f_c_medio = []

i = 0
while i < max_iteraciones:
    c_medio = (c_inferior + c_superior) / 2
    if abs(f(c_medio, t)) < tolerancia:
        break
    elif f(c_inferior, t) * f(c_medio, t) < 0:
        c_superior = c_medio
        list_c_medio.append(c_medio)
        list_f_c_medio.append(f(c_medio, t))
    else:
        c_inferior = c_medio
        list_c_medio.append(c_medio)
        list_f_c_medio.append(f(c_medio, t))
    i += 1

df = pd.DataFrame({"Iteración": range(len(list_c_medio)), "X": list_c_medio, "f(X)": list_f_c_medio})
df.set_index("Iteración", inplace=True)
print('\n==================================')
print("ECUACION: X^3 + X^2 - 3(X) - 3")
print('==================================\n')
print(df)
print(" ")
print("El valor real de la raiz es 1.7321 y tiene\ncomo paridad la 11 iteracion con valor en\n'X = 1.732178' y 'f(X) = 0.001201'")
print('\n==================================')

