import random

options =('piedra','papel','tijeras')
rounds = 1 
computer_wins = 0 
user_wins = 0 

print("""[🤖 Bienvenido al juego piedra, papel o tijeras 🙋 ]
      >>> Ingresa una opcion<<<
      """)


while rounds < 4: 
    print('***'*10)
    print('round',rounds)
    print('***'*10)
    
    print(f'''
🤖computer wins:{computer_wins}
🙋user wins:{user_wins}
      ''')

    user_option=input('>>> piedra,papel o tijeras=>').lower()

    while not user_option in options:
        print('esa opcion no es valida')
        user_option= input('>>> piedra, papel o tijeras=>').lower()
        
    computer_option = random.choice(options)
            
    print('user option=>', user_option)
    print('computer option=>',computer_option)
    
    if user_option == computer_option:
          print('empate!\n')
    elif user_option == 'piedra':
            if computer_option == 'tijeras':
                  print('🪨 piedra gana a tijeras ✂️')
                  print('¡user gana!\n')
                  user_wins += 1 
            else: 
                  print('📄papel gana a piedra🪨')
                  print('¡computer gana!\n')
                  computer_wins +=1 
    elif user_option == 'papel': 
         if computer_option == 'piedra':
            print('📄 papel gana a piedra 🪨')
            print('¡user gana!\n')
            user_wins +=1 
         else:
            print('✂️ tijeras gana a papel 📄')
            print('¡computer gana!\n')
            computer_wins +=1 
    elif user_option == 'tijeras': 
         if computer_option == 'papel':
            print('✂️ tijeras gana a papel 📄')
            print('¡user gana!\n')
            user_wins +=1
         else:
            print('🪨 piedra gana a tijeras ✂️')
            print('¡computer gana!\n')
            computer_wins +=1
    rounds +=1 
   
if user_wins > computer_wins:
      print('🎖️ el ganador es user 🎖️')
      print(f'puntaje:{user_wins}')
else: 
      print('🎖️ el ganador es el computer 🎖️')
      print(f'puntaje:{computer_wins}')
      
      
    
       
    
      
               
            
               
            
               
               
              
          
           
                       
          
      
               

     
         
      




