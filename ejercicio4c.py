def verificar_votacion():
    edad = int(input("Por favor, ingresa tu edad: "))
    if edad >= 18:
        print("¡Puedes votar en las elecciones presidenciales!")
    else:
        print("Lo siento, no puedes votar en las elecciones presidenciales.")

verificar_votacion()
