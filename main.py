
from funciones import *

_RUTA_FICHERO = "piramide.txt"

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
        

        



