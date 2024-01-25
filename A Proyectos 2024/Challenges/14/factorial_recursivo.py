"""

 * Enunciado: Escribe una función que calcule y retorne el factorial de un número
 dado de forma recursiva.

- la funcion toma un numero
"""

def factorial(n):
    # Caso base
    if n == 0 or n == 1:
        return 1
    # Caso recursivo
    else:
        return n * factorial(n-1)  # La funcion se llama asi mismo, una y otra ves hasta llegar en este caso a 1

# Ejemplo de uso
resultado = factorial(6)
print("El factorial es:", resultado)