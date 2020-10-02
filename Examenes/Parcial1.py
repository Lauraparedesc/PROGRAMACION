#Dado un de número devolver el número elevado al cuadrado.
def elevar2 (valor1=0):
    return valor1 ** 2
def elevar3 (valor1=0):
    return valor1 ** 3
def elevar4 (valor1=0):
    return valor1 ** 4
def elevar5 (valor1=0):
    return valor1 ** 5
def calculadora(accion, valor1):
    print(accion(valor1))
calculadora (elevar2, 12)
calculadora (elevar3, 5)
calculadora (elevar4, 8)
calculadora (elevar5, 6)

#Como ingeniero Biomédico se le pide que cree unas clases referentes a los pacientes de un hospital
class Doctor:
    def __init__ (self,idin,nombre,sexo,universidad):
        self.id = idin
        self.nombre = nombre
        self.sexo = sexo
        self.universidad = universidad
    def mostraratributos (self):
        print (f'Mi nombre es {self.nombre}, identificado con {self.id} C.C, sexo {self.sexo} de la Universidad {self.universidad}')
    def sintomas (self, lista):
        print ('Presenta los siguientes sintomas : ')
        for elemento in lista :
            print (elemento)
listaSintomas = ['Fiebre', 'Nauseas', 'Dolor de cabeza', 'Dolor abdominal']
class Neurologo (Doctor):
    def __init__ (self,idin,nombre,sexo,universidad,experiencia,consultorio,salario):
        Doctor.__init__(self,idin,nombre,sexo,universidad)
        self.experiencia = experiencia
        self.consultorio = consultorio
        self.salario = salario
    def mostraratributos (self):
        print (f'Nombre : {self.nombre}',
        f'N° ID : {self.id}',
        f'Sexo: {self.sexo}',
        f'Universidad : {self.universidad}',
        f'Experiencia : {self.experiencia} años',
        f'Consultorio : {self.consultorio}',
        f'Salario : {self.salario} millones')
    def pacientes (self, lista):
        for elemento in lista :
            print (f'Puede seguir para atención el paciente : {elemento}')
listaPacientes = ['Juan', 'Luis', 'Camila', 'Cristina', 'Julio']
class Cardiologo (Doctor):
    def __init__ (self,idin,nombre,sexo,universidad,experiencia,consultorio,salario):
        Doctor.__init__(self,idin,nombre,sexo,universidad)
        self.experiencia = experiencia
        self.consultorio = consultorio
        self.salario = salario
    def mostraratributos (self):
        print (f'Nombre : {self.nombre}',
        f'N° ID : {self.id}',
        f'Sexo: {self.sexo}',
        f'Universidad : {self.universidad}',
        f'Experiencia : {self.experiencia} años',
        f'Consultorio : {self.consultorio}',
        f'Salario : {self.salario} millones')
    def sintomasRespuesta (self, lista):
        print ('Presenta los siguientes sintomas : ')
        for elemento in lista :
            print (elemento)
        print ('Ya conocemos lo que tiene el paciente')
listaRespuesta = ['Fiebre', 'Convulsiones', 'Migraña', 'Dolor abdominal']

Laura = Doctor(1004691625, 'Laura','F', 'CES')
Laura.mostraratributos()
Laura.sintomas(listaSintomas)
Claudia = Neurologo(1004691625, 'Claudia','F', 'CES', 8, 312, 5)
Claudia.mostraratributos()
Claudia.pacientes(listaPacientes)
Carlos = Cardiologo (1004691625, 'Carlos','M', 'UDEA', 14, 57, 8)
Carlos.mostraratributos()
Carlos.sintomasRespuesta(listaRespuesta)
