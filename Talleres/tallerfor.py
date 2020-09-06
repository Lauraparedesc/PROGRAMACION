#-----sumatoria 0-100-----#
print("Sumatoria de números entre 0 y 100")
suma = 0 
for i in range (0,101):
    suma += i
print (f"El resultado de la suma es : {suma}")



#-----factorial-----#
print("Factorial")
preguntaNumero = "Por favor ingrese un número entero positivo : "
n = int(input(preguntaNumero))

def factorial (n):
    resultado = 1 
    for i in range (1, n + 1):
        resultado *= i 
    return resultado

print (factorial(n))



#-----6numeros-----#
cantidad = int(input("Cantidad de números a ingresar : "))

sumapositivos = 0
totalpositivos = 0
sumanegativos = 0

for i in range (cantidad):
    numero = int(input("Número : "))
    if (numero > 0) :
        sumapositivos += numero
        totalpositivos += 1
    else:
        sumanegativos += numero

print("Sumatoria de los negativos: ", sumanegativos)
if (totalpositivos != 0) :
    print("Promedio de los positivos: ",sumapositivos/totalpositivos)
else:
    print("No se ingresaron números positivos")



#-----canciones-----#
import random 

canciones = ["Adore you", 
        "Mad at Disney", 
        "Hawái",
        "Bye", 
        "Lost on you"]

for cancion in canciones :
    print (cancion)
aleatorio = random.randint(0,4)
print (f"Escogi esta canción para ti : {canciones[aleatorio]}")



