import random
NOMBREARCHIVO="PalabrasIngles.txt"
with open(NOMBREARCHIVO, "r") as Archivo:
    for Linea in Archivo:
        Palabra = Linea.strip()
        print(Palabra)