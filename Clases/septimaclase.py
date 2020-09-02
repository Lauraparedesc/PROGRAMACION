#-----se crea la listaNombres-----#
listaNombres = []
listaNombres = ["Melany", 
        "Karla",
        "Laura Paredes",
        "Laura Montoya",
        "Juan Pablo",
        "Mario",
        "Valeria",
        "Santiago"]

listaEdades = [20,18,18,18,21,20,18,18]
print (listaNombres)
print (listaNombres[2])
print (listaNombres[-1])
listaNombres.append("Daniel")
print (listaNombres[-1])
print (listaNombres)

listaNombres.pop(-1)
print (listaNombres)
listaNombres.append ("Daniel")
listaEdades.append (27)
sizeList = len (listaNombres)
print (sizeList)

for i in range (sizeList) :
        print (f"Hola soy {listaNombres [i]} y estoy feliz programando")
print ("SEGUNDO MÉTODO")

for nombre in listaNombres: 
        print (f"Hola soy {nombre} y estoy feliz programando")


for i in range (sizeList) :
        print (f"Nombre: {listaNombres [i]} y Edad: {listaEdades[i]}")

listaHobbies = []
decision = 0
while (decision == 0) :
        hobbie = input("¿Cual es tu hobbie favorito? : ")
        listaHobbies.append(hobbie)
        decision = int (input ("""Ingrese :
                0- Para seguir agregando Hobbies
                !0- Para finalizar
        : """))
print (listaHobbies)