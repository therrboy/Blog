"""
* Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.

 crear funcion, tiene que recibir texto y codigo morse, tiene que transformar el texto a codigo morse o viceversa,
 el programa debe identificar si es codigo morse o texto, el morse entre letras deja 1 espacio, entre palabras deja 2,
hay letras y numeros.
"""

codigo_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

def palabra_a_morse(palabra):
    lista_nueva = []

    for letra in palabra:
        if letra.upper() == ' ':
            lista_nueva.append(' ')
        else:
            for clave, valor in codigo_morse.items():
                if letra.upper() == clave:
                    lista_nueva.append(valor)

    texto_final = " ".join(lista_nueva)
    print(f"el codigo morse es: {texto_final}")

def palabra_a_texto(texto):
    lista_nueva = []
    texto = texto.split(" ")

    for palabra in texto:
        if palabra == '':
            lista_nueva.append(' ')
        else:
            for clave, valor in codigo_morse.items():
                if palabra == valor:
                    lista_nueva.append(clave)

    texto_final = "".join(lista_nueva)
    print(f"lista con letras: {texto_final}")

palabra_a_texto('.-.. .-   -.-. .- ... .-   -.. .   .- .-..   .-.. .- -.. ---')
palabra_a_morse("la casa de al lado")
