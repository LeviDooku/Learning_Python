#Script que pide al usuario sus datos y los muestra por pantalla

print("Introduzca su nombre: \n")

nombre = str(input())

while nombre == "":
    print("Debe introducir un nombre: \n")
    nombre = str(input())

#También es válido: nombre = input("Introduzca su nombre: \n")

print("\nIntroduzca ahora su edad: \n")

edad = int(input())

while edad < 0 or edad > 120:
    print("\nEdad no válida, pruebe de nuevo: \n")
    edad = int(input())

print(f"\nSu nombre es: {nombre}\n")
print(f"Su edad es: {edad}\n")