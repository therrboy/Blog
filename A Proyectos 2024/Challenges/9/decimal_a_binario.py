"""
 * Enunciado: Crea un programa se encargue de transformar un número decimal a binario
 sin utilizar funciones propias del lenguaje que lo hagan directamente.

    creo un DEF, tiene que tomar un numero, ingreso un numero (fijarse si tiene que ser entero sin ",")
    este numero se transforma a binario,
"""

def binario(numero):
    bin = []
    while numero > 0:
        bin.insert(0, numero % 2)  # Insertar el residuo al principio de la lista
        # (el 0 nos indica en que posicion van los numeros) si los ponemos de corrido no lee los 0
        # el programa por eso ponemos de esta manera ingresando.
        numero = numero // 2  # aca bajamos la cantidad del numero para que sea finito
    return bin


final = binario(8)
print(final)
