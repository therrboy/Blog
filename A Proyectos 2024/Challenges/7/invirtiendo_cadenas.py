"""
* Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar
funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def palabra(palabra):
    lista = list(palabra)
    invertido = ''.join(map(str, reversed(lista)))
    print(invertido)

palabra("Hola mundo")