#pido al usuario los goles correspondientes a cada partido
partido1 = int (input("¿cuantos goles anoto el jugador en su primer partido?"))
partido2 = int (input("¿cuantos goles anoto el jugador en su segundo partido?"))
partido3 = int (input("¿cuantos goles anoto el jugador en su tercer partido?"))

#defino los condicionales, si la suma de partidos da mayor que 10
if (partido1 + partido2 + partido3 > 10):

    #creo una variable que sume los partidos y los divida en la cantidad de partidos
    promedio =int((partido1 + partido2 + partido3)/3)

    #muestro al usuario: "el promedio de goles anotados es de (la variable promedio que suma los goles por partido entre la cantidad de partidos) goles"
    print(f"el promedio de goles anotados es de {promedio} goles")

#si esta condicion no se cumple, muestro al usuario: "No se puede determinar el promedio de goles de 	este jugador"
else:
    print("No se puede determinar el promedio de goles de 	este jugador")