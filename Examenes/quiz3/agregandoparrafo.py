import funciones_archivos as helper
nameFile = 'parrafo.txt'
helper.agregarLinea ('parrafo.txt', '')
renglonesLibro = helper.leerArchivos(nameFile)

linea = input ('Ingrese la linea que desea agregar : \n')
helper.agregarLinea (nameFile, linea)