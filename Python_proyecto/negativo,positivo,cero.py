## Solicita al usuario un número y determina si es positivo, negativo o cero
## Dave Pozo

print("#"*40)
print(" positivo, negativo o cero" .center(40, " "))
print("#"*40)
print("")

numero=int(input("Ingrese un numero entero: "))

if numero<0:
    print("El numero es negativo")
elif numero>0:
    print("El numero es positivo")
else:
    print("El numero es cero")
    
