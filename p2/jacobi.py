import math
from tabulate import tabulate
import sympy as sp

print('\n')

# Definir la precisión deseada del error absoluto
error = []
precision = float(input("\nINGRESE EL PORCENTAJE DE ERROR (0.01 EQUIVALE A 1%): "))
error.append([precision, "%"])

# Pedir al usuario que introduzca las ecuaciones
eq1_input = input("\nINGRESE LA ECUACION X1 DESPEJADA EN TERMINO DE X2 Y X3: ")
eq2_input = input("INGRESE LA ECUACION X2 DESPEJADA EN TERMINO DE X1 Y X3: ")
eq3_input = input("INGRESE LA ECUACION X3 DESPEJADA EN TERMINO DE X1 Y X2: ")

# Definir las ecuaciones y los valores iniciales de x1, x2 y x3
eq1 = lambda x2,x3: eval(eq1_input)
eq2 = lambda x1,x3: eval(eq2_input)
eq3 = lambda x1,x2: eval(eq3_input)

# Crear los símbolos de las variables x1, x2, x3
x1, x2, x3 = 0, 0, 0

# Definir la tabla para almacenar los resultados de cada iteración
tabla = []

# Definir la función para calcular el error absoluto
def error_absoluto(actual, anterior):
    return abs((actual - anterior) / actual) * 100

# Realizar las iteraciones hasta que el error absoluto sea menor al 1%
iteracion = 1
while True:
    # Calcular los nuevos valores de x1, x2 y x3 usando las ecuaciones y los valores actuales
    nuevo_x1 = eq1(x2,x3)
    nuevo_x2 = eq2(x1,x3)
    nuevo_x3 = eq3(x1,x2)

    # Calcular el error absoluto de cada variable
    error_x1 = error_absoluto(nuevo_x1, x1)
    error_x2 = error_absoluto(nuevo_x2, x2)
    error_x3 = error_absoluto(nuevo_x3, x3)

    # Agregar los valores de la iteración actual a la tabla
    tabla.append([iteracion, nuevo_x1, error_x1, nuevo_x2, error_x2, nuevo_x3, error_x3])

    # Comprobar si el error absoluto es menor al 1%
    if error_x1 < precision and error_x2 < precision and error_x3 < precision:
        break

    # Actualizar los valores de x1, x2 y x3 para la próxima iteración
    x1, x2, x3 = nuevo_x1, nuevo_x2, nuevo_x3

    # Incrementar el contador de iteración
    iteracion += 1

# Solicitar las ecuaciones y los valores iniciales de x1, x2 y x3 por teclado
eq1_str = input("\nINGRESA LA ECUACION ORIGINAL X1: ")
eq2_str = input("INGRESA LA ECUACION ORIGINAL X2: ")
eq3_str = input("INGRESA LA ECUACION ORIGINAL X3: ")

#Sustituir los valores finales de x1, x2 y x3 en las ecuaciones originales
resultado1 = eval(eq1_str)
resultado2 = eval(eq2_str)
resultado3 = eval(eq3_str)

# Imprimir la cantidad de error ingresada
tabla_headers = ["PORCENTAJE DE","ERROR INGRESADO"]
tabla_error = tabulate(error, headers=tabla_headers, tablefmt="fancy_grid")

print("\n" + tabla_error)

# Imprimir la tabla de las ecuaciones ingresadas
ecuaciones_headers = ["ECUACIONES ORIGINALES", "ECUACIONES DESPEJADAS"]
ecuaciones_ingresadas = [
    [eq1_str,   eq1_input],
    [eq2_str,   eq2_input],
    [eq3_str,   eq3_input]
]
ecuaciones_finales = tabulate(ecuaciones_ingresadas, headers=ecuaciones_headers, tablefmt="fancy_grid")
print("\n" + ecuaciones_finales)

# Imprimir la tabla de las iteraciones realizadas
print("\nTABLA DE RESULTADOS DE LAS ITERACIONES")
tabla_headers = ["Iteracion", "x1", "error absoluto x1", "x2", "error absoluto x2", "x3", "error absoluto x3"]
tabla_formateada = tabulate(tabla, headers=tabla_headers, floatfmt=".6f", tablefmt="fancy_grid")
print(tabla_formateada)

# Mensaje extra
tabla_headers = ["TABLA DE RESULTADOS FINALES DE LA ECUACION ORIGINAL"]
message_alert = [["REEMPLAZE LOS VALORES DE X1, X2, X3 EN LAS ECUACIONES SI QUIERE COMPROBAR LOS RESULTADOS"]]
message = tabulate(message_alert, headers=tabla_headers, tablefmt="fancy_grid")
print("\n" + message)

# Imprimir la tabla de resultados finales de las ecuaciones
ecuaciones_headers = ["ECUACIONES ORIGINALES", "VALORES FINALES DE X1, X3, X3", "RESULTADO FINAL"]
ecuaciones_valores = [
    [eq1_str,   f"X1 = {round(tabla[-1][1],6)}",     f"{resultado1:.6f}"],
    [eq2_str,   f"X2 = {round(tabla[-1][3],6)}",     f"{resultado2:.6f}"],
    [eq3_str,   f"X3 = {round(tabla[-1][5],6)}",     f"{resultado3:.6f}"]
]
ecuaciones_formateadas = tabulate(ecuaciones_valores, headers=ecuaciones_headers, tablefmt="fancy_grid")
print(ecuaciones_formateadas)


# TOTALMENTE FUNCIONAL