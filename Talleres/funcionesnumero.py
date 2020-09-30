#primer ejercicio

a = int(input('Ingrese el primer número entero : '))
b = int(input('Ingrese el segundo número entero : '))
def numeros (a,b):
    if a > b :
        print (f'{a} es el número mayor')
    elif b > a :
        print (f'{b} es el número mayor')
    else:
        print ('Los números ingresados son iguales')

numeros (a,b)

#segundo ejercicio 

def mostrarLista (lista):
    for elemento in lista :
        print (elemento)

listaNombres = ['Luis', 'Maria', 'Angela', 'Valentina', 'Rodrigo']
mostrarLista (listaNombres)

#tercer ejercicio

peso = float(input('Por favor ingresa tu peso en Kg : '))
altura = float(input('Por favor ingresa tu altura en metros : '))

def IMC (peso, altura):
    return round((peso /(altura ** 2)), 3)

print (IMC(peso, altura))

#cuarto ejercicio

class Persona:
    def __init__(self, idin,
    nombrein, pesoin, alturain, sexoin):
        self.id = idin
        self.nombre = nombrein
        self.peso = pesoin
        self.altura = alturain
        self.sexo = sexoin
class Estudiante (Persona):
    def __init__ (self, semestre, universidad, carrera, idin, nombrein, pesoin, alturain, sexoin):
        Persona.__init__(self,idin,nombrein, pesoin, alturain, sexoin)
        self.semestre = semestre
        self.universidad = universidad
        self.carrera = carrera 
    def materia (self):
        print (f'Hola soy {self.nombre} y voy a estudiar Física')

Laura = Estudiante ('Tercer', 'CES', 'Biomédica', 1004691625, 'Laura', 50, 1.59, 'F')
print (Laura.nombre)
print (Laura.id)
print (Laura.peso)
print (Laura.altura)
print (Laura.sexo)

print (f'Hola soy {Laura.nombre} , estoy en {Laura.semestre} semestre de {Laura.carrera} en la Universidad {Laura.universidad}')
Laura.materia()