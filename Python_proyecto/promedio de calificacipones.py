## Solicita calificaciones al usuario (hasta que ingrese -1)
## y calcula el promedio.
## Dave Pozo

print("#"*40)
print("promedio de calificaciones" .center(40, " "))
print("#"*40)
print("")




suma_calificaciones = 0
contador = 0


while True:
    calificacion = float(input("Ingrese una calificación (o -1 para terminar): "))
    
    
    if calificacion == -1:
        break
    
    
    if calificacion >= 0:
        suma_calificaciones += calificacion
        contador += 1
    else:
        print("Calificación inválida, ingrese un valor positivo o -1 para terminar.")


if contador > 0:
    promedio = suma_calificaciones / contador
    print(f"El promedio de las calificaciones es: {promedio:.2f}")
else:
    print("No se ingresaron calificaciones válidas.")
