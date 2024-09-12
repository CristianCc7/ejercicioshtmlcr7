import pandas as pd
import matplotlib.pyplot as plt
#Cargar los datos desde el archivo Excel
df = pd.read_excel('datos.xlsx')
# Graficar los datos
valores = df[["Años", "Ventas"]]
print(valores)
ax = valores.plot.bar(x="Años",y="Ventas", rot=0)
#Añadir eitquetas y titulo
plt.xlabel('Años')
plt.ylabel('Ventas')
plt.title('Ventas a lo largo de los años')
#Mostra la fica
plt.grid(True)
plt.show()





