"""

 * Enunciado: Crea una función que ordene y retorne una matriz de números.
 * - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro adicional
 *   "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor o de mayor a menor.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.

"""

import math


def crear_matriz(var_matriz, orden):
    # Ordenar la lista var_matriz en orden ascendente o descendente
    var_matriz = sorted(var_matriz, reverse=(orden == "Desc"))

    # Calcular la longitud de cada fila de la matriz
    longitud = math.ceil(len(var_matriz) / 3)

    # Crear la matriz dividiendo la lista ordenada en sublistas de longitud 'longitud'
    matriz = [var_matriz[i:i + longitud] for i in range(0, len(var_matriz), longitud)]

    for fila in matriz:
        print(fila)


crear_matriz([2, 4, 6, 8, 9, 10, 4, 7, 8, 8, 8, 8, 5, 7], "Asc")
