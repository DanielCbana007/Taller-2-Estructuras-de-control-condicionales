#pido al susuario que escriba el valorde las variables (a,b,c)
a = int(input("escriba el valor de la variable (a): "))
b = int(input("escriba el valor de la variable (b): "))
c = int(input("escriba el valor de la variable (c): "))

#establesco los condicionales 

#si (a) es distinto de 0 ejecuto las siguientes condiciones 
if (a != 0):

    #si (b) y (c) son mayores que (a)
    if (b and c > a):

        #declaro una variable llamada ecuación que contiene la siguiente opercaion: "(((b**2)/(4*(a**2)))-(c/a))**0.5"
        ecuación = (((b**2)/(4*(a**2)))-(c/a))**0.5

        #muestro al usuario: "la solucion de la ecuación es el resultado de la variable ecuación"
        print(f"la solucion de la ecuación es {ecuación}")

    #si (b) y (c) no son mayores que (a)
    else:

        #muestro al usuario: "(b) y (c) no son mayores que (a)"
        print("(b) y (c) no son mayores que (a)")
        
#si no a es distinto de 0       
else:
    #muestro al usuario: "(a) no es distinto de 0"
    print("(a) no es distinto de 0")