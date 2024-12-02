## Solicita un número al usuario y determina si es par o impar.
## Dave Pozo

print("#"*40)
print("par o impar" .center(40, " "))
print("#"*40)
print("")

numero=int(input("Ingrese un numero: "))

if numero%2==0:
    print("numero par")
elif numero%2!=0:
    print("numero impar")
