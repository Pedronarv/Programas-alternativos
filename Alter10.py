#Programa marca nota en texto según nota numérica
nota=float(input("Introduce tu nota:"))
if nota<5:
    print("SUSPENSO")
#Podría añadirse un límite inferior en la nota de 0
#Pero el aún profesor de lengua en este instituto Recio me demostró en 3º de la ESO que es posible sacar un -8 en un examen
elif nota>=5 and nota<6:
    print("SUFICIENTE")
elif nota>=6 and nota<7:
    print("BIEN")
elif nota>=7 and nota<9:
    print("NOTABLE")
elif nota>=9 and nota<=10:
    print("SOBRESALIENTE")
else:
    print ("Nota incorrecta, introduce la nota de tu examen")