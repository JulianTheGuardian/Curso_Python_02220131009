print("Hola new worl")


# Ejercicio 1

print("Digite numero entero y positivo")

Numero = int(input())
cont = 0
total = 0

while Numero != cont:
    cont = cont + 1
    total = total + cont

print("La sumatoria del rango es: " + str(total))

# Ejercicio 2

print("Digite numero entero y positivo")

Numero2 = int(input())
cont2 = 0
totalPar= 0
totalImpar = 0

while Numero2 != cont2:
    cont2 = cont2 + 1
    if cont2 % 2 == 0:
        totalPar = totalPar + cont2
    else:
         totalImpar = totalImpar + cont2

print("La sumatoria de los impares es: " + str(totalImpar))
print("La sumatoria de los pares es: " + str(totalPar))