
import matplotlib.pyplot as plt
#Datos en el eje horizontal (X)
x=[1,2,3,4,5]
#Datos en el eje vertical (Y)
y=[2,3,5,7,11]

#Graficar los datos 
plt.plot(x,y,marker= "o" ,linestyle='-' )
#Añadir etiquetas y estilos
plt.xlabel("eje X")
plt.xlabel("eje Y")
plt.xlabel("Grafico de ejemplo")
#Mostrar grafica
plt.grid(True)
plt.show()



