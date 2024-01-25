"""

 * Enunciado: Crea una función que reciba días, horas, minutos y segundos
 (como enteros) y retorne su resultado en milisegundos.

"""


def conversor(dias, horas, minutos, segundos):
    dias_m = dias * 24 * 60 * 60 * 1000
    horas_m = horas * 60 * 60 * 1000
    minutos_m = minutos * 60 * 1000
    segundos_m = segundos * 1000
    total = dias_m + horas_m + minutos_m + segundos_m
    return total


print(conversor(1, 1, 1, 1))