#Crea un calculadora que dé a elegir entre suma, resta, multiplicación, división o resta entre dos números enteros.
n1=int(input("Introduce el primer número:"))
signo=input("Introduce + para suma - para resta * para multiplicación y / para división: ")
n2=int(input("Introduce el segundo número:"))
if signo=="+":
    n3=n1+n2
    print("Tu resultado es:", n3)
elif signo=="-":
    n3=n1-n2   
    print("Tu resultado es:", n3)
elif signo=="*":
    n3=n1*n2
    print("Tu resultado es:", n3)
elif signo=="/":
    n3=n1/n2
    print("Tu resultado es:", n3)
else: 
    print("Signo incorrecto incorrecto, introduce +, -, * o /")