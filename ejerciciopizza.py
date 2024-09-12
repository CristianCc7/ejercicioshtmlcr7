class Pizza:
    def __init__(self, sabor, tamaño, ingredientes):
        self.sabor = sabor
        self.tamaño = tamaño
        self.ingredientes = ingredientes

class Pedido:
    def __init__(self, cliente, direccion, pizzas):
        self.cliente = cliente
        self.direccion = direccion
        self.pizzas = pizzas

    def mostrar_pedido(self):
        print(f"Pedido para: {self.cliente}")
        print(f"Dirección de entrega: {self.direccion}")
        print("Pizzas:")
        for pizza in self.pizzas:
            print(f"- {pizza.tamaño} {pizza.sabor} con {', '.join(pizza.ingredientes)}")

# Crear pizzas
pizza1 = Pizza("Pepperoni", "Grande", ["Pepperoni", "Queso", "Salsa de tomate"])
pizza2 = Pizza("Vegetariana", "Mediana", ["Pimientos", "Cebolla", "Aceitunas", "Queso"])

# Realizar pedido
pedido1 = Pedido("Cristian Calderon", "Barrio CR7 ", [pizza1, pizza2])

# Mostrar el pedido
pedido1.mostrar_pedido()
