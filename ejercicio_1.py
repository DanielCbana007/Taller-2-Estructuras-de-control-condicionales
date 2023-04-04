#esta es la solucion usual que la gente encontraria 

#pido al usuario que indique el numero del cual quiere la raiz 
numero = float(input("escriba un numero mayor que cero: "))

#esotos son los condicionales que uso

#si el numero es mayor que cero entonces ejecuto las siguientes acciones 
if (numero > 0):
    #defino una nueva variable la cual hace un operacion (el numero que le pedimos a usuario lo potenciamos con 0.5)
    raiz = numero**0.5
    #muestro al usuario: "la raiz del numero (este es el numero que escrivio el usuario) esiguan a: (este es el resultado de la operacion echa en la variable raiz)"
    print(f"la raiz del numero {numero} esiguan a: {raiz}")

#este condicional lo puse por si el usuario comete un error y se lo indicamos 
else:
    print("error")

"""#solucion con funcion math 

#investigando en internet encontre la funcion math y pense que seria divertido usarla en este ejercicio, aparte de practicar 

#pido al usuario que indique el numero del cual quiere la raiz 
numero = int(input("escriba un numero mayor que cero: "))

#si el numero es mayor que cero entonces ejecuto las siguientes acciones 
if (numero > 0):
    #importo la funcion math 
    import math
    #creo una variable llamada raiz en la cual mando llamar la funcion math con su atributo sqrt, este atributo nos devuelve la raiz cuadrada de un numero entero
    raiz = math.sqrt(numero)
    #muestro al usuario: "la raiz del numero (este es el numero que escrivio el usuario) esiguan a: (este es el resultado de la operacion echa en la variable raiz)"
    print(f"la raiz del numero {numero} esiguan a: {raiz}")
else:
    print("error")
print("solucion con funcion math ")
"""

