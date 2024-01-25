"""

 * Enunciado: Crea dos funciones, una que calcule el máximo común divisor (MCD)
 y otra que calcule el mínimo común múltiplo (mcm) de dos números enteros.
 * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.

"""

def max_comun_div(num1, num2):
    comun_div = []
    for numero in range(1, num1 + 1):
        if num1 % numero == 0 and num2 % numero == 0:
            comun_div.append(numero)
            if len(comun_div) == 2:
                comun_div.pop(0)

    return comun_div

maximo = max_comun_div(10, 40)


def min_comun_mult(num1, num2):
    comun_num1 = []
    comun_num2 = []

    def factores(contador):
        comun_list = []
        divisor = 2
        while contador > 1:
            while contador % divisor == 0:
                comun_list.append(divisor)
                contador //= divisor
            divisor += 1
        return comun_list

    comun_num1 = factores(num1)
    comun_num2 = factores(num2)

    mcm = 1
    for factor in set(comun_num1 + comun_num2):
        count1 = comun_num1.count(factor)
        count2 = comun_num2.count(factor)
        mcm *= factor ** max(count1, count2)

    print("Mínimo común múltiplo:", mcm)

min_comun_mult(12, 18)