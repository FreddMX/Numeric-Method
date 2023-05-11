from tabulate import tabulate

print('\n')

def lagrange(x, y, z):
    n = len(x)
    L = [0]*n
    for i in range(n):
        p = 1
        for j in range(n):
            if j != i:
                p *= (z - x[j])/(x[i] - x[j])
        L[i] = p
    return sum(y[i]*L[i] for i in range(n))

n = int(input("Ingrese la cantidad de datos: "))
x = []
y = []

for i in range(n):
    xi = float(input("Ingrese la coordenada x{}: ".format(i+1)))
    yi = float(input("Ingrese la coordenada y{}: ".format(i+1)))
    x.append(xi)
    y.append(yi)

z = float(input("Ingrese el valor inicial de x: "))

L = [0]*n
y_L = [0]*n
for i in range(n):
    p = 1
    for j in range(n):
        if j != i:
            p *= (z - x[j])/(x[i] - x[j])
        L[i] = p
        y_L[i] = y[i]*p

resultado = lagrange(x, y, z)

# Imprimir tabla
tabla = []
for i in range(n):
    tabla.append([i+1, x[i], y[i], L[i], y_L[i]])

headers = ["#", "x", "y", "L(x)", "y*L(x)"]
print(tabulate(tabla, headers=headers, tablefmt="fancy_grid", floatfmt=".5f"))

print("El resultado de la interpolación en x={} es: {:.5f}".format(z, resultado)+'\n')
