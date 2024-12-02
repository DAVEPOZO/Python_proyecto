## Solicita un número al usuario y muestra su tabla de multiplicar del 1 al 10.
## Dave Pozo

print("#"*40)
print("Multiplicar del 1 al 10" .center(40, " "))
print("#"*40)
print("")


numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))


print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
