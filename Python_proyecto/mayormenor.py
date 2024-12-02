##Escribe un programa que solicite un número y determine si es mayor o menor que 10
##Dave Pozo
print("#"*40)
print("mayor y menor" .center(40, " "))
print("#"*40)
print("")
a = int(input("ingrese primer numero: "))
b = int(input("ingrese segundo numero: "))

max = a
min = b

if b > max:
    max = b

if a < min:
    min = a

print("mayor:", max)
print("menor:", min)
