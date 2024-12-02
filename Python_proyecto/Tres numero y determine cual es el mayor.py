## Solicita tres números y determina cuál es el mayor.
## Dave Pozo

print("#"*40)
print("Tres numero y determina cual es el mayor" .center(40, " "))
print("#"*40)
print("")


numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))


if numero1 >= numero2 and numero1 >= numero3:
    mayor = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    mayor = numero2
else:
    mayor = numero3

print(f"El número mayor es: {mayor}")
