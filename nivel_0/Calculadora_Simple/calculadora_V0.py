#################################
#Autor: Pedro Velasco Santana   #
#                               #
#Archivo: calculadora_V0.py     #
#################################

#Versión en terminal de un proyecto más ambicioso

#NOTA: De antemano pido disculpas por los núemeros mágicos, espero que se entienda la utilidad de los mismos

#Funciones para las distintas operaciones

"""
Nota sobre el funcionamiento:

Las operaciones usan los operadores de asignación: 

                +=, -=, *=, /= 

La finalidad de su uso es concatenar operaciones, el problema
está presenta en la resta y división, donde no existe un elemento 
neutro al que inicializar la variable que contendrá el resultado.
Por ende, se me ha ocurrido asignarle la primera operación a esta
variable para posteriormente continuar con el resto de operaciones con 
normalidad. 

Para suma y producto se usan bucles for y para resta y división un bucle
while que recorre la lista de operandos desde la tercera posición
"""

def suma(operandos):
    resultado = float(0)
    for numero in operandos:
        resultado += numero
    
    operandos.clear()
    return resultado

def resta(operandos):
    resultado = operandos[0] - operandos[1]
    indice = 2 #Se empieza a calcular desde la tercera posición
    while indice < len(operandos):
        resultado /= operandos[indice]
        indice += 1
    
    operandos.clear()
    return resultado

def producto(operandos):
    resultado = float(1) #Elemento neutro del producto
    for numero in operandos:
        resultado *= numero
    
    operandos.clear()
    return resultado

def divison(operandos):
    resultado = operandos[0] / operandos[1] #Calcula la primera división
    indice = 2 #Se empieza a calcular desde la tercera posición
    while indice < len(operandos):
        resultado /= operandos[indice]
        indice += 1

    operandos.clear()
    return resultado

#Función que hace las veces de switch

def switch(cod_operacion, operandos):
    if cod_operacion == 1:
        return suma(operandos)
    elif cod_operacion == 2: 
        return resta(operandos)
    elif cod_operacion == 3: 
        return producto(operandos)
    elif cod_operacion == 4: 
        return divison(operandos)

print("***************************************\n         CALCULADORA PYTHON V0\n***************************************\n")

#Selección de operación

cod_operacion = int(input("\n\n[+] ¿Qué operación desea realizar? SUMA(1) RESTA(2) PRODUCTO(3) DIVISIÓN(4): ")) 
while cod_operacion < 1 or cod_operacion > 4:
    cod_operacion = int(input("\n\n[+] Código de operación no válido SUMA(1) RESTA(2) PRODUCTO(3) DIVISIÓN(4): "))

operandos = list() #Los operandos se guardarán en una lista, y se van introduciendo al final de la misma
indice = int(0)

#Se rellena la lista con los operandos

while True: 
    numero = input(f"\n[+] Ingrese operando #{indice} (<Enter> para terminar): ")

    if not numero:
        break
    elif indice > 0 and cod_operacion == 4 and float(numero) == 0: #Control de divisores = 0
        print("[-] ERROR: el divisior no puede ser 0")
        break

    operandos.append(float(numero)) #Los números se almacenan como float
    indice += 1

resultado = switch(cod_operacion, operandos)
print(f"\n\n[+] Resultado de la operación: {resultado}")
