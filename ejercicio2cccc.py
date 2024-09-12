
ruta_archivo = "C:/Users/SENA/Desktop/ejercicios/cr7.txt"

with open(ruta_archivo,"w") as carta: 
    carta.write("este es un archivo de ejemplo\n")
    carta.write("esta es una segunda linea de texto")
    with open(ruta_archivo,"r") as carta: 
        contenido = carta.read()
        print (contenido)
        
        
        
