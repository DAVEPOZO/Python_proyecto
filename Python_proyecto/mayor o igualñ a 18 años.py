## Solicita la edad del usuario y determina si es elegible para votar
## (mayor o igual a 18 años).
## Dave Pozo

print("#"*40)
print("Mayor o igual a 18 años" .center(40, " "))
print("#"*40)
print("")


edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Eres elegible para votar.")
else:
    print("No eres elegible para votar.")
