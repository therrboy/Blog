"""

 * Enunciado: Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
 ¿De cuántas maneras eres capaz de hacerlo? Crea el código para cada una de ellas.


"""


def numero_1():
    for num in range(1, 101):
        print(num)


def numero_2():
    numero = 1
    while numero != 101:
        print(numero)
        numero += 1


def numero_3():
    print(*range(1, 101), sep='\n')


def numero_4(n):
    if n <= 100:
        print(n)
        numero_4(n + 1)


def numero_5():
    count = iter(range(1, 101))
    print(*count, sep='\n')


def numero_6():
    print(*(i for i in range(1, 101)), sep='\n')
