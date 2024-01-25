"""

 * Enunciado: Crea una función que reciba dos array, un booleano y retorne un array.
 * - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
 * - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
 * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.

"""


def conjuntos(array1, array2, booleano):
    texto_comun = []
    texto_diferente = []
    for palabra1 in array1:
        encontrado = False
        for palabra2 in array2:
            if palabra1 == palabra2:
                texto_comun.append(palabra1)
                encontrado = True
                break

        if not encontrado:
            texto_diferente.append(palabra1)
    if booleano:
        return texto_comun
    else:
        return texto_diferente

texto1 = ["Todo", "bien", "y", "usted?"]
texto2 = ["Todo", "bien", "y", "tu?"]
prueba = conjuntos(texto1, texto2, True)
print(prueba)
