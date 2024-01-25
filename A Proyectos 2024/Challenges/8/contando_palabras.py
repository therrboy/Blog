"""
* Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que
muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
"""

import string

texto = "Hola Hola Hola Hola como Hola Hola Hola Hola como estas?"

# Eliminar signos de puntuación y convertir a minúsculas
texto_limpio = texto.translate(str.maketrans("", "", string.punctuation)).lower()

# Convertir el texto limpio a una lista de palabras
lista_de_palabras = texto_limpio.split()


def contador(palabra):
    conteo = 0
    palabra = palabra.lower()
    for x in lista_de_palabras:
        if x == palabra:
            conteo += 1

    print(f"La palabra {palabra} aparece {conteo} veces")

total = contador("HOLA")