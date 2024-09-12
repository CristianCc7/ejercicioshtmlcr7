def ordenar_lista(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

# Lista de elementos
lista = [5, 3, 6, 2, 10]

# Llamar al procedimiento para ordenar la lista
ordenar_lista(lista)

# Imprimir la lista ordenada
print("Lista ordenada:", lista)


