print ("Hola, vamos a valorar el estado en el que te encuentras, para ello por favor ingresa los datos siguientes")

procedencia =  input ("Por favor ingrese su lugar de procedencia:")
temperatura = float (input("Por favor ingrese su temperatura : "))

if (procedencia == "China"):
    print ("Estado en Observación")
elif (procedencia == "Iran"):
    print ("Estado en Observación")
elif (procedencia == "Italia"):
    print ("Estado en Observación")
elif (temperatura >= 36 and temperatura <= 38.4):
    print ("Estado Saludable")
elif (temperatura < 36):
    print ("Estado Hipotermia")
elif (temperatura >= 38.5 and temperatura <= 40):
    print ("Estado Alerta")
else:
    print ("Estado Peligro") 