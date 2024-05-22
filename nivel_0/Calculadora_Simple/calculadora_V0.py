#Versión en terminal de un proyecto más ambicioso

#Funciones para las distintas operaciones

def suma(operandos):
    
    return True

def resta(operandos):
    
    return True

def producto(operandos):
    
    return True

def divison(operandos):
    
    return True

def switch(cod_operacion):
    if cod_operacion == 1:
        return "\n\nSuma seleccionada\n\n"
    elif cod_operacion == 2: 
        return "\n\nResta seleccionada\n\n"
    elif cod_operacion == 3: 
        return "\n\nProducto seleccionada\n\n"
    elif cod_operacion == 4: 
        return "\n\nDivisión seleccionada\n\n"
    else:
        return "[-] ERROR: código de operación no válido"

print("***************************************\n         CALCULADORA PYTHON V0\n***************************************\n")
cod_operacion = int(input("\n\n[+] ¿Qué operación desea realizar? SUMA(1) RESTA(2) PRODUCTO(3) DIVISIÓN(4) : "))
while cod_operacion < 1 or cod_operacion > 4:
    cod_operacion = int(input("\n\n[+] Código de operación no válido SUMA(1) RESTA(2) PRODUCTO(3) DIVISIÓN(4) : "))
print(switch(cod_operacion))

operandos = list()

indice = int(0)
while True: 
    numero = input(f"[+] Ingrese operando #{indice} (<Enter> para terminar): ")

    if not numero:
        break
    elif indice > 0 and cod_operacion == 4 and float(numero) == 0:
        print("[-] ERROR: el divisior no puede ser 0")
        break

    operandos.append(float(numero))
    indice += 1

