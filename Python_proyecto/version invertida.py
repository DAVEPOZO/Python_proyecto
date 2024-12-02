## Solicita un número entero y muestra su versión invertida.
## Dave Pozo

print("#"*40)
print("Version invertida" .center(40, " "))
print("#"*40)
print("")



numero = input("Ingrese un número entero: ")


numero_invertido = numero[::-1]


print(f"La versión invertida de {numero} es: {numero_invertido}")
