## Solicita un número entero y calcula la suma de sus dígitos.
## Dave Pozo

print("#"*40)
print("número entero y calcula la suma de sus dígitos" .center(40, " "))
print("#"*40)
print("")



numero = input("Ingrese un número entero: ")


suma_digitos = 0


for digito in numero:
    suma_digitos += int(digito)


print(f"La suma de los dígitos de {numero} es: {suma_digitos}")
