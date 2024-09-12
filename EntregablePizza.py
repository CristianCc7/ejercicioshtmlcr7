#Registro de usuarios
import random
print("Bienvenido a Pizzeria Pizza Planeta")
registro =int(input("Opcion 1 para cliente, y 2 para empleados: "))


if registro == 1:
    print("Que desea hacer?: ")
    print("Reservar(1)")
    print("Hacer un pedido(2)")
    print("Cancelar pedido(3)")
    print("Consulta de eventos(4)")
    opc = int(input("Diga su opcion: "))
    if opc == 1:
        print("De cuantos puestos desea la mesa: ")
        mesa = int(input("Diga su opcion: "))
        print("Reservacion exitosa") 
    elif opc == 2:
        print("En este momento tenemos pizza de queso(1), pepperoni(2) y hawaiana(3)")   
        pedido = int(input("Diga su opcion: "))
        print("Su pedido llegara pronto")
    elif opc == 3:
        print("Diga cual es su numero de pedido: ")
        cpedido= int(input("Diga su opcion: "))
        print("Listo, su numero de pedido ", cpedido, " ya fue cancelado")
    else:
        print("Actualmente tenemos descuentos los viernes por 50% de descuento y cumpleañero no paga")
else:
    print("Consulta de horario(1)")
    print("Dejar puesto de trabajo(2)")
    em=int(input("Diga su opcion: "))
    if em == 1:
        print("Su horario va de lunes a sabado de 5pm a 10 pm")
    else:
        print("Consulte con su jefe para redactar su carta de renuncia")
