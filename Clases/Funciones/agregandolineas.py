#es lo mismo de abajo pero aca hay que hacerlo cada vez y alla ejecuta normal 
archivo = open ('opinion.txt', 'a', encoding = 'UTF-8')
archivo.write('\nMe gustó tu opinión del poema')
archivo.close()
#segunda opcción 
import funciones_archivos as helper
nameFile = 'libro.txt'
helper.agregarLinea ('opinion.txt', 'Nueva linea')
renglonesLibro = helper.leerArchivos(nameFile)
print (len(renglonesLibro))

if (len(renglonesLibro)== 0):
    print('Es la primera linea que se escribirá en el libro')
    helper.agregarLinea(nameFile, 'El día que programar, fue fácil')
else : 
    linea = input ('Ingrese la linea que desea agregar : \n')
    helper.agregarLinea (nameFile, linea)