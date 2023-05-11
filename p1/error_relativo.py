import numpy as np

print('\n')

valorExacto = float(input("Ingrese el valor exacto (Vex): "))
errorRelativoMinMax = float(input("Cual es su menor o maximo Error Relativo: "))
cant_erroresAbsolutos = int(input("Cuantos errores absolutos (e) desea ingresar: "))

Absolut_Error = []
for erroresAbsolutos in range(cant_erroresAbsolutos):
    num = 1
    ErrorAbsoluto = float(input(f'Ingrese el error absoluto (e) n.{num+erroresAbsolutos}: '))
    Absolut_Error.append(ErrorAbsoluto)

print("")
for error in range(cant_erroresAbsolutos):
    num = 1
    print(f'El error absoluto n.{num+error} equivale a "{Absolut_Error[error]:.0f}"')
# print(Absolut_Error)

print("")
Relative_Error = []
for erroresRelativos in range(cant_erroresAbsolutos):
    ErrorRelativo = (Absolut_Error[erroresRelativos] / valorExacto) * (100)
    Relative_Error.append(ErrorRelativo)
# print(f'El porcentaje de error de cada valor ingresado es: {Relative_Error}')

for datos in range(cant_erroresAbsolutos):
    print(f'El porcentaje de error relativo de "{Absolut_Error[datos]:.0f}" es {Relative_Error[datos]:.2f}%')

print("")
min = errorRelativoMinMax
for run in Relative_Error:
    if run < min:
        min = run
# print(f'El porcentaje de error mas bajo es {min:.1f}%\n')

print(f'Segun mis calculos el error relativo equivalente a {min:.2f}% es el mas preciso.')
