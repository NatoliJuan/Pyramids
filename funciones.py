def contar_piramides(ruta_fichero):
    contador = 0
    try:
        with open(ruta_fichero, "r") as fichero_abierto:
            contenido = fichero_abierto.readlines()
            for linea in contenido:
                #if not linea.startswith(" "):
                if linea.startswith("*"):
                    contador +=1    
            return contador
    except FileNotFoundError:
        print("Archivo no encontrado")
        return None

def añadir_piramides(piramide_lista,ruta_fichero):
    with open(ruta_fichero, "a") as fichero_abierto:
        for linea in piramide_lista:
            archivo = fichero_abierto.write(linea + "\n")
        return archivo
      
def crear_piramide(niveles):
   
    simbolo = "*"
    piramide_lista = []

    for nivel in range(1, niveles + 1):
        resultado = 1 + (nivel - 1) * 2
        espacio = niveles - nivel
        simbolos = resultado * simbolo
        linea = " " * espacio + simbolos

        piramide_lista.append(linea)
    
    return piramide_lista

            
          


                