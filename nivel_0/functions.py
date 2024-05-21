#Aprender a usar funciones en Python

#Script que a partir de una lista devuelve otra con los números primos presentes

def es_primo(_numero):
    contador = int(0)
    divisor = int(1)
    if _numero < 0:
        return False
    else: 
        while divisor <= _numero:
            if _numero % divisor == 0:
                contador += 1
            divisor += 1
        return True if contador == 2 else False #Operador ternario 

def devuelve_primo(_candidatos):
    conjunto_primos = list() #Se crea lista vacía

    for i in _candidatos:
        if es_primo(i):
            conjunto_primos.append(i)

    return conjunto_primos


_candidatos = list() #El caracter "_" indica que la variable no debe ser modificada
indice = int(0)
total = int(input("¿Cuántos números tendrá la lista?: "))

for i in range(total): #Determina el número de iteraciones en el bucle
    numero = int(input(f"Número índice #{indice}: "))
    _candidatos.append(numero)
    indice += 1

print(f"\nLista ingresada: {_candidatos}\n")
lista_resultado = devuelve_primo(_candidatos) 
print(f"Lista resultado: {lista_resultado}\n")
