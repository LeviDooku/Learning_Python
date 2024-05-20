#Script que busca un nombre en una lista de nombres introducidos por el usuario

#Se usa un set en vez de list, para evitar nombres repetidos

c_nombres = set()
indice = int(0)

print("Introduzca los nombres (presione <enter> para terminar): \n")

#Forma bastante mala de introducir datos, pero todavía no se tanto 

while True:
    nombre = str(input(f"Nombre número #{indice}: "))
    if not nombre:
        break
    c_nombres.add(nombre)
    indice += 1

print("\nConjunto introducido: ")
print(c_nombres)

print("\n¿Desea comprobar algún nombre? (Y/N)\n")
caracter = str(input())

if caracter != 'Y':
    print("Programa acabado\n")
else:
    print("\n¿Qué nombre desea buscar?\n")
    a_buscar = str(input())
    if a_buscar in c_nombres:
        print(f"El nombre {a_buscar} se encuentra en el conjunto")
    else:
        print(f"El nombre {a_buscar} no se encuentra en el conjunto")


