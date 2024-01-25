"""

* Enunciado: Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su resultado e
imprímelo.
 * - El .txt se corresponde con las entradas de una calculadora.
 * - Cada línea tendrá un número o una operación representada por un símbolo (alternando ambos).
 * - Soporta números enteros y decimales.
 * - Soporta las operaciones suma "+", resta "-", multiplicación "*" y división "/".
 * - El resultado se muestra al finalizar la lectura de la última línea (si el .txt es correcto).
 * - Si el formato del .txt no es correcto, se indicará que no se han podido resolver las operaciones.

"""

def procesar_problemas_matematicos(archivo):
    with open(archivo, 'r') as archivo_txt:                     # Abrimos el archivo en modo lectura
        lineas = archivo_txt.readlines()                        # hacemos una lista con los valores

    for linea in lineas:
        # Dividir la línea en operando1, operador y operando2
        operando1, operador, operando2 = linea.strip().split()  # strip() eliminamos espacios en blanco al principio y al final
                                                                # split() separa el texto en una lista ej [1, 2, 3]
        # Comprobar si la línea está vacía
        if not linea:
            continue  # Omitir líneas vacías

        # Convertir los operandos a números
        operando1 = float(operando1)
        operando2 = float(operando2)

        # total de cada uno
        if operador == "+":
            total = operando1 + operando2

        elif operador == "-":
            total = operando1 - operando2

        elif operador == "*":
            total = operando1 * operando2

        elif operador == "/":
            if operando1 != 0 and operando2 != 0:
                total = operando1 / operando2
            else:
                print("Error: División por cero.")
                continue
        else:
            print(f"Error: Operador no válido - {operador}")
            continue

        print(f"Total: {total}")

    # Ejemplo de uso
procesar_problemas_matematicos("calculadora.txt")