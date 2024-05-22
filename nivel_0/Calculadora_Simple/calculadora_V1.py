#################################
#Autor: Pedro Velasco Santana   #
#                               #
#Archivo: calculadora_V1.py     #
#################################

#Versión de la calculadora con GUI (Versión 1)

#Sé que hay muchos comentarios pero hay que acordarse!!

#Explicación del código en calculadora_V0.py, aquí solo se comentará los aspectos relacionados con la GUI

from tkinter import *

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

"""
Explicación de argumentos:

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

Funciones:

Para llamar a una función después de pulsar un botón o cualquier tipo de evento se usa: 

command=funcion_a_llamar

Si la funcion tiene parámetros:

command=lamda parametro = x: funcion(parametro)

                        o

command=lamda: funcion(parametro) #(útil si el parámetro es constante. Ver botones a partir lin: 163)
"""

numero_actual = "" #De primeras se usa el string para concatenar cifras
operandos = list() #Lista usada para los números a operar

#Función que aplica la lógica del programa

#Recibe un parámetro caracter con el que trabaja dependiendo del contenido

def mostrar_info(caracter):
    global numero_actual #Variable usada como global, esto hace que no se actualice la variable cada vez que se llama a la función

    if caracter == "<Enter>":
        operandos.append(float(numero_actual)) #Se introduce a la lista
        numero_actual = "" #Se resetea la variable, para el siguiente número
    elif caracter == "+":
        numero_actual = suma(operandos)
    elif caracter == "-":
        numero_actual = resta(operandos)
    elif caracter == "x":
        numero_actual = producto(operandos)
    elif caracter == "/":
        numero_actual = divison(operandos)
    elif caracter == "RESULT": #Se muestra el resultado
        caracter_pulsado.config(text = numero_actual)
    elif caracter == "RESET": #Se resetean los parámetros
        numero_actual = ""
        operandos.clear()
        caracter_pulsado.config(text = "")
    else: #Si es un número se concatena
        numero_actual += str(caracter)
        caracter_pulsado.config(text = numero_actual)

    print(operandos) #Útil para depurar
    print(numero_actual) #Útil para depurar

instrucciones = Tk() #Ventana que muestra las instrucciones
instrucciones.title("Instrucciones")

instrucciones = Label(instrucciones, text = "INSTRUCCIONES:\n\n- Presiona <Enter> después de introducir un número (1 o + cifras)\n- Cuando se termine de introducir datos pulsar: operación -> RESULT\n- Se debe empezar presionando un botón numérico\n- Para concatenar operaciones se debe obtener previamente un RESULT y presionar <Enter>\n- El botón RESET cancela la operación en cualquier punto\n\nEj: 1 -> <Enter> -> 3 -> <Enter> -> + -> RESULT -> <Enter> -> 1 -> <Enter> -> - -> RESULT").pack(fill = BOTH) 

root = Tk() #Creación de la ventana
root.title("Calculadora v1")

#No se puede poner el .grid en el mismo objeto, ya que al evaluarlo, la función "mostrar_info" lo detecta como nulo 
caracter_pulsado = Label(root, text = " ", padx = 35, pady = 25, borderwidth = 2, relief = "solid") #Etiqueta del nombre de donde se van mostrando los caracteres pulsados
caracter_pulsado.grid(row = 1, column = 0, columnspan = 4, sticky = "ew") 

#Generación y colocación de los botones de números    

botones = {} #Diccionario, cada elemento lleva una etiqueta asociada (similar a map de C++)

for i in range(10):
    botones[i] = Button(root, text = str(i), command = lambda numero = i: mostrar_info(numero), width = 15, height = 5)

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

boton_suma = Button(root, text = "+", command = lambda: mostrar_info("+"), width = 10, height = 5).grid(row = 2, column = 3)
boton_resta = Button(root, text = "-", command = lambda: mostrar_info("-"), width = 10, height = 5).grid(row = 3, column = 3)
boton_prod = Button(root, text = "x", command = lambda: mostrar_info("x"), width = 10, height = 5).grid(row = 4, column = 3)
boton_div = Button(root, text = "/", command = lambda: mostrar_info("/"), width = 10   , height = 5).grid(row = 5, column = 3)
boton_enter = Button(root, text = "<Enter>", command = lambda: mostrar_info("<Enter>"), width = 4, height = 4).grid(row = 6, column = 0, columnspan = 4, sticky = "ew")
boton_result = Button(root, text = "RESULT", command = lambda: mostrar_info("RESULT"), width = 4, height = 4, bg = "red").grid(row = 7, column = 0, columnspan = 2, sticky = "ew")
boton_reset = Button(root, text = "RESET", command = lambda: mostrar_info("RESET"), width = 4, height = 4, bg = "red").grid(row = 7, column = 2, columnspan = 2, sticky = "ew")

autor = Label(root, text =  "Pedro Velasco Santana, 2024", bg = "blue").grid(row = 8, column = 0, columnspan = 4, sticky = "new") #Etiqueta autor

root.mainloop()
