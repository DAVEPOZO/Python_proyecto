## Calcula el factorial de un número ingresado por el usuario (n!).
## Dave Pozo

print("#"*40)
print("Factor de un numero" .center(40, " "))
print("#"*40)
print("")


numero = int(input("Ingrese un número para calcular su factorial: "))


factorial = 1


for i in range(1, numero + 1):
    factorial *= i


print(f"El factorial de {numero} es: {factorial}")
