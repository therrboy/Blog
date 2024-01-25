"""
Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 números primos entre 1 y 100: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 y 97
Los números primos son aquellos que solo son divisibles entre ellos mismos y el 1
"""
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Comprobar si un número es primo
def verificar_primo(numero):
    if es_primo(numero):
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")

# Imprimir números primos entre 1 y 100
print("Números primos entre 1 y 100:")
primos = [num for num in range(1, 101) if es_primo(num)]
print(primos)