#################################
#Autor: Pedro Velasco Santana   #
#                               #
#Archivo: calculadora_V1.py     #
#################################

#Versión de la calculadora con GUI (Versión 1)

#Explicación del código en calculadora_V0.py, aquí solo se comentará los aspectos relacionados con la GUI

import tkinter 

window = tkinter.Tk() #Creación de la ventana
window.geometry("300x450") #Medidas (a ojo)

titulo = tkinter.Label(window, text = "Calculadora simple", bg = "blue") #Etiqueta del nombre del programa
titulo.grid(row = 0, column = 0, columnspan = 3, sticky = "ew")

caja_de_texto = tkinter.Label(window, text = "Aquí irá resultado", padx = 35, pady = 25) #Etiqueta del nombre de donde debería ir el resultado
caja_de_texto.grid(row = 1, column = 0, columnspan = 3, sticky = "ew")

botones = {}
for i in range(10):
    botones[i] = tkinter.Button(window, text = str(i), width = 4, height = 4)

botones[1].grid(row = 2, column = 0)
botones[2].grid(row = 2, column = 1)
botones[3].grid(row = 2, column = 2)
botones[4].grid(row = 3, column = 0)
botones[5].grid(row = 3, column = 1)
botones[6].grid(row = 3, column = 2)
botones[7].grid(row = 4, column = 0)
botones[8].grid(row = 4, column = 1)
botones[9].grid(row = 4, column = 2)
botones[0].grid(row = 5, column = 0, columnspan = 3, sticky = "ew")

autor = tkinter.Label(window, text =  "Pedro Velasco Santana, 2024", bg = "blue")
autor.grid(row = 6, column = 0, columnspan = 3, sticky = "ew")

window.mainloop()

"""
#Funciones para las distintas operaciones

def suma(operandos):
    resultado = float(0)
    for numero in operandos:
        resultado += numero
    
    operandos.clear()
    return resultado

def resta(operandos):
    resultado = operandos[0] - operandos[1]
    indice = 2 
    while indice < len(operandos):
        resultado -= operandos[indice]
        indice += 1
    
    operandos.clear()
    return resultado

def producto(operandos):
    resultado = float(1) 
    for numero in operandos:
        resultado *= numero
    
    operandos.clear()
    return resultado

def divison(operandos):
    resultado = operandos[0] / operandos[1] 
    indice = 2 
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

print("***************************************\n         CALCULADORA PYTHON V1\n***************************************\n")

#Selección de operación

cod_operacion = int(input("\n\n[+] ¿Qué operación desea realizar? SUMA(1) RESTA(2) PRODUCTO(3) DIVISIÓN(4): ")) 
while cod_operacion < 1 or cod_operacion > 4:
    cod_operacion = int(input("\n\n[+] Código de operación no válido SUMA(1) RESTA(2) PRODUCTO(3) DIVISIÓN(4): "))

operandos = list()
indice = int(0)

while True: 
    numero = input(f"\n[+] Ingrese operando #{indice} (<Enter> para terminar): ")

    if not numero:
        break
    elif indice > 0 and cod_operacion == 4 and float(numero) == 0: 
        print("[-] ERROR: el divisior no puede ser 0")
        break

    operandos.append(float(numero))
    indice += 1

#Salida 

resultado = switch(cod_operacion, operandos)
print(f"\n\n[+] Resultado de la operación: {resultado}")
"""