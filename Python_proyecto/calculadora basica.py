## Solicita dos números y una operación (+, -, *, /)
## y realiza el cálculo correspondiente.
## Dave Pozo

print("#"*40)
print("Calculadora basica" .center(40, " "))
print("#"*40)
print("")



numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, *, /): ")


if operacion == "+":
    resultado = numero1 + numero2
elif operacion == "-":
    resultado = numero1 - numero2
elif operacion == "*":
    resultado = numero1 * numero2
elif operacion == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Error: No se puede dividir por cero."
else:
    resultado = "Operación no válida."


print(f"El resultado de {numero1} {operacion} {numero2} es: {resultado}")
