## Solicita un año y determina si es bisiesto
## (divisible entre 4 pero no entre 100, excepto si es divisible entre 400).
## Dave Pozo

print("#"*40)
print("Año bisiesto" .center(40, " "))
print("#"*40)
print("")


anio = int(input("Ingrese un año: "))


if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")
