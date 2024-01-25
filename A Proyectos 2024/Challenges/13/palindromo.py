"""

 * Enunciado: Escribe una función que reciba un texto y retorne verdadero o falso (Boolean)
 según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha
 que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.

- La funcion recibe texto
retorna verdadero o falso
guarda la palabra en un diccionario
se compara la palabra al derecho y al reves
no importa si hay espacios, signos o tildes.

"""
import unicodedata

def quitar_tildes(cadena):
    return ''.join((c for c in unicodedata.normalize('NFD', cadena) if unicodedata.category(c) != 'Mn'))


def palindromo(texto):
    texto_diccionario = []
    letra_sin_tilde = quitar_tildes(texto)

    for letra in letra_sin_tilde:
        if letra != " ":
            texto_diccionario.append(letra.lower())

    texto_diccionario_invertido = texto_diccionario[::-1]

    if texto_diccionario == texto_diccionario_invertido:
        return True
    else:
        return False

print(palindromo("Hola alóh"))