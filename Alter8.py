#Introducir los tres valores para una ecuación de segundo grado (a, b, c).
#Visualizar el resultado solo si sus raíces son reales (cuando al realizar el
#cálculo de dentro de la raíz nos da >=0).
a=float(input("Introduce el valor del número al cuadrado: "))
b=float(input("Introduce el valor del número que se multiplica por x: "))
c=float(input("Introduce el valor de los números que no llevan x: "))
cálculoraiz=b**2-4*a*c 
if cálculoraiz>=0:
    R1=(-b+(cálculoraiz)**0.5)/(2*a)
    R2=(-b-(cálculoraiz)**0.5)/(2*a)
    print(f"Tu primera raíz es: {R1:.2f}, tu segunda raíz es: {R2:.2f}")
else:
    print("No existe solución real)")