"""

 * Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima
 otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.

la funcion recibe 2 textos.
tiene que devolver 2 textos.
al devolver el texto 1 tiene que tener las letras de ese texto que no se repitan en el segundo
caso contraria para el segundo texto

"""

retornado1 = []
retornado2 = []
texto_comun = []

texto1 = "Hola como estas"
texto2 = "Todo bien y vos"
def devoluciones(texto1, texto2):
    for letra1 in texto1:
        for letra2 in texto2:
            if letra1 == letra2:
                if letra1 in texto_comun:
                    break
                else:
                    texto_comun.append(letra1)

    retornado1 = ''.join(letra for letra in texto1 if letra not in texto_comun)
    retornado2 = ''.join(letra for letra in texto2 if letra not in texto_comun)

    print(texto_comun)
    print(f"Retorno texto1 = {retornado1}")
    print(f"Retorno texto2 = {retornado2}")

devoluciones(texto1, texto2)