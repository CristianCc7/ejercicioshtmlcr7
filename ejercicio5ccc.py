def ingresar_dinero():
    total_dinero = 0
    
    while True:
        entrada = input("Ingrese la cantidad de dinero a ingresar en la alcancia (o 'fin' para terminar): ")
        
        if entrada.lower() == 'fin':
            break
        
        try:
            cantidad = float(entrada)
            
            if cantidad < 0:
                print("Por favor, ingrese una cantidad positiva.")
            else:
                total_dinero += cantidad
        except ValueError:
            print("Entrada no valida. Por favor, ingrese un numero.")
    
    print(f"El total de dinero ingresado en la alcancia es: {total_dinero}")

# Llamar a la funcion para comenzar el proceso
ingresar_dinero()

