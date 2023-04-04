#pido los numero al usuario
numero1 = int(input("indique el numero1: "))
numero2 = int(input("indique el numero2: "))
numero3 = int(input("indique el numero3: "))

#defino los condicionlaes, si numero1 es mayor que numero2 y numero2 es mayor que numero3, entonces
if (numero1 > numero2 & numero2 > numero3):

    #muestro al usuario que: "numero1 es mayor numero2 es el numero del medio numero3 es el numero menor"
    print(f"{numero1} es mayor\n{numero2} es el numero del medio\n{numero3} es el numero menor")

#si numero2 es mayor que numero1 y numero1 es mayor que numero3, entonces
elif (numero2 > numero1 & numero1 > numero3):

    #muestro al usuario que: "numero2 es mayor numero1 es el numero del medio numero3 es el numero menor"
    print(f"{numero2} es mayor\n{numero1} es el numero del medio\n{numero3} es el numero menor")

#si numero3 es mayor que numero2 y numero1 es mayor que numero2, entonces
elif (numero3 > numero2 & numero1 > numero2):

    #muestro al usuario que: "numero3 es mayor numero1 es el numero del medio numero2 es el numero menor"
    print(f"{numero3} es mayor\n{numero1} es el numero del medio\n{numero2} es el numero menor")

#si numero1 es mayor que numero3 y numero3 es mayor que numero2, entonces
elif(numero1 > numero3 & numero3 > numero2):

    #muestro al usuario que: "numero1 es mayor numero3 es el numero del medio numero2 es el numero menor"
    print(f"{numero1} es mayor\n{numero3} es el numero del medio\n{numero2} es el numero menor")

#si numero3 es mayor que numero1 y numero2 es mayor que numero1, entonces
elif(numero3 > numero1 & numero2 > numero1):

    #muestro al usuario que: "numero3 es mayor numero2 es el numero del medio numero1 es el numero menor"
    print(f"{numero3} es mayor\n{numero2} es el numero del medio\n{numero1} es el numero menor")

#si numero2 es mayor que numero3 y numero3 es mayor que numero1, entonces
elif(numero2 > numero3 & numero3 > numero1):

    #muestro al usuario que: "numero2 es mayor numero3 es el numero del medio numero1 es el numero menor"
    print(f"{numero2} es mayor\n{numero3} es el numero del medio\n{numero1} es el numero menor")

#si ninguan de estas condiciones se cumple
else:

    #le muestro al usuario que hay un error
    print("error")