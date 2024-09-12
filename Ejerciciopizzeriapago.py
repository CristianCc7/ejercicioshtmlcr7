# Menu que represente el carrito de compras
carrito = {
    "Pizza pepperoni": 12.99,
    "Pizza vegetariana": 10.99,
    "Refresco": 1.99
}

# Función para calcular el total a pagar
def calcular_total(carrito):
    total = sum(carrito.values())
    return total

# Método de pago
def procesar_pago(metodo, total):
    print(f"Procesando pago de ${total} mediante {metodo}")

# Ejemplo de uso
total_a_pagar = calcular_total(carrito)
print(f"Total a pagar: ${total_a_pagar}")

metodo_de_pago = "tarjeta"  # Aquí se puede cambiar el método de pago
procesar_pago(metodo_de_pago, total_a_pagar)
