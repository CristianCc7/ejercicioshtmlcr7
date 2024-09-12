#Bienvenidos a la ruta de aprendizaje, donde jugaremos el ahorcado con todos ustedes!
import random

def seleccionar_palabra():
    palabras = ['python', 'programacion', 'desarrollador', 'ahorcado', 'javascrip', 'computador', 'diseño', 'analisis']
    return random.choice(palabras)

def mostrar_estado(palabra, letras_adivinadas):
    estado = ''.join([letra if letra in letras_adivinadas else '_' for letra in palabra])
    return estado

def jugar():
    palabra = seleccionar_palabra()
    letras_adivinadas = set()
    intentos_restantes = 6

    print("¡Bienvenido al juego del ahorcado!")
    
    while intentos_restantes > 0:
        estado_actual = mostrar_estado(palabra, letras_adivinadas)
        print(f"Palabra: {estado_actual}")
        print(f"Intentos restantes: {intentos_restantes}")
        print(f"Letras adivinadas: {', '.join(letras_adivinadas)}")
        
        letra = input("Adivina una letra: ").lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa solo una letra.")
            continue
        
        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra.")
            continue
        
        letras_adivinadas.add(letra)
        
        if letra in palabra:
            print("¡Buena elección!")
        else:
            print("Esa letra no está en la palabra.")
            intentos_restantes -= 1
        
        if all(letra in letras_adivinadas for letra in palabra):
            print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
            break
    else:
        print(f"¡Juego terminado! La palabra era: {palabra}")

if __name__ == "__main__":
    jugar() 