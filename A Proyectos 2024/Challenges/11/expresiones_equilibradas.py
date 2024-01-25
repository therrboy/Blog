"""
 * Enunciado: Crea un programa que comprueba si los paréntesis, llaves y corchetes de una
 expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }

 la funcion tiene que poder recibir texto
 tiene que entender cuales son los delimitadores

"""


# delimitadores = ["{", "[", "(", ")", "]", "}"]
delimitadores = {
    "{": "}",
    "[": "]",
    "(": ")"
}
coincidencias = []

def equilibrados(texto):
    for letra in texto:
        for clave, valor in delimitadores.items():
            if letra == clave:
                coincidencias.append(letra)
            elif letra == valor:
                for i in range(len(coincidencias) - 1, -1, -1):
                    if coincidencias[i] == clave:
                        coincidencias.pop(i)
                        break
                else:
                    print("Error: Delimitadores no están balanceados.")
                    return

    if coincidencias:
        print("Error: Delimitadores no están balanceados.")
    else:
        print("Los delimitadores están balanceados.")


textos = "({[}])"
equilibrados(textos)
