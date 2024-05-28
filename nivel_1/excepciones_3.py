##################################
#Autor: Pedro Velasco Santana    #
#                                #
#Archivo: excepciones_3.py       #
##################################

#Crear excepciones personalizadas a partir de una clase que hereda de clase Exception

#Como las clases y herencia es algo que ya tengo asumido, no voy a centrarme en explicarlo aquí, si eso más adelante

#La clase ExcepcionPersonalizada hereda de Exception
class ExcepcionPersonalizada(Exception):

    #Constructor de la clase
    def __init__(self, mensaje = None):
        if mensaje is None:
            mensaje = "Esto es una excepción personalizada, y este es su mensaje por defecto"
        self.mensaje = mensaje
        super().__init__(mensaje)

#Función para definir cuando se lanzará la excepción creada
def edad_valida(edad):
    if edad < 0 or edad > 120:
        raise ExcepcionPersonalizada("[-] ERROR: Edad ingresada inválida")
    return "Edad validada correctamente"

while True: #Bucle infinito hasta ingresar una edad adecuada
    try:
        edad = int(input("Introduzca su edad: "))
        edad_valida(edad) #Se evalua la edad ingresada
        break
    except ExcepcionPersonalizada as e: #"as e" captura una instancia de la excepción y permite acceder a sus atributos
        print(e.mensaje)

print(f"Edad ingresada: {edad}")
