#Cree la clase Torta con atributos forma, sabor, altura, también tendrá una función donde muestre todos sus atributos
class Torta ():
    def __init__ (self,formaIn, saborIn,alturaIn):
        self.forma = formaIn
        self.sabor = saborIn
        self.altura = alturaIn
    def mostrar_atributos(self):
        print (f'Es una torta de forma {self.forma} , de sabor {self.sabor}  y de una altura {self.altura}cm')

cake = Torta ('redonda', 'chocolate',20)
cake.mostrar_atributos()

#ESTUDIANTE
class Estudiante ():
    def __init__ (self, nombreIn, edadIn,idIn, carreraIn, semestreIn):
        self.nombre = nombreIn
        self.edad = edadIn
        self.id = idIn
        self.carrera = carreraIn
        self.semestre = semestreIn
    def estudiar_materia (self, materia,tiempo) :
        print (f'Hola soy {self.nombre} y tengo que estudiar : {materia}  por {tiempo} horas')

estudent = Estudiante('pepe', 23, 123789, 'Sistemas', 4)
estudent.estudiar_materia('física',12)

#imc
class Nutricionista():
    def __init__ (self, nombreIn, edadIn,idIn, universidadIn):
        self.nombre = nombreIn
        self.edad = edadIn
        self.id = idIn
        self.universidad = universidadIn
    def calcular_imc(self, peso,estatura) :
        return round ((peso/estatura**2), 3)

aleja = Nutricionista('Aleja', 27,13024789,'CES')
print (f'Hola soy {aleja.nombre} y tengo {aleja.edad} años, mi id es {aleja.id} y estudio en Universidad {aleja.universidad}')
print (aleja.calcular_imc ( 80 , 1.67))

#Cree una clase Canguro que tenga los atributos edad, id, nombre
class Canguro():
    def __init__ (self, nombreIn, edadIn,idIn):
        self.nombre = nombreIn
        self.edad = edadIn
        self.id = idIn
    def saltar (self, saltos) :
        for i in range(saltos):
            print (f'El canguro {self.nombre} ha dado  {i+1}  saltos')

jack = Canguro('Jack', 12, 134098)
jack.saltar(12)

#Instrumento
class Violin():
    def __init__ (self, marca, color, material, tipo):
        self.marca = marca
        self.color = color
        self.material = material
        self.tipo = tipo
    def interpetar (self, cancion):
        print (f'Vamos a escuchar : {cancion}')

instrumento = Violin ('yamaha', 'café', 'madera', 'acustico')
print (f'El violin es marca {instrumento.marca}, color {instrumento.color}, hecho de {instrumento.material} y {instrumento.tipo}')
instrumento.interpetar('Recuérdame')
