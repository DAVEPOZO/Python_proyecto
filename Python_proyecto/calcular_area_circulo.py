radio = int(input('Ingrese el radio del circulo: '))

def cal_area_cir(radio): 
    area_cir = (3.1415 * (radio**2))
    area_cir = round(area_cir,2)
    return(area_cir)


print(f"El area del circulo es {cal_area_cir(radio)}")