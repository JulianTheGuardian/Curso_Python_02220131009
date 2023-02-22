# Condicional if-elif-else

print("Digite un numero")
numero = int(input())

if numero > 0:
    print("El numero es positivo..")

elif numero == 0:
    print("El numero es 0.")

else:
    print("El numero es negativo.")   

# do-while

while True:
    print("Digite la letra 'A' para Actualizar Sistema")
    print("Digite la letra 'E' para Eliminar Catalogo")
    print("Digite la letra 'C' para Crear Productos")
    print("Digite la letra 'S' para Salir del Programa")
    letra = str(input())
    
    if letra == 'S' or letra == 's':
        print("Finalizado con exito \n")
        break
    
    elif letra == 'A' or letra == 'a':
        print("Se actualizo el sistema \n")
        break

    elif letra == 'E' or letra == 'e':
        print("Se elimino el catalogo \n")
        break
    
    elif letra == 'C' or letra == 'c':
        print("Se creo un producto \n")
        break
    
    else: 
        print("Sigue dentro del proceso del do-while \n")

print("Finalizo el do-while \n")    

# while

num = 1
while num != 0:
    print("Digite un numero")
    num = int(input())

    if num%2 == 0:
        print("El numero es par")

    else:
        print("El numero es impar")

print("El programa finalizo")  

# for
suma = 0

for i in range(0,10,1):
    print("Digite el numero " + str(i+1) + ": ")
    numero = int(input())
    suma = suma + numero

print("La sumatoria total es: " +str(suma))

# el fish (match)

print("Digite un numero del 1 al 12")
num = int(input())

match num:
    case 1:
        print("Enero")
    case 2:
        print("Febrero") 
    case 3: 
        print("Marzo")
    case 4: 
        print("Abril")
    case 5:
        print("Mayo")
    case 6:
        print("Junio")
    case 7:
        print("Julio")
    case 8:
        print("Agosto")
    case 9: 
        print("Septiembre")
    case 10:
        print("Octubre") 
    case 11: 
        print("Noviembre")
    case 12:
        print("Diciembre el mejor mes")        
                                                  