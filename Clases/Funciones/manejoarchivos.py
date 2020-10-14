#leer

archivo = open ('poema.txt', encoding = 'UTF-8')
print (archivo)
lineas = archivo.readlines()
archivo.close()
print (lineas)
listaRenglones = []
with open ('poema.txt', encoding = 'UTF-8')as lineas:
    for line in lineas :
        print (line)
        listaRenglones.append(line)

print (listaRenglones)

print ('Saludo :\nHola como estás')
print ('Saludo :\t\t\tHola como estás')


nombre = input ('Ingrese su nombre : ')
edad = int (input('Ingrese su edad : '))
opinion = input ('Ingrese su opinión : \n')

archivo = open ('opinion.txt','w', encoding = 'UTF-8')
archivo.write (f'Opinion de {nombre} \n')
archivo.write (f'Edad : {edad} \n')
archivo.write (f'Reseña : {opinion} \n')
archivo.close()