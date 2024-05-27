##################################
#Autor: Pedro Velasco Santana    #
#                                #
#Archivo: excepciones_2.py       #
##################################

#Instrucción raise, permite lanzar excepciones con un mensaje personalizado. Tiene más sentido en POO.

#En siguientes programas se verá como crear excepciones propias usando clases

#Este script sirve para quedarnos con la sintaxis

def evalua_edad(edad):
    #La ejecución en este caso se para devido a que no se controla con try - except
    if edad < 0:
        raise TypeError("[-] ERROR: no se permiten edades negativas") #La excepción realmente puede ser la que sea

    if edad < 20:
        return "[+] Muy joven"
    elif edad < 40:
        return "[+] Mediana edad"
    elif edad < 65:
        return "[+] Tercera edad"
    elif edad < 100:
        return "[+] Tic tac..."
    
edad = int(input("Introduce tu edad: "))
print(evalua_edad(edad))