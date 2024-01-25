"""

 * Enunciado: Crea una función que analice una matriz 3x3 compuesta por
 "X" y "O" y retorne
 lo siguiente:
 * - "X" si han ganado las "X"
 * - "O" si han ganado los "O"
 * - "Empate" si ha habido un empate
 * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
 O si han ganado los 2.
 * Nota: La matriz puede no estar totalmente cubierta. Se podría representar con un
 vacío "", por ejemplo.

creo una matriz
tengo que analizar la matriz como un juego
hay que leer X y O, dar ganador, empate, o incorrecto (si se usa otra letra, si hay mucha dif entre cantidad de X e O)

"""

matriz_vacia = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

turno = 0


def hay_ganador(tablero):
    # Verificar filas
    for fila in tablero:
        if all(elemento == 'X' for elemento in fila) or all(elemento == 'O' for elemento in fila):
            return True

    # Verificar columnas
    for columna in range(3):
        if all(tablero[fila][columna] == 'X' for fila in range(3)) or all(
                tablero[fila][columna] == 'O' for fila in range(3)):
            return True

    # Verificar diagonales
    if all(tablero[i][i] == 'X' for i in range(3)) or all(tablero[i][2 - i] == 'O' for i in range(3)):
        return True

    return False


def obtener_ganador(turno):
    if turno % 2 == 0:
        return 'Jugador 1'
    else:
        return 'Jugador 2'


game = True
while game:
    if not hay_ganador(matriz_vacia):
        entrada_valida = False
        while not entrada_valida:
            entrada_usuario1 = input("Jugador 1, Ingrese fila y columna (0,1,2 - 0,1,2) ej, 0 2:  ")
            datos1 = entrada_usuario1.split()

            if len(datos1) == 2 and datos1[0].isdigit() and datos1[1].isdigit():
                fila1, columna1 = int(datos1[0]), int(datos1[1])

                if 0 <= fila1 <= 2 and 0 <= columna1 <= 2 and matriz_vacia[fila1][columna1] == ' ':
                    matriz_vacia[fila1][columna1] = 'X'
                    turno += 1
                    entrada_valida = True
                    print(matriz_vacia)
                else:
                    print("Error! Jugador 1 Ingrese valores válidos y una posición no ocupada. Vuelve a intentarlo.")
            else:
                print("Error! Jugador 1 Ingrese dos números separados por espacio. Vuelve a intentarlo.")

        entrada_valida = False
        while not entrada_valida:
            entrada_usuario2 = input("Jugador 2, Ingrese fila y columna (0,1,2 - 0,1,2) ej, 0 2:  ")
            datos2 = entrada_usuario2.split()

            if len(datos2) == 2 and datos2[0].isdigit() and datos2[1].isdigit():
                fila2, columna2 = int(datos2[0]), int(datos2[1])

                if 0 <= fila2 <= 2 and 0 <= columna2 <= 2 and matriz_vacia[fila2][columna2] == ' ':
                    matriz_vacia[fila2][columna2] = 'O'
                    turno += 1
                    entrada_valida = True
                    print(matriz_vacia)
                else:
                    print("Error! Jugador 2 Ingrese valores válidos y una posición no ocupada. Vuelve a intentarlo.")
            else:
                print("Error! Jugador 2 Ingrese dos números separados por espacio. Vuelve a intentarlo.")


    else:
        ganador = obtener_ganador(turno)
        print("¡{} gana!".format(ganador))
        game = False
