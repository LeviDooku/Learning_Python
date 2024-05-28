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
            mensaje = "Esto es una excepción personalizada"
        self.mensaje = mensaje
        super().__init__(mensaje)

#Función para definir 
def edad_valida(edad):
    if edad < 0 or edad > 120:
        raise ExcepcionPersonalizada("[-] ERROR: Edad ingresada inválida")
    return "Edad validada correctamente"

while True: 
    try:
        edad = int(input("Introduzca su edad: "))
        edad_valida(edad)
        break
    except ExcepcionPersonalizada as e:
        print(e.mensaje)

print(f"Edad ingresada: {edad}")
