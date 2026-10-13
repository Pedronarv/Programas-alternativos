#Introducir una letra y visualizar si es vocal o consonante
letra=input("Introduce una letra:")

if letra in "AEIOUaeiou":
#si usamos in aeiou
    print("La letra",letra,"es una vocal")
else:
    print("La letra",letra,"es una consonante")