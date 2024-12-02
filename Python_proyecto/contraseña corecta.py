## Escribe un programa que solicite una contraseña y valide si es correcta 
## Dave Pozo

print("#"*40)
print("Crontraseña correcta" .center(40, " "))
print("#"*40)
print("")



contraseña_correcta = "12345"


contraseña_ingresada = input("Ingrese la contraseña: ")


if contraseña_ingresada == contraseña_correcta:
    print("Contraseña correcta. Acceso concedido.")
else:
    print("Contraseña incorrecta. Acceso denegado.")
