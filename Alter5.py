#Introducir una letra, tal que si es A, realizaremos el área de una
#circunferencia y si es L, realizaremos la longitud de la circunferencia. Sea
#cualquiera de las opciones elegidas, visualizar el resultado indicando si
#se trata del área o de la longitud.
import math
letra=input("Introduce una A para área o L para para longitud:").upper()
r=float(input("Introduce un radio:"))
if letra=="A":
    A=math.pi*r**2
    print(f"Tu área es: {A:.2f}")
elif letra=="L":
    L=2*math.pi*r
    print(f"Tu longitud es: {L:.2f}")
else:
    print("Valor incorrecto, introduce A o L")