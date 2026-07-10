import random
NOMBREARCHIVO="PalabrasIngles.txt"
def Cargar_Archivo():
    with open(NOMBREARCHIVO, "r", encoding="utf-8") as Archivo:
        return [Linea.strip().upper() for Linea in Archivo]
def Obtener_Palabra_Aleatoria(Palabras):
    return random.choice(Palabras)
Total_Palabras=Cargar_Archivo()
Palabra_Aleatoria=Obtener_Palabra_Aleatoria(Total_Palabras)
print(Palabra_Aleatoria)