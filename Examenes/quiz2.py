listaPesos = [20000,30000,4000,2500,1000,7600]
preguntaMenu = '''
Por favor ingrese alguna de estas opciones:
            1- Convertir pesos 
            2- Agregar un valor a la lista 
            3- Ver máximo, minimo y promedio de ingresos 
            4- Eliminar un valor de la lista 
            5- Para salir del programa
: '''
preguntaConversionPesos = '''
Por favor ingrese alguna de estas opciones:
            C- Convertir a pesos colombianos
            D- Convertir a dolares
            E- Convertir a euros
: '''

msjNovalidoN = 'Recuerda ingresar una opción valida : 1,2,3,4,5'
msjNovalidoC = 'Recuerda ingresar una opción valida : C,D,E'
mensajeSalida = 'Gracias por usar el programa'
mensajePesos = 'No es necesaria la conversión, pero se muestra la lista'

opcion = int(input(preguntaMenu))
listaD = []
listaE = []
listaC = listaPesos

for elemento in listaC:
    dolares = elemento * 0.00027
    listaD.append (dolares)
for elemento in listaC:
    euros = elemento * 0.00023
    listaE.append (euros)

mayor = max (listaC)
menor = min (listaC)
totalSuma = 0
for elemento in listaPesos :
    totalSuma += elemento
promedio= round(totalSuma/len(listaPesos))

while (opcion != 5):
    if (opcion == 1):
        conversion = input(preguntaConversionPesos)
        if (conversion == 'C'):
            print (mensajePesos)
            print (listaC)
        elif (conversion == 'E'):
            print (listaE)
        elif (conversion == 'D'):
            print (listaD)
        else:
            print (msjNovalidoC)
    elif (opcion == 2):
        agregar = int(input('Ingresa el valor que deseas agregar : '))
        listaC.append(agregar)
        print (listaC)
    elif (opcion == 3):
        print ('El mayor ingreso fue de : ', mayor)
        print ('El menor ingreso fue de : ', menor)
        print ('El promedio de ingresos tiene un valor total de : ', promedio)
    elif (opcion == 4):
        print (listaC)
        quitar = int(input('Ingresa la posición que deseas eliminar comenzando por 0 como primera posción : '))
        listaC.pop(quitar)
        print (listaC)
    else:
        print(msjNovalidoN)
    opcion = int(input(preguntaMenu))

print(mensajeSalida)