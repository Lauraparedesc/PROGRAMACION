#lista
def mostrarLista (lista):
    for elemento in lista :
        print (elemento)

listaEdades = [20,18,18,18,21,20,18,18]
mostrarLista (listaEdades)

#mayor, menor, promedio
listaD = [20000,30000,4000,2500,1000,7600]
mayor = max (listaD)
menor = min (listaD)
totalSuma = 0
for elemento in listaD :
    totalSuma += elemento
promedio= round(totalSuma/len(listaD))
print ('El mayor ingreso fue de : ', mayor)
print ('El menor ingreso fue de : ', menor)
print ('El promedio de ingresos tiene un valor total de : ', promedio)

#salude n veces
def saludo (n = 0):
    print ('Hola, ' * n)
saludo (15)

#numeros pares
def paresLista(lista):
    pares = []
    for elemento in lista:
        if elemento % 2 == 0 :
            pares.append (elemento)
    return pares

numeros = [63, 24, 85, 16, 18, 25, 3, 2, 24]
numerosPares = paresLista(numeros)
print (numerosPares)

#numeros > 24
def mayores24 (lista):
    m24 = []
    for elemento in lista:
        if elemento > 24 :
            m24.append (elemento)
    return m24

numeros = [63, 24, 85, 16, 18, 25, 3, 2, 24]
numerosm24 = mayores24(numeros)
print (numerosm24)

#IMC
peso = float(input('Por favor ingresa tu peso en Kg : '))
altura = float(input('Por favor ingresa tu altura en metros : '))

def calcularIMC (peso, altura):
    return (peso / (altura ** 2))

print (calcularIMC(peso, altura))

#despedida
def despedida ():
    print ('Gracias por usar el codigo, hasta pronto!')
despedida ()
