def encontrar_mayor_menor():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    num3 = float(input("Ingresa el tercer número: "))

    mayor = max(num1, num2, num3)
    menor = min(num1, num2, num3)

    print(f"El número mayor es: {mayor}")
    print(f"El número menor es: {menor}")

encontrar_mayor_menor()