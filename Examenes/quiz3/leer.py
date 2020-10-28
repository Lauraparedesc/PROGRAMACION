archivo = open ('parrafo.txt', encoding = 'UTF-8')
print (archivo)
lineas = archivo.readlines()
archivo.close()
print (lineas)
listaRenglones = []
with open ('parrafo.txt', encoding = 'UTF-8')as lineas:
    for line in lineas :
        print (line)
        listaRenglones.append(line)

print (listaRenglones)