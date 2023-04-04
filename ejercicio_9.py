#pido al usuario la bonificasion
bonificacion = int(input("¿cual es la bonificacion?"))

#defino los condicionlaes 

#si la bonificacion es igual a 500000 entonces 
if (bonificacion == 500000):

    #muestro al usuario: "comprará un teclado gaming"
    print("comprará un teclado gaming")

#si bonificasion es mayor o igual a 500000 y bonificasion es menor igual a 1000000 entonces
elif (bonificacion >= 500000 and bonificacion <= 1000000):

    #muestro al usuario: "comprará una tableta digitalizadora"
    print("comprará una tableta digitalizadora")

#si bonificasion es mayor a 1000000 y bonificasion es menor igual a 2000000 entonces
elif (bonificacion > 1000000 and bonificacion <= 2000000):

    #muestro al usuario: "comprará un iPad"
    print("comprará un iPad")

#si bonificasion es mayor a 2000000 entonces
elif (bonificacion > 2000000):

    #muestro al usuario: "comprará una MacBook o un computador ASUS ROG"
    print("comprará una MacBook o un computador ASUS ROG")

#si ninguna de las condiciones se cumple entonces
else:

    #muestro al usuario: "no compra nada"
    print("no compra nada")
