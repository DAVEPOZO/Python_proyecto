## Calcula y muestra la suma de los números del 1 al 10
## Dave Pozo

print("#"*40)
print("suma de los numeros del 1 al 10" .center(40, " "))
print("#"*40)
print("")


suma = 0


for i in range(1, 11):
    suma += i


print("La suma de los números del 1 al 10 es:", suma)
