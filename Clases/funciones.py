#FUNCIONES SIN ENTRADA
print ('#'*60)
print ('¡Hola!')
print ('¿Como está?')
print ('#'*60)
def lineDesing():
    print ('#'*60)
lineDesing()
print('¡Hola!')
print('¿Como está?')
lineDesing()
#FUNCIONES CON UNA ENTRADA
def lineDesingC(cantidad=2):
    print('#'*cantidad)
lineDesingC(12)
lineDesingC()
#FUNCION SUMA
def sumar(valor1=0, valor2=0):
    return valor1 + valor2
def restar(valor1=0, valor2=0):
    return valor1 - valor2
def multiplicar(valor1=0, valor2=1):
    return valor1 * valor2
def dividir(valor1=0, valor2=1):
    return valor1 / valor2
print(sumar(2,2))
print (sumar())
#FUNCIONES QUE UTILIZAN OTRAS
def calculadora(accion, valor1, valor2):
    print(accion(valor1, valor2))
lineDesingC (30)
calculadora (sumar, 1,1)
calculadora (dividir, 1,2)
calculadora (multiplicar, 73,77)
calculadora (restar, 73,77)