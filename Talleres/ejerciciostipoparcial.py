#Dada una lista de número mostrar en pantalla el mayor número, el menor y el promedio de la lista.
mensaje1 =  '########################## Número mayor, menor y promedio ##########################'
print (mensaje1)
def infoList(lista):
    mayor = max (lista)
    menor = min (lista)
    acumulador = 0
    for elemento in lista :
        acumulador += elemento
    sizeList =   len (lista)
    promedio = acumulador / sizeList
    print (f'el número mayor en la lista es el {mayor}, el menor {menor} y el promedio {promedio}')
edades = [23,22,12,45,17,33,77,18]
infoList(edades)

#Dada una lista números, devuelva únicamente los números pares
mensaje2 = '########################## Números pares ##########################'
print (mensaje2)
def paresLista(lista):
    pares = []
    for elemento in lista:
        if elemento % 2 == 0 :
            pares.append (elemento)
    return pares
numeros = [63, 24, 85, 16, 18, 25, 3, 2, 24]
numerosPares = paresLista(numeros)
print (numerosPares)

#Dado un mensaje mostrarlo en pantalla
mensaje3 = '########################## Mensaje ##########################'
print (mensaje3)
def mostrarMensaje (mensaje):
    print (mensaje)
mensaje = '¡Hola, espero que tengas un gran día hoy!'
mostrarMensaje (mensaje)

#Calculadora 12
print ('########################## Calculadora ##########################')
def sumar(valor1=0, valor2=0):
    return valor1 + valor2
def restar(valor1=0, valor2=0):
    return valor1 - valor2
def multiplicar(valor1=0, valor2=1):
    return valor1 * valor2
def dividir(valor1=0, valor2=1):
    return valor1 / valor2
def calculadora(accion, valor1, valor2):
    print(accion(valor1, valor2))
calculadora (restar, 24,12)
calculadora (multiplicar, 24,12)
calculadora (dividir, 24,12)
calculadora (sumar, 24,12)

#Como ingeniero Biomédico se le pide que cree unas clases referentes a los pacientes de un hospital
print ('########################## HOSPITAL ##########################')
class Paciente:
    def __init__(self, idin,
    nombre,sexo,afiliado):
        self.id = idin
        self.nombre = nombre
        self.sexo = sexo
        self.afiliado = afiliado
    def sintomas (self, lista):
        for elemento in lista :
            print (elemento)
listaSintomas = ['Fiebre', 'Nauseas', 'Dolor de cabeza', 'Dolor abdominal']
class Estable (Paciente):
    def __init__ (self,idin,nombre,sexo,afiliado,tiempo,temperatura,animo):
        Paciente.__init__(self,idin,nombre,sexo,afiliado)
        self.tiempo = tiempo
        self.temperatura = temperatura
        self.animo = animo
    def recomendaciones (self, lista):
        print (f'{self.nombre}, dederas seguir las siguientes recomendaciones : ')
        for elemento in lista :
            print (elemento)
listaRecomendacion = ['Tomar los medicamentos prescritos', 'descansar','mantenerte hidratado']
class Critico (Estable):
    def __init__ (self,idin,nombre,sexo,afiliado,tiempo,temperatura,animo,habitacion, patologia):
        Estable.__init__(self,idin,nombre,sexo,afiliado,tiempo,temperatura,animo)
        self.habitacion = habitacion
        self.patologia = patologia
    def sintomas (self, lista):
        for elemento in lista :
            print (elemento)
listaSintomas2 = ['Fiebre', 'Convulsiones', 'Migraña', 'Dolor abdominal']

Laura = Paciente (1004691625, 'Laura','F', 'SURA')
print (f'Nombre : {Laura.nombre}')
print (f'N° ID : {Laura.id}')
print (f'Sexo : {Laura.sexo}')
print (f'EPS : {Laura.afiliado}')
Laura.sintomas(listaSintomas)
print ('######################################################################################################')
Maria = Estable (9764258841, 'María', 'F', 'Commeva', '30 min', 36 , 'cansada')
print (f'Nombre : {Maria.nombre}')
print (f'N° ID : {Maria.id}')
print (f'Sexo : {Maria.sexo}')
print (f'EPS : {Maria.afiliado}')
print (f'Tiempo de espera : {Maria.tiempo}')
print (f'Temperatura : {Maria.temperatura}')
print (f'Ánimo : {Maria.animo}')
Maria.recomendaciones(listaRecomendacion)
print ('######################################################################################################')
Jose = Critico (8462558841, 'Jose', 'M', 'Nueva EPS', '10 min', 40 , 'decaido', 310, 'Epilepsia' )
print (f'Nombre : {Jose.nombre}')
print (f'N° ID : {Jose.id}')
print (f'Sexo : {Jose.sexo}')
print (f'EPS : {Jose.afiliado}')
print (f'Tiempo de espera : {Jose.tiempo}')
print (f'Temperatura : {Jose.temperatura}')
print (f'Ánimo : {Jose.animo}')
print (f'Habitación : {Jose.habitacion}')
print (f'Patología : {Jose.patologia}')
Jose.sintomas (listaSintomas2)


