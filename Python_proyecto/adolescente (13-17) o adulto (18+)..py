## Solicita una edad y clasifica al usuario como niño (0-12),
## adolescente (13-17) o adulto (18+).
## Dave Pozo

print("#"*40)
print("Adolescente (13-17) o adulto (18+)." .center(40, " "))
print("#"*40)
print("")


edad = int(input("Ingrese su edad: "))

           
if edad >= 0 and edad <= 12:
    clasificacion = "niño"
elif edad >= 13 and edad <= 17:
    clasificacion = "adolescente"
else:
    clasificacion = "adulto"



print(f"Con {edad} años, eres un {clasificacion}.")
