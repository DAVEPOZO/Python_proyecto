num = int(input("Ingrese un numero: "))

def comprbarParImpar(numero):
    if numero % 2 == 0:
        return True
    else: 
        return False

print(comprbarParImpar(num))