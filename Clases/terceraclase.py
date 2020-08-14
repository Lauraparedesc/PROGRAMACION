a = int (input("Ingrese el primer número entero : "))
b = int (input("Ingrese el segundo número entero : "))
print (a,b)

if (a == b):
    print("Son números iguales")
elif (a > b):
    print("El número A", a, "Es mayor que el número", b)
else:
    print(f"El número B : {b} es mayor que el número A : {a}")

#Dada una temperatura determinar si el paciente esta sano o no
# Temperatura menos a 36 - hipotermia
# Temperatura en el intervalo a 36-38 normal
# Temperatura mayor o igual a 38 - Fiebre
#Muestre el nombre del paciente y su estado

name = input("Ingrese el nombre del paciente : ")
temperatura = float(input("Ingrese la temperatura del paciente : "))
if (temperatura < 36) :
    print(f"El paciente {name} tiene hipotermia ")
elif (temperatura >= 36 and temperatura < 37.5) :
    print(f"El paciente {name} tiene una temperatura dentro del estandar normal")
elif (temperatura >= 37.5 and temperatura < 38) :
    print(f"El paciente {name} esta en estado de alerta")
else:
    print(f"El paciente {name} tiene fiebre")

