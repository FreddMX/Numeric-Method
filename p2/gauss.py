import numpy as np
from tabulate import tabulate

print('\n')

def gauss_seidel(A, b, x0, max_iter, min_error):
    n = len(b)
    x = x0.copy()
    iter_count = 0
    error = 1

    iter_values = []

    while iter_count < max_iter and error > min_error:
        x_prev = x.copy()
        # devuelve una matriz en ceros
        x_error = np.zeros(n)

        for i in range(n):
            # Calcula la suma de los términos de la fila i que ya han sido actualizados
            s1 = np.dot(A[i, :i], x[:i])

            # Calcula la suma de los términos de la fila i que aún no se han actualizado
            s2 = np.dot(A[i, i + 1:], x_prev[i + 1:])

            # Calcula el nuevo valor para x[i] a partir de las sumas y el término independiente
            x[i] = (b[i] - s1 - s2) / A[i, i]

            # Calcula el error relativo de la variable x[i]
            x_error[i] = np.abs((x[i] - x_prev[i]) / x[i])

        # Añade los valores de iteración, x y error a la lista iter_values
        iter_values.append((iter_count+1, *[round(val, 5) for val in x], *[round(error * 100, 5) for error in x_error]))

        # Calcula el error máximo entre los errores relativos de las variables
        error = np.max(x_error)
        iter_count += 1

    # Verifica si se ha alcanzado el umbral de error mínimo
    if error <= min_error:
        print(f"\nEL METODO HA OBTENIDO UN RESULTADO CON UN ERROR MENOR AL {min_error*100}% DESPUES DE {iter_count} ITERACIONES.")
        print(f"RESULTADO: {x}.\nLA ITERACION {iter_count} ESTA CON UN ERROR DE {[error * 100 for error in x_error]}%\n")
        headers = ["iteracion", *[f"valor x{i+1}" for i in range(n)], *[f"error x{i+1}" for i in range(n)]]
        print(tabulate(iter_values, headers=headers, tablefmt="fancy_grid")+'\n')
        return x, iter_count
    else:
        print(f"\nEl método de Gauss-Seidel no llega a ningún resultado antes de {iter_count} iteraciones.")
        return None

print("METODO DE GAUSS-SEIDEL")
print("Ingrese la cantidad de ecuaciones:")
n = int(input())
print("Ingrese el porcentaje de error:")
min_error = float(input()) / 100
A = np.zeros((n, n))
b = np.zeros(n)

for i in range(n):
    for j in range(n):
        print(f"Ingrese el valor de la incógnita {j+1} en la ecuación {i+1}: [{i+1},{j+1}]:")
        A[i][j] = float(input())
    print(f"Ingrese el resultado de la ecuación {i+1} [{i+1},{n+1}]:")
    b[i] = float(input())

# devuelve una ventana de matrices de cero
x0 = np.zeros_like(b)

solucion, iteraciones = gauss_seidel(A, b, x0, 100, min_error)

# Crear una lista de diccionarios para cada iteración
tabla_iteraciones = []
for i in range(iteraciones):
    iteracion = i+1
    valores = solucion.tolist()
    errores = [(error * 100) for error in ((solucion - x0) / solucion)]
    x0 = solucion.copy()

# Crear el diccionario con los datos de la iteración actual
iteracion_dict = {"Iteración": iteracion}
for j in range(n):
    iteracion_dict[f"Valor x{j+1}"] = valores[j]
    iteracion_dict[f"Error x{j+1}"] = errores[j]
tabla_iteraciones.append(iteracion_dict)


# Imprimir la tabla utilizando el módulo tabulate
# encabezado = ["Iteración"] + [f"Valor x{i+1}" for i in range(n)] + [f"Error x{i+1}" for i in range(n)]
# filas = [[iteracion_dict["Iteración"]] + [iteracion_dict[f"Valor x{i+1}"] for i in range(n)] + [iteracion_dict[f"Error x{i+1}"] for i in range(n)] for iteracion_dict in tabla_iteraciones]
# print(tabulate(filas, headers=encabezado, tablefmt="fancy_grid"))






# FUNCIONA CORRECTAMENTE