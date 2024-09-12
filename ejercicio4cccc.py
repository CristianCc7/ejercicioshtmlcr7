import pandas as pd
import matplotlib.pyplot as plt 

workbook1 = "pruebagrafos1.xlsx"
df =pd.read_excel(workbook1)
print(df.head())
valores = df[["Nombre","Net Worth (Billions)"]]
print(valores)
ax = valores.plot.bar(x="Nombre",y="Net Worth (Billions)", rot=0)
plt.show()

