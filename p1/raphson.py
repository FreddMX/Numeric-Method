import math
import pandas as pd

print('\n')

def newton_raphson(f, df, x0, n):
    iteraciones = []
    valores_x = []
    valores_fx = []
    valores_dfx = []
    valores_err_abs = []
    valores_err_rel = []

    for i in range(n):
        x = x0 - f(x0)/df(x0)
        fx = f(x)
        dfx = df(x)
        err_abs = abs(x - x0)
        err_rel = abs(err_abs / x)

        iteraciones.append(i+1)
        valores_x.append(x)
        valores_fx.append(fx)
        valores_dfx.append(dfx)
        valores_err_abs.append(err_abs)
        valores_err_rel.append(err_rel)

        x0 = x

    err_rel_porcentual = [err * 100 for err in valores_err_rel]

    pd.set_option('display.float_format', lambda x: '%.10f' % x)
    df = pd.DataFrame({
        'Iteración': iteraciones,
        'x': valores_x,
        'f(x)': valores_fx,
        "f'(x)": valores_dfx,
        'Error Relativo': valores_err_rel,
        'Error Relativo (%)': err_rel_porcentual
    })

    return df

f = lambda x: math.exp(-x) - x
df = lambda x: -math.exp(-x) - 1
# f = lambda x: x * (math.log(x)) - 5
# df = lambda x: math.log(x) + 1

x0 = float(input("Introduce el valor inicial de x: "))
n = int(input("Introduce el número de iteraciones: "))

resultados = newton_raphson(f, df, x0, n)
print(resultados)
