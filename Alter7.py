#Programa que a partir de la medida de los lados de un triángulo, es
#capaz de decir si es equilátero, isósceles o escaleno.
n1=int(input("Introduce lado 1:"))
n2=int(input("Introduce lado 2:"))
n3=int(input("Introduce lado 3:"))
if n1==n2==n3:
    print("Equilátero")
elif n1==n2 or n2==n3 or n1==n3:
    print("Isósceles")
else:
    print ("Escaleno")