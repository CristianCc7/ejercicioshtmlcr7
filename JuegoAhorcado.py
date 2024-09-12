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
   
