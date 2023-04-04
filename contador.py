
def count_word(texto):
    result = {}

    palabras = texto.lower().split() #Cambia las mayusculas por minusculas
    for palabra in palabras:
        if palabra in result:
            result[palabra] += 1 #Si existe la palabra, la suma
        else:
            result[palabra] = 1 #Si no existe la palabra, la agrega

    return result

