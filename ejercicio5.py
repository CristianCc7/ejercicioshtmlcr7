import math
#Definir el radio del circulo
radio=float(input("ingresa el radio del circulo:"))

#Calcular el perimetro del circulo 
perimetro= 2 * math.pi * radio

#Calcular el area del circulo 
area= math.pi *(radio**2)


print("el perimetro del circulo es:", perimetro)
print("el area del circulo es", area)
