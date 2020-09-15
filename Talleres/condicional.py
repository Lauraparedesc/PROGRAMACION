#>,< O =
a = int (input("Ingrese el primer número entero : "))
b = int (input("Ingrese el segundo número entero : "))
print (a,b)

mensajeIgual = 'Los números ingresados son iguales'
mensajeMayor = 'El número {} es mayor que {}'

if (a > b):
    print(mensajeMayor.format(a , b))
elif (b > a):
    print(mensajeMayor.format(b , a))
else:
    print(mensajeIgual)
#EDAD USUARIO
edad = int (input('Ingresa tu edad por favor : '))

mensajeMenorE = 'Menor de edad'
mensajeJoven = 'Joven'
mensajeAdulto = 'Adulto'
mensajeAdultoM = 'Adulto mayor'

if (edad < 18):
    print(mensajeMenorE)
elif (edad >= 18 and edad <= 25):
    print(mensajeJoven)
elif (edad >= 26 and edad <= 60):
    print(mensajeAdulto)
else:
    print(mensajeAdultoM)
#AÑO ACTUAL
añoActual = int(input('Por favor ingrese el año actual : '))
añoX = int(input('Ahora ingresa cuaquier año : '))

msjañoigual = 'Los años ingresados son iguales'
msjañopasado = 'Entre los años ingresados han pasado {} años'
msjañofaltan = 'Para llegar al año ingresado aun faltan {} años'

if (añoActual > añoX):
    resta = añoActual - añoX
    print(msjañopasado.format(resta))
elif (añoX > añoActual):
    resta = añoX - añoActual
    print(msjañofaltan.format(resta))
else:
    print(msjañoigual)
#Distancia
print('Convertidor de Cm a Km, m, mm')
distanciaCm = float(input('Por favor ingresa la distancia en Cm : '))

preguntaMenu = float(input('''
Por favor ingrese una de las siguientes opciones :
            1- Convertir a Km
            2- Convertir a m
            3- Convertir a mm
    : ''')) 

if (preguntaMenu == 1):
    dividir = distanciaCm / 100000
    print(f'La distancia en kilometros es {dividir}')
elif (preguntaMenu == 2):
    dividir = distanciaCm / 100
    print (f'La distancia en Metros es {dividir}')
elif (preguntaMenu == 3):
    multiplicar = distanciaCm * 10
    print (f'La distancia en Milimitros es {multiplicar}')
else:
    print ('Entrada no valida')

print('Fin del programa')
