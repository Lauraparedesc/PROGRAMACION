class TortasRedonda: 
    def __init__ (self, saborIngresado):
        #DEFINIENDO ATRIBUTOS
        self.forma = 'Redonda'
        self.sabor = saborIngresado
        #accion al crear objeto
        print ('Soy una torta nueva')
    def mostrar_atributos (self):
        print (f'Soy de forma {self.forma} y de sabor {self.sabor}')

#creo torta
tortaChocolate = TortasRedonda ('Chocolate')
tortaVainilla = TortasRedonda ('Vainilla')
#se muestra en pantalla atributos
print (tortaChocolate.sabor)
print (tortaVainilla.sabor)
print (tortaChocolate.forma)
print (tortaVainilla.forma)

#
tortaChocolate.mostrar_atributos()
tortaVainilla.mostrar_atributos()
