import random 

preguntaNumero = "Adivina el número que arrojo el dado : "

mensajeFallido = "Fallaste!, no es el número"
mensajeExitoso = "Felicitaciones has acertado el número"
mensajeDespedida = "Gracias por jugar, nos vemos"

dado = random.randint (1,6) 
numeroIngresado = int(input(preguntaNumero))

while( dado != numeroIngresado) :
    print(mensajeFallido)
    numeroIngresado = int(input(preguntaNumero))
print(mensajeExitoso)
print(mensajeDespedida)

#-----ListaAlimentos----#

listaAlimentos = []
listaAlimentos = ["manzana", 
        "lasagna",
        "creps",
        "baby beef"]
sizeList = len (listaAlimentos)

for i in range (sizeList) :
        print (f"{listaAlimentos [i]}")

