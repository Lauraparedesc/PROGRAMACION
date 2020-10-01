class Persona:
    def __init__(self, idin, nombre, edad):
        self.id = idin 
        self.nombre = nombre
        self.edad = edad
    def hablar (self):
        print (f'Hola soy {self.nombre}, gusto en conocerte, mi ID es {self.id} y tengo {self.edad} años')
    def caminar (self, pasos):
        print (f'{self.nombre} ha dado {pasos} pasos mientras caminaba')
class Doctor (Persona):
    def __init__ (self,idin,nombre,edad,especialidad):
        Persona.__init__(self,idin,nombre,edad)
        self.especialidad = especialidad
    def tratamiento (self, enfermedad):
        print (f'Hola mi nombre es {self.nombre} soy especialista en {self.especialidad} y voy atender tu {enfermedad}')
class Nutricionista(Persona):
    def __init__ (self,idin,nombre,edad,universidad):
        Persona.__init__(self,idin,nombre,edad)
        self.universidad = universidad
    def calcular_imc(self, peso,estatura) :
        return round ((peso/estatura**2), 3)
class Abogado (Persona):
    def __init__(self, idin, nombre, edad, especialidad, universidad):
        Persona.__init__(self,idin,nombre,edad)
        self.especialidad = especialidad
        self.universidad = universidad
        print (f'Hola soy {self.nombre}, gusto en conocerte, mi ID es {self.id} y tengo {self.edad} años. Soy abogad@ {self.especialidad} de la universidad {self.universidad}')
    def presentacaso (self,caso):
        print (f'Procedo a presentar a mi cliente {self.nombre} en el caso {caso}')

Juliana = Persona (1004857965, 'Juliana', 26)
Juliana.hablar()
Juliana.caminar(150)
David = Doctor (9852635425, 'David', 35, 'Neurología')
David.tratamiento('Epilepsia')
Angela = Nutricionista (1002546987, 'Angela', 28, 'CES')
print (f'Hola soy {Angela.nombre}, mi id es {Angela.id}, tengo {Angela.edad} años y estudie en universidad {Angela.universidad}')
print (f'El IMC del paciente es : {Angela.calcular_imc ( 50 , 1.61)}')
Catalina = Abogado (1256356958, 'Catalina', 42, 'Penalista', 'UDEA')
Catalina.presentacaso('Homicidio')
