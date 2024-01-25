"""

* Enunciado: Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
 * - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
 * - EXTRA: ¿Eres capaz de dibujar más figuras?

"""


def figura(fig, tamaño):
    if fig == "cuadrado":
        for x in range(tamaño):
            print("* " * tamaño)

    if fig == "triangulo":
        for x in range(1, tamaño + 1):
            espacios = (tamaño - x) * " "
            if x == 1:
                tam_x = (x * "x")
            elif x % 2 != 0:
                tam_x = ((x * 2) - 1) * "x"
            else:
                tam_x = (2 * x - 1) * "x"

            print(f"{espacios}{tam_x}")

    if fig == "rombo":
        for i in range(tamaño):
            espacios = " " * (tamaño - i - 1)
            asteriscos = "* " * (i + 1)
            print(espacios + asteriscos)
        for i in range(tamaño - 2, -1, -1):
            espacios = " " * (tamaño - i - 1)
            asteriscos = "* " * (i + 1)
            print(espacios + asteriscos)

figura("triangulo", 4)