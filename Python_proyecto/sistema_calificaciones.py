## Solicita una calificación numérica y devuelve la letra correspondiente:
## 90-100: A.
## 80-89: B.
## 70-79: C.
## 60-69: D.

## Dave Pozo

print("#"*40)
print("Calificación numérica y devuelve con una letra" .center(40, " "))
print("#"*40)
print("")


calificacion = float(input("Introduce tu calificación numérica: "))

if 90 <= calificacion <= 100:
    letra = "A"
elif 80 <= calificacion < 90:
    letra = "B"
elif 70 <= calificacion < 80:
    letra = "C"
elif 60 <= calificacion < 70:
    letra = "D"
elif calificacion < 60:
    letra = "F"
else:
    letra = "Calificación no válida"


print(f"Tu calificación es {letra}.")
