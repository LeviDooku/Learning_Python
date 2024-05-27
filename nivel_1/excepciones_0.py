##################################
#Autor: Pedro Velasco Santana    #
#                                #
#Archivo: excepciones_0.py       #
##################################

#Una excepción es un error en tiempo de ejecución

#Controlar las excepciones es vital para no interrumpir la ejecución de la totalidad del programa

#El bloque try - except sirve para lanzar excepciones, en este programa, solo si se divide por 0

#Las excepciones se pueden consultar: https://docs.python.org/es/3/tutorial/errors.html

def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("[-] ERROR: no se puede dividir por 0") 

num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))

print(f"El resultado de la operación es: {divide(num1, num2)}")