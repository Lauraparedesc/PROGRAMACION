listaDolares = [20000,30000,4000,2500,1000,7600]

preguntaMenu = '''
Por favor ingrese alguna de estas opciones:
            1- Convertir dolares 
            2- Mostrar categoria de ingresos
            3- Ver máximo, minimo y promedio de ingresos 
            4- Para salir del programa
: '''
preguntaConversionDolares = '''
Por favor ingrese alguna de estas opciones:
            C- Convertir a pesos colombianos
            D- Convertir a dolares
            E- Convertir a euros
: '''
msjNovalidoN = 'Recuerda ingresar una opción valida : 1,2,3,4'
msjNovalidoC = 'Recuerda ingresar una opción valida : C,D,E'

mensajeSalida = 'Gracias por usar el programa'
mensajeDolares = 'No es necesaria la conversión, pero se muestra la lista'

opcion = int(input(preguntaMenu))
listaC = []
listaE = []
listaD = listaDolares
listaingresos = []

for elemento in listaD:
    pesos = elemento * 3700
    listaC.append (pesos)
for elemento in listaD:
    euros = elemento * 0.84
    listaE.append (euros)
for elemento in listaD:
    estado = ''
    if (elemento <= 1000 ):
        estado = 'Bajos ingresos'
    elif (elemento > 1000 and elemento < 7000):
        estado = 'Ingresos medios'
    elif (elemento >= 7000 and elemento < 20000):
        estado = 'Ingresos altos'
    else:
        estado = 'Ingresos elevados'
    listaingresos.append(estado)
mayor = max (listaD)
menor = min (listaD)
totalSuma = 0
for elemento in listaDolares :
    totalSuma += elemento
promedio= round(totalSuma/len(listaDolares))

while (opcion != 4):
    if (opcion == 1):
        conversion = input(preguntaConversionDolares)
        if (conversion == 'C'):
            print (listaC)
        elif (conversion == 'E'):
            print (listaE)
        elif (conversion == 'D'):
            print (mensajeDolares)
            print (listaD)
        else:
            print (msjNovalidoC)
    elif (opcion == 2):
        print (listaingresos)
    elif (opcion == 3):
        print ('El mayor ingreso fue de : ', mayor)
        print ('El menor ingreso fue de : ', menor)
        print ('El promedio de ingresos tiene un valor total de : ', promedio)
    else:
        print(msjNovalidoN)
    opcion = int(input(preguntaMenu))

print(mensajeSalida)

