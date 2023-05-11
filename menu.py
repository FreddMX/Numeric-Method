import os

def ejecutar_archivo(archivo):
    if os.path.exists(archivo):
        os.system('python ' + archivo)
    else:
        print("El archivo no existe.")

def submenu_p1():
    while True:
        print("\nSUBMENÚ Parcial 1")
        print("1. Error absoluto")
        print("2. Error relativo")
        print("3. Biseccion")
        print("4. Newton-Raphson")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejecutar_archivo('p1/error_absoluto.py')
        elif opcion == "2":
            ejecutar_archivo('p1/error_relativo.py')
        elif opcion == "3":
            ejecutar_archivo('p1/biseccion.py')
        elif opcion == "4":
            ejecutar_archivo('p1/raphson.py')
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def submenu_p2():
    while True:
        print("\nSUBMENÚ Parcial 2")
        print("1. Jacobi")
        print("2. Gauss Seidel")
        print("3. Newton")
        print("4. Lagrange")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejecutar_archivo('p2/jacobi.py')
        elif opcion == "2":
            ejecutar_archivo('p2/gauss.py')
        elif opcion == "3":
            ejecutar_archivo('p2/newton.py')
        elif opcion == "4":
            ejecutar_archivo('p2/lagrange.py')
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def submenu_p3():
    while True:
        print("\nSUBMENÚ Parcial 3")
        print("1. Trapecio")
        print("2. Simpson 1/3")
        print("3. Euler")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejecutar_archivo('p3/trapecio.py')
        elif opcion == "2":
            ejecutar_archivo('p3/grafica_simp.py')
        elif opcion == "3":
            ejecutar_archivo('p3/euler.py')
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def mostrar_menu_principal():
    print("MENU PRINCIPAL")
    print("1. Parcial 1")
    print("2. Parcial 2")
    print("3. Parcial 3")
    print("4. Salir")

while True:
    mostrar_menu_principal()
    opcion_principal = input("Seleccione una opción: ")

    if opcion_principal == "1":
        submenu_p1()
    elif opcion_principal == "2":
        submenu_p2()
    elif opcion_principal == "3":
        submenu_p3()
    elif opcion_principal == "4":
        break
    else:
        print("Opción inválida. Intente nuevamente.")
