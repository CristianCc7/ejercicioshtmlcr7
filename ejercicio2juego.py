import random

options = ('piedra', 'papel', 'tijera')
rounds = 1
computador_win = 0
jugador1 = 0

print("""
      [🤖 Bienvenido al juego Piedra, Papel o Tijera 🙋
                <<< ¡Empieza el Juego! >>>]
        """)

while rounds <= 4:  
    print("***" * 10)
    print("Round", rounds)
    print("***" * 10)
    
    print(f"""
🤖 Victorias del computador: {computador_win}
🙋 Victorias del Usuario: {jugador1}
        """)
    
    user_option = input("<<Piedra, Papel o Tijera>>: ").lower()
    
        
    while user_option not in options:
        print("Opción no válida.")
        user_option = input("Ingrese opción <<Piedra, Papel o Tijera>>: ").lower()
    
    computador_opcion = random.choice(options)
    
    print(f"La opción del usuario fue: {user_option}")
    print(f"La opción del computador fue: {computador_opcion}")
    
    if user_option == computador_opcion:
        print("Resultado: ¡Empate!")
    elif user_option == 'piedra':
        if computador_opcion == 'tijera':
            print("Piedra gana a Tijera")
            print("Usuario gana")
            jugador1 += 1
        else:
            print("Papel gana a Piedra")
            print("Computador gana")
            computador_win += 1
    elif user_option == 'papel':
        if computador_opcion == 'piedra':
            print("Papel gana a Piedra")
            print("Usuario gana")
            jugador1 += 1
        else:
            print("Tijera gana a Papel")
            print("Computador gana")
            computador_win += 1
    elif user_option == 'tijera':
        if computador_opcion == 'papel':
            print("Tijera gana a Papel")
            print("Usuario gana")
            jugador1 += 1
        else:
            print("Piedra gana a Tijera")
            print("Computador gana")
            computador_win += 1
            
    rounds += 1

if jugador1 > computador_win:
    print("El ganador es el usuario")
    print(f"Puntos: {jugador1}")
elif jugador1==computador_win:
    print("Fue un empate")
else:
    print("El ganador es el computador")
    print(f"Puntos: {computador_win}")
    
    