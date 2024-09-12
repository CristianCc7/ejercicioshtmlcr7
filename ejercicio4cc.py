# Definir la cadena de texto de ejemplo
cadena = "Hola, qué tal?"

# Convertir la cadena a minúsculas para simplificar la búsqueda de vocales
cadena = cadena.lower()

# Inicializar el contador de vocales
contador_vocales = 0

# Utilizar un bucle for para imprimir las vocales y contarlas
for letra in cadena:
    if letra in "aeiouáéíóú":
        print(letra)
        contador_vocales += 1

# Imprimir el total de vocales encontradas
print("El total de vocales en la cadena es:", contador_vocales)
