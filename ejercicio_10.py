#pido al usuario el mes del año 
mes = input("escriba un mes del año: ")

#ddefino los condicionales 

#si el mes es igual a noviembre, diciembre o enero entonces
if (mes == "noviembre" or mes == "diciembre" or mes == "enero"):

    #muestro al usuario: "invierno"
    print("invierno")

#si el mes es igual a febrero, marzo o abril entonces
elif (mes == "febrero" or mes == "marzo" or mes == "abril"):

    #muestro al usuario: "primavera"
    print("primavera")

#si el mes es igual a febrero, marzo o abril entonces
elif (mes == "mayo" or mes == "junio" or mes == "julio"):

    #muestro al usuario: "verano"
    print("verano")

#si el mes es igual a agosto, septiembre o octubre entonces
elif (mes == "agosto" or mes == "septiembre" or mes == "octubre"):

    #muestro al usuario: "otoño"
    print("otoño")

#si ninguna de las condiciones se cumple entonces
else:

    #muestro al usuario: "este mes no existe"
    print("este mes no existe")

    