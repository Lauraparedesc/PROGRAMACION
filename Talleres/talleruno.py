nombre =  input ("Por favor ingrese su nombre :")
print (f"Hola! {nombre}, vamos a calcular tu IMC ")
peso = float (input("Por favor ingrese su peso : "))
estatura = float (input("Por favor ingrese su estatura :"))
print (peso)
print (estatura)

IMC = (peso / estatura**2)
print (f"Tu IMC es {IMC}")

if (IMC < 18.5):
    print ("Usted tiene infrapeso")
elif (IMC >= 18.5 and IMC <= 24.9):
    print ("Su peso esta dentro del rango normal")
elif (IMC >= 25 and IMC <= 29.9):
    print ("Usted tiene sobrepeso")
elif (IMC >= 30 and IMC <= 34.9):
    print ("Usted tiene obesidad")
else:
    print ("Usted tiene obesidad morbida")


