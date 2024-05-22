#################################
#Autor: Pedro Velasco Santana   #
#                               #
#Archivo: calculadora_V1.py     #
#################################

#Versión de la calculadora con GUI (Versión 1)

#Sé que hay muchos comentarios pero hay que acordarse!!

#Explicación del código en calculadora_V0.py, aquí solo se comentará los aspectos relacionados con la GUI

from tkinter import *

"""
Explicación rápida de argumentos:

1. Label(root, text = "Calculadora simple", bg = "blue")

root: donde se mostrará 
text: texto a mostrar
bg: color del background

2. grid(row = 0, column = 0, columnspan = 3, sticky = "ew")

row: fila del grid donde se mostrará
column: columna del grid donde se mostrará
columnspan: número de columnas que ocupará el objeto referenciado
sticky: usa las iniciales de los puntos cardinales para indicar que llene el espacio disponible en esa dirección.
"ew" ocupa de east a west aka eje x.

3. Button(root, text = " ", width = 4, height = 4)

root: donde se mostrará
text: texto a mostrar
width: anchura
height: altura

4. Otros

borderwidth: grosor del borde (no vale de nada sin relief)
relief: estilo del borde

"""

def mostrar_caracter(caracter):
    caracter_pulsado.config(text = caracter)

root = Tk() #Creación de la ventana
root.title("Calculadora v1")

instrucciones = Label(root, text = "INSTRUCCIONES:\n- Se debe presionar <Enter> después de presionar cada botón\n- Se debe empezar presionando un botón numérico\n- Cuando se termine de introducir datos pulsar RESULT", bg = "blue"
                      ).grid(row = 0, column = 0, columnspan = 4, sticky = "ew") 


#No se puede poner el .grid en el mismo objeto, ya que al evaluarlo, la función "mostrar_caracter" lo detecta como nulo 
caracter_pulsado = Label(root, text = " ", padx = 35, pady = 25, borderwidth = 2, relief = "solid") #Etiqueta del nombre de donde se van mostrando los caracteres pulsados
caracter_pulsado.grid(row = 1, column = 0, columnspan = 4, sticky = "ew") 


#Generación y colocación de los botones de números    

botones = {} #Diccionario, cada elemento lleva una etiqueta asociada (similar a map de C++)

for i in range(10):
    botones[i] = Button(root, text = str(i), command = lambda numero = i: mostrar_caracter(numero), width = 10, height = 4)

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

#Generación y colocación de los botones de operaciones

boton_suma = Button(root, text = "+", command = lambda caracter = i: mostrar_caracter("+"), width = 4, height = 4).grid(row = 2, column = 3)
boton_resta = Button(root, text = "-", command = lambda caracter = i: mostrar_caracter("-"), width = 4, height = 4).grid(row = 3, column = 3)
boton_prod = Button(root, text = "x", command = lambda caracter = i: mostrar_caracter("x"), width = 4, height = 4).grid(row = 4, column = 3)
boton_div = Button(root, text = "/", command = lambda caracter = i: mostrar_caracter("/"), width = 4, height = 4).grid(row = 5, column = 3)
boton_enter = Button(root, text = "<Enter>", command = lambda caracter = i: mostrar_caracter("<Enter>"), width = 4, height = 4).grid(row = 6, column = 0, columnspan = 4, sticky = "ew")
boton_enter = Button(root, text = "RESULT", command = lambda caracter = i: mostrar_caracter("RESULT"), width = 4, height = 4, bg = "red").grid(row = 7, column = 0, columnspan = 4, sticky = "ew")

autor = Label(root, text =  "Pedro Velasco Santana, 2024", bg = "blue").grid(row = 8, column = 0, columnspan = 4, sticky = "new") #Etiqueta autor

root.mainloop()

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