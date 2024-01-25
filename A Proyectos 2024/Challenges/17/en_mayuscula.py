"""

* Enunciado: Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.

la funcion recibe un texto
el texto lo agregamos a una lista con un for separando las palabras
hacemos un for para que cada primer letra de cada palabra este en mayuscula
"""

def texto_mayuscula(texto):
    lista_separada = []
    lista_texto = texto.split(' ')

    for palabra in lista_texto:
        lista_separada.append(palabra.capitalize())

    resultado = " ".join(lista_separada)
    print(resultado)

texto_mayuscula("Hola como estas hoy?")