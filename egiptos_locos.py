######################### EGIPCIOS LOCOS #############################
#  Crea un programa que le pida al usuario si quieres saber cuantas piramides existen o si quiere añadir una piramide.
#  Si el usuario decide escribir una piramide nueva, se le preguntará cuantos niveles quiere que tenga la piramide.
#    A continuación se escribirá una piramide de tantos niveles como a pedido el usuario en un fichero llamado piramides.txt
#    Ej: Si el usuario quiere una piramide de nivel 2 lo que se tiene que escribir en el fichero es lo siguiente:
# *
#***
#    Ej: Si el usuario quiere piramide de nivel 4 sería asi:
#   *
#  ***
# *****
#*******
from funciones import *

_RUTA_FICHERO = "./piramides/piramide_2.txt"

while True:
    try:
        eleccion_usuario = int(input("Pulsa 1 para saber cuantas piramides hay o pulsa 2 para añadir una piramide: "))
    except ValueError:
        print("Ingrese un numero valido")
    
    if eleccion_usuario == 1:
        cantidad_piramides = contar_piramides(_RUTA_FICHERO)

        if cantidad_piramides != None:
            print(f"El numero de piramides es: {cantidad_piramides}")
    
    elif eleccion_usuario == 2:
        pedir_niveles = int(input("Cuantos niveles quieres que tenga tu piramide?: "))
        
        piramide_lista = crear_piramide(pedir_niveles)
        
        añadir_piramides(piramide_lista, _RUTA_FICHERO)
        
        print("La piramide se ha añadido.")
        

        



