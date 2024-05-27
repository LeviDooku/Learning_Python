##################################
#Autor: Pedro Velasco Santana    #
#                                #
#Archivo: excepciones_1.py       #
##################################

#Lanzar varias excepciones en un programa, claúsula finally

#Se pueden concatenar varias excepciones en un mismo bloque try - except. La claúsula finally siempre se ejecuta, útil cuando existen conexiones con BD, fichero etc.

#Las excepciones se pueden consultar: https://docs.python.org/es/3/tutorial/errors.html

def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("[-] ERROR: no se puede dividir por 0") 
    finally:
        print("Función terminada")

while True: #Bucle que asegura que se introducen los valores correctos
    try:
        num1 = int(input("Introduzca el primer número: "))
        num2 = int(input("Introduzca el segundo número: "))
        break
    except ValueError:
        print("[-] ERROR: tipo de dato incorrecto")

print(f"El resultado de la operación es: {divide(num1, num2)}")

