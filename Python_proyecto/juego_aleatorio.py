## Genera un número aleatorio entre 1 y 10 y solicita al usuario que
## adivine el número. Usa if para verificar si acertó o no.
## Dave Pozo

print("#"*40)
print("Juegos de nuemero" .center(40, " "))
print("#"*40)
print("")




import random

numero_aleatorio = random.randint(1, 10)

print("Generando numero")
intento = int(input("Adivina cual es: "))

if intento == numero_aleatorio:
    print("¡Felicidades, acertaste!")
else:
    print(f"Intenta de nuevo. El numero era {numero_aleatorio}.")
