#pido al susuario que escriba el valorde las variables (a,b,c)
a = int(input("escriba el valor de la variable (a): "))
b = int(input("escriba el valor de la variable (b): "))
c = int(input("escriba el valor de la variable (c): "))

#establesco los condicionales 

#si (b) y (c) son distintos de 0 ejecuto las siguientes condiciones 
if (b != 0 and c != 0):

    #si (b) es mayor que (a)
    if (b > a):

        #declaro una variable llamada EC que contiene la siguiente opercaion: "((-b) + a ) / (2 (b * c))"
        ec = ((-b) + a) / (2 * (b * c))
 
        #muestro al usuario: "la solucion de la ecuación es el resultado de la variable EC"
        print(f"la solucion de la ecuación es {ec}")

    #si (b) no es mayor que (a)
    else:

        #muestro al usuario: "(b) no es mayor que (a)"
        print("(b) no es mayor que (a)")
        
#si (b) y (c) no son distintos de 0       
else:
    #muestro al usuario: "(b) y (c) no son distintos de 0"
    print("(b) y (c) no son distintos de 0")

