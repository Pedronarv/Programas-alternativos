#Introducir dos números enteros y ordenarlos de menor a mayor
n1= float(input("Introduce el primer número:"))
n2= float(input("Introduce el segundo número:"))
if n1>n2:
    print (n2,"es menor que",n1)
elif n1==n2:
    print (n1,"es igual que",n2)
else:
    print (n1,"es menor que",n2)