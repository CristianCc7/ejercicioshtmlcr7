# calcular el area y oermetro de un trapecio
base1 = float(input("escribe la base del trapecio n1:"))
base2 = float(input("escribe la base del trapecio n2:"))
altura = float(input("escribe la altura del trapecio:"))
lado1 = float(input("escribe el lado n1:"))
lado2  = float(input("escribe el lado n2: "))


area = (base1 + base2 * altura)/2
perimetro = base1 + base2 + lado1 +lado2

print("El resultado del area del trapecio es: ", area , "El resultado del perimetro del trapecio es: ", perimetro)

