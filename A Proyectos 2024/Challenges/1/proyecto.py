"""
* Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100
(ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
* - Múltiplos de 3 por la palabra "fizz".
* - Múltiplos de 5 por la palabra "buzz".
* - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:   # Multiplos de 3 y 5
        print("multiplo de ambos")
    elif x % 3 == 0:                # Multiplos de 3
        print("multiplo de 3")
    elif x % 5 == 0:                # Multiplos de 5
        print("multiplo de 5")
    else:
        print(x)
