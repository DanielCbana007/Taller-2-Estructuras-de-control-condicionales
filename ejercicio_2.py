#pido al usuario el simbolo y uso el atributo 
simbolo = input("introdisca el simbolo quimico: ")

#creo una lista que contenga los simbolos que voy a usar 
simbolos = ["H", "C", "O", "F", "CL"]

#establesco los condicionales 

#si el simbolo es igual a "H", entonces muestro al usuario: "el simbolo (simbolo "H") equivale a Hidrógeno"
if (simbolo == simbolos[0]):
    print(f"el simbolo {simbolo} equivale a Hidrógeno")

#si el simbolo es igual a "C", entonces muestro al usuario: "el simbolo (simbolo "C") equivale a Carbono"
elif (simbolo == simbolos[1]):
    print(f"el simbolo {simbolo} equivale a Carbono")

#si el simbolo es igual a "O", entonces muestro al usuario: "el simbolo (simbolo "O") equivale a Oxígeno"
elif (simbolo == simbolos[2]):
    print(f"el simbolo {simbolo} equivale a Oxígeno")

#si el simbolo es igual a "F", entonces muestro al usuario: "el simbolo (simbolo "F") equivale a Flúor"
elif (simbolo == simbolos[3]):
    print(f"el simbolo {simbolo} equivale a Flúor")

#si el simbolo es igual a "CL", entonces muestro al usuario: "el simbolo (simbolo "CL") equivale a Cloro"
elif (simbolo == simbolos[4]):
    print(f"el simbolo {simbolo} equivale a Cloro")

#si el simbolo es diferente de los contemplados en la lista simbolos, entonces muestro al usuario: "Elemento no contemplado"
else:
    print("Elemento no contemplado")