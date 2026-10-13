#Introducir dos números enteros.¿El primer número es divisible por el segundo?
a=int(input("Introduce el valor del primer número: "))
b=int(input("Introduce el valor del segundo número: "))
division=a/b
if division==int(division):
    print("El primer número es divisible por el segundo.")
else:
    print("El primer número no es divisible por el segundo.")