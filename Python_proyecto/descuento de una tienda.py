## Una tienda ofrece un 20% de descuento si el cliente gasta más de $100.
## Escribe un programa que calcule el monto final
## Dave Pozo

print("#"*40)
print("Descuenro del 20% si el cliente gasta mas 100$" .center(40, " "))
print("#"*40)
print("")



def calcular_monto_final(monto):
    if monto > 100:
        descuento = monto * 0.20  
        monto_final = monto - descuento
    else:
        monto_final = monto  
    return monto_final


monto_compra = float(input("Ingrese el monto de su compra: $"))


monto_final = calcular_monto_final(monto_compra)


print(f"El monto final de su compra es: ${monto_final:.2f}")
