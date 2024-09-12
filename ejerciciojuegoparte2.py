import random 

options = ('piedra', 'papel','tijera')
rounds = 1
computer_wins = 0
user1_wins = 0
user2_wins = 0

print ("""
       [ 🤖 Bienvenido al juego Piedra, Papel o Tijera 🙋]
                   >>> Ingresa una opción <<<
       """)

opc = input("Como desea jugar: (PvP) / (PvC) o: ").lower()

while rounds < 4:
    print('*' * 10)
    print('Round ', rounds)
    print('*' * 10)

    if opc == 'pvc':
        print(f'''
🤖 Computer wins: {computer_wins}  
🙋 User1 wins: {user1_wins}

        ''')
    
        user1_option = input('>>> Piedra, papel o tijera =>').lower()
        while not user1_option in options: 
            print('Esa opción no es válida crack')
            user1_option = input('>>> Piedra, papel o tijera =>').lower()
    
        computer_option = random.choice(options)

        print('User1 option => ', user1_option)
        print('Computer option => ', computer_option)

        if user1_option == computer_option:
            print('Empate!\n')
        elif user1_option == 'piedra':
            if computer_option == 'tijera':
                print('🪨 Piedra gana a tijera ✂️')
                print('¡User gana!\n')
                user1_wins += 1
            else:
                print('📄 Papel gana a piedra 🪨')
                print('¡Computer gana!\n')
                computer_wins += 1
        elif user1_option == 'papel':
            if computer_option == 'piedra':
                print('📄 Papel gana a piedra 🪨')
                print('¡User gana!\n')
                user1_wins += 1
            else:
                print('✂️ Tijera gana a papel 📄')
                print('¡Computer gana!\n')
                computer_wins += 1
        elif user1_option == 'tijera':
            if computer_option == 'papel':
                print('✂️ Tijera gana a papel 📄')
                print('¡User gana!\n')
                user1_wins += 1
            else: 
                print('🪨 Piedra gana a tijera ✂️')
                print('¡Computer gana!\n')
                computer_wins += 1
        rounds += 1


    elif opc == 'pvp': 
        print(f''' 
🙋 User1 wins: {user1_wins}
🙋 User2 wins: {user2_wins} 
            ''')      
        user1_option = input('>>> Piedra, papel o tijera =>').lower()
        user2_option = input('>>> Piedra, papel o tijera =>').lower()
    
        while not user1_option in options: 
            print('Esa opción no es válida crack')
            user1_option = input('>>> Piedra, papel o tijera =>').lower()
        while not user2_option in options: 
            print('Esa opción no es válida crack')
            user2_option = input('>>> Piedra, papel o tijera =>').lower()
        print('User1 option => ', user1_option)
        print('User2 option => ', user2_option)

        if user1_option == user2_option:
            print('Empate!\n')
        elif user1_option == 'piedra':
            if user2_option == 'tijera':
                print('🪨 Piedra gana a tijera ✂️')
                print('¡User1 gana!\n')
                user1_wins += 1
            else:
                print('📄 Papel gana a piedra 🪨')
                print('¡User2 gana!\n')
                user2_wins += 1
        elif user1_option == 'papel':
            if user2_option == 'piedra':
                print('📄 Papel gana a piedra 🪨')
                print('¡User1 gana!\n')
                user1_wins += 1
            else:
                print('✂️ Tijera gana a papel 📄')
                print('¡User2 gana!\n')
                user2_wins += 1
        elif user1_option == 'tijera':
            if user2_option == 'papel':
                print('✂️ Tijera gana a papel 📄')
                print('¡User1 gana!\n')
                user1_wins += 1
            else: 
                print('🪨 Piedra gana a tijera ✂️')
                print('¡User2 gana!\n')
                user2_wins += 1
        rounds += 1


if opc == 'pvc':
    if user1_wins > computer_wins:
        print('🎖️ El ganador es User 🎖️')
        print(f'Puntaje: {user1_wins}')
    elif user1_wins == computer_wins:
         print('¡🥶Hay un empate general 🥶!')
         print(f'Puntaje: {computer_wins}')
    else:
         print('🎖️ El ganador es Computer 🎖️')
         print(f'Puntaje: {computer_wins}')

elif opc == 'pvp': 
    if user1_wins > user2_wins:
        print('🎖️ El ganador es User1 🎖️')
        print(f'Puntaje: {user1_wins}')
    elif user1_wins == user2_wins:
        print('¡🥶Hay un empate general 🥶!')
    else:
        print('🎖️ El ganador es User2 🎖️')
        print(f'Puntaje: {user2_wins}')