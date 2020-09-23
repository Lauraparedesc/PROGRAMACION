class Persona:
    def __init__(self, estaturaingresado,
    pesoingresado, nombreingresado, 
    idingresado, edadingresado):
        self.raza = 'Humana'
        self.estatura = estaturaingresado
        self.edad = edadingresado
        self.nombre = nombreingresado
        self.peso = pesoingresado
        self.id = idingresado
        print ('Hola mundo estoy viv@')
    def caminar (self):
        print ('Hola voy a caminar')
    def saludo (self, saludoEspecial):
        print (saludoEspecial)
class Arquitecto (Persona):
    def dibujarPlanos (self):
        print (f'Hola soy {self.nombre} voy a dibujar el plano')
class Biomedico (Persona):
    def cultivarCelulas (self):
        print (f'Hola soy {self.nombre} voy a cultivar celulas')

karla = Arquitecto (1.62, 48, 'Karla', 1032321323, 18)
karla.caminar ()
Juan = Biomedico (1.76, 82, 'Juan Pablo', 912837981237, 23)
Juan.caminar ()
karla.saludo ('HOLI CRAYOLI')
Juan.saludo ('HOLA COCACOLA')
karla.dibujarPlanos()
Juan.cultivarCelulas()