import math
import statistics

print('\n')

date = int(input("Cuantos valores vas a ingresar: "))
unit = input("Especifique su unidad de medida: ")

# INGRESAR TODOS LOS DATOS
valores = []
for i in range(date):
    digit = 1
    medicion = float(input('Ingresa la medicion num.{}: '.format(digit+i)))
    valores.append(medicion)
print("\nLos valores ingresados son \n"+str(valores))

# CONTAR CUANTOS DECIMALES TIENEN LAS MEDICIONES
datosNum = str(valores[i])
longitud = len(datosNum)
indice = -1
salir = False

while salir == False:
    indice = indice + 1
    if(datosNum[indice] == ".") or (longitud - 1 == indice):
        salir = True
        if longitud - 1 == indice:
            indice = indice + 1

# print("EN LA IZQUIERDA DEL PUNTO DECIMAL HAY",indice, "DIGITOS")
# print("DESPUES DEL PUNTO DECIMAL HAY",longitud - indice - 1)
valueDecimal = longitud - indice -1

# CALCULAR LA MEDIA DE LOS VALORES INGRESADOS
media = statistics.mean(valores)

# RESTAR CADA MEDIDA INGRESADA CON LA MEDIA CALCULADA
resSustract = []
for sustract in range(date):
    net = valores[sustract] - media
    resSustract.append(net)

# ELEVAR CADA VALOR OBTENIDO DE LA RESTA AL CUADRADO
potence = []
for eleved in range(date):
    elevado = resSustract[eleved] ** 2
    potence.append(elevado)

# SUMAR TODOS LOS VALORES
suma = sum(potence)
# SUSTITUIR Y CALCULAR EL VALOR DE 'N'
functionEX = date * (date-1)
# SUSTITUIR LOS VALORES DE LA FUNCION
error = round(math.sqrt(suma/functionEX), valueDecimal)

if unit == "m" or "M" or "kg" or "KG":
    errorInstrumento = 0.01
elif unit == "cm" or "CM":
    errorInstrumento = 0.001
elif unit == "h" or "H":
    errorInstrumento = 1
    
print(f'\nLA MEDIA ES: \n' + str(media))
print('\nLA RESTA DE LOS VALORES CON LA MEDIA ES:')
for valueSustract in resSustract:
    print(valueSustract) 

print('\nLA RESTA DE LOS VALORES CON LA MEDIA ELEVADA AL CUADRADO ES:')
for valuePotence in potence:
    print(valuePotence)
    
print(f'\nLA SUMA DE LAS MEDIDAD ANTERIORES ES: \n{suma:.5f}')
print('\nEL VALOR DE N*(N-1) ES: \n' + str(functionEX))
print('\nEL RESULTADO DE LA RAIZ ES: \n' + str(error) + '\n')

print("EL RESULTADO FINAL ES:")
print('d={} ± {} {}'.format(str(media), str(error), str(unit)))
print(f'\nEL ERROR (e) DEL INSTRUMENTO EQUIVALE A {errorInstrumento} {unit}')

