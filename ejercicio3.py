#Algoritmo que calcula el area en m2 y perimetro en m de un triangulo equilatero 
base= float(input("ingrese la base del triangulo m^2:"))
altura=float(input("ingrese la altura del triangulo en m:")) 
#perimetro=base+base+base
perimetro=3*base
area=(base*altura)/2
print("para una base de ",base,"m","y una altura de", altura,"el area es:", area, "m^2,","y el perimetro es:",perimetro,"m")
      