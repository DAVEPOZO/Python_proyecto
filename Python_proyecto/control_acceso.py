## Solicita un nombre de usuario y contraseña, y valida si ambos son correctos.
## Permite tres intentos antes de bloquear el acceso.
## Dave Pozo

print("#"*40)
print("Control acceso" .center(40, " "))
print("#"*40)
print("")


usuario_valido = "admin"
contra_valida = "1234"


intentos = 3

while intentos > 0:

    usuario = input("Introduce tu nombre de usuario: ")
    contra = input("Introduce tu contraseña: ")
    
    # Validar las credenciales
    if usuario == usuario_valido and contra == contra_valida:
        print(f"Bienvenido, {usuario}.")
        break
    else:
        intentos -= 1
        if intentos > 0:
            print(f"Usuario o contraseña incorrectos. Te quedan {intentos} intentos.")
        else:
            print("Has superado el número máximo de intentos. Acceso bloqueado.")
