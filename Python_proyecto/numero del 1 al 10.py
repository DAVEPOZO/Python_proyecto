## Usa un bucle para mostrar los números del 1 al 10 en la consola.
## Dave Pozo

print("#"*40)
print("Mostrar los números del 1 al 10" .center(40, " "))
print("#"*40)
print("")



for i in range(1, 11):
    
    if i < 10:
        print(i, end=", ")
    else:
        print(i)
