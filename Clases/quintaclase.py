#-------Preguntas-------#
preguntaNumero = "ingrese un número del 1 al 10 : "
#-------Mensaje-------#
mensajeFallido = "Fallaste!, no es el número secreto"
mensajeExitoso = "Felicitaciones has acertado el número en el que pense"
mensajeDespedida = "Gracias por jugar, nos vemos"
#Ciclos while

numeroSecreto = 6
numeroIngresado = int(input(preguntaNumero))
while(numeroSecreto != numeroIngresado) :
    print(mensajeFallido)
    numeroIngresado = int(input(preguntaNumero))
print(mensajeExitoso)
print(mensajeDespedida)

#EjercicioVocales

preguntaVocal = "Ingrese una vocal en minuscula : "
mensajeFallido = "¡Fallaste! No es la vocal secreta"
mensajeExitoso = "Felicitaciones!! has adividado la vocal que pense"
mensajeDespedida = "Gracias por jugar, te veo pronto"

vocalSecreta = "e"
vocalIngresada = input(preguntaVocal)
while(vocalSecreta != vocalIngresada) :
    print(mensajeFallido)
    vocalIngresada = input(preguntaVocal)
print(mensajeExitoso)
print(mensajeDespedida)
