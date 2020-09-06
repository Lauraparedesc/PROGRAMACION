#-----Numeroteclado-----#
preguntaNumero = "Ingrese un número entero o digite cero para finalizar y realizar la sumatoria : "

numeroIngresado = int(input(preguntaNumero))
suma = 0
while(numeroIngresado != 0) :
    suma += numeroIngresado
    numeroIngresado = int(input(preguntaNumero))

print(f"Este es el resultado de la sumatoria {suma}")



#-----2numerosenteros-----#
preguntaNumero1 = "Por favor ingresa el primer número entero : "
preguntaNumero2 = "Por favor ingresa el segundo número entero : "

numeroIngresado1 = int(input(preguntaNumero1))
numeroIngresado2 = int(input(preguntaNumero2))

while(numeroIngresado2 <= numeroIngresado1) :
    print ("Por favor digita un número mayor que el primero")
    numeroIngresado2 = int(input(preguntaNumero2))

print (f"{numeroIngresado1} , {numeroIngresado2}")



#-----Numeros+Grandes----#
preguntaNumeroM = "Por favor ingresa un número entero : "
preguntaNumeroN = "Ahora ingresa un número mayor al anterior : "

numeroIngresadoM = int(input(preguntaNumeroM))
numeroIngresadoN = int(input(preguntaNumeroN))

while(numeroIngresadoN > numeroIngresadoM) :
    numeroIngresadoM = numeroIngresadoN
    numeroIngresadoN = int(input(preguntaNumeroN))
print("Has ingresado un número menor o igual al anterion, fin.")



#-----MontosCompras----#
total = 0
monto = float(input("Monto de una venta: $"))
while monto != 0 :
    if monto < 0 :
        print("Monto no válido.")
    else:
        total += monto
    monto = float(input("Monto de una venta: $"))
if total > 1000:
    total -= total * 0.1
print("Monto total a pagar: $", total)
