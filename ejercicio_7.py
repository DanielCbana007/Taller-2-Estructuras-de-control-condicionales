#pido al usuario la temperatura 
temperatuar = float(input("dijite slos grados: "))

# establesco los condicionales 

#si temperatura es menor a 23°c entonces 
if(temperatuar < 23 ):

    #muestro al usuario: "Hace frío"
    print("Hace frío")

#si temperatura es mayor o iguanl a 23°c y la temperatura es menor a 30°c entonces 
elif (temperatuar >= 23 and temperatuar < 30):

    #muestro al usuario: "Día normal"
    print("Día normal")

#si temperatura es mayor o iguanl a 30°c entonces 
elif (temperatuar >= 30):

    #muestro al usuario: "Hace calor"
    print("Hace calor")

#si ninguna de las condiciones se cumple 
else:

    #muestro al usuario: "error"
    print("error")

    