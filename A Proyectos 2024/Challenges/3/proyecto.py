"""
* Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de
Fibonacci empezando en 0.
 * La serie Fibonacci se compone por una sucesión de números en la que el siguiente
 siempre es la suma de los dos anteriores.
 * 0, 1, 1, 2, 3, 5, 8, 13...
"""

# Inicializar la lista de Fibonacci con los primeros dos números
fibonacci = [0, 1]

# Generar los siguientes números de Fibonacci
for i in range(2, 50):
    # Sumar los dos números anteriores y agregar el resultado a la lista
    siguiente_numero = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(siguiente_numero)

# Imprimir la lista completa de Fibonacci
print(fibonacci)


