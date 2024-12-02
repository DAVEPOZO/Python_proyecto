## Solicita la calificación de un estudiante y determina si está aprobado
## (mayor o igual a 7) o reprobado.
## Dave Pozo

print("#"*40)
print("Aprobado,Reprobado" .center(40, " "))
print("#"*40)
print("")

cali1 = float(input("Ingrese la calificacion 1: "))
cali2 = float(input("Ingrese la calificacion 2: "))
cali3 = float(input("Ingrese la calificacion 3: "))

promedio = (cali1 + cali2 + cali3) / 3

if promedio >= 7:
    print("Aprobastes el curso con un promedio de: ",round(promedio,1))
else:
    print("Reprobaste el curso con un promedio de: ",round(promedio,1))
