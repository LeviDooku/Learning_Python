######################################
#Autor: Pedro Velasco Santana        #
#                                    #
#Archivo: lambda_function_0.py       #
######################################

#Una función lambda es una función anónima, se usan para abreviar. 
#Consiste en resumir una función normal en una lambda.
#Muy útil si tenemos que aplicar una función en repetidas ocasiones en nuestro programa

#Las funciones complejas (muchos if, bucles etc.) NO podemos usar funciones lamda

"""
EJEMPLO: transformar esta función en una lambda

def eleva_numero(base, exponente):

    return base**exponente
"""

eleva_numero = lambda base, exponente:(base**exponente)

while True: 
    try:
        num1 = int(input("Introduzca base: "))
        num2 = int(input("Introduzca exponente: "))
        break
    except ValueError:
        print("[-] Valor introducido no válido")

print(f"El resultado de {num1} elevado a {num2} = {eleva_numero(num1, num2)}")



