#pido el año al usuario 
year = int(input("¿cual es el año a evaluar?: "))

#defino los condicionales 

#si el numero es divisible entre cuatro paso al siguiente condicional
if (year % 4):

    #si el año es divsible entre 100 paso al sigiente condicional
    if (year % 100):

        #si el año es divisible entre 400 entonces
        if (year % 400):

            #muestro al usuario: "El año es bisiesto (tiene 366 días)"
            print("El año es bisiesto (tiene 366 días)")
        
        #si esta condicion no se cumple entonces
        else:

            #muestro al usuario: "El año no es bisiesto (tiene 365 días)"
            print("El año no es bisiesto (tiene 365 días)")

    #si esta condicion no se cumple entonces
    else:

        #muestro al usuario: "El año es bisiesto (tiene 366 días)"
        print("El año es bisiesto (tiene 366 días)")


#si esta condicion no se cumple entonces
else:

    #muestro al usuario: "El año no es bisiesto (tiene 365 días)"
    print("El año no es bisiesto (tiene 365 días)")

    