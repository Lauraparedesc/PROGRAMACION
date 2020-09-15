listaDolares = [20000,30000,4000,2500,1000,7600]
preguntaMenu = '''
Por favor ingrese alguna de estas opciones:
            1- Convertir dolares 
            2- Mostrar categoria de ingresos
            3- Ver máximo, minimo y promedio de ingresos 
            4- Para salir del programa
: '''
preguntaConversionDolares = '''
Por favor ingrese alguna de estas opciones:
            C- Convertir a pesos colombianos
            D- Convertir a dolares
            E- Convertir a euros
: '''
msjNovalidoN = 'Recuerda ingresar una opción valida : 1,2,3,4'
msjNovalidoC = 'Recuerda ingresar una opción valida : C,D,E'

mensajeSalida = 'Gracias por usar el programa'
mensajeDolares = 'No es necesaria la conversión, pero se muestra la lista'

opcion = int(input(preguntaMenu))
listaGradosC = []
listaGradosE = []
listaGradosD = listaDolares


