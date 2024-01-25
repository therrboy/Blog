"""
* Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso
(Boolean) según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra
 inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
"""


def enunciado(palabra1, palabra2):
    lista1 = list(palabra1)
    lista2 = list(palabra2)

    if palabra1 == palabra2:
        return False

    lista1.sort()
    lista2.sort()

    return lista1 == lista2


resultado = enunciado("casa", "saca")
print(resultado)