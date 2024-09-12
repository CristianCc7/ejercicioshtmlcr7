# Definir la lista original
numeros = [1, 2, 3, 4, 5]

# Inicializar una lista vacía para almacenar los productos
productos = []

# Utilizar un bucle for para multiplicar los elementos y almacenar los resultados en la nueva lista
for numero in numeros:
    producto = numero * 2
    productos.append(producto)

# Imprimir la lista con los nuevos valores
print("La lista con los elementos multiplicados por 2 es:", productos)
