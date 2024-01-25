"""

 * Enunciado: Crea un programa que calcule quien gana más partidas al piedra, papel, tijera.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "R" (piedra), "P" (papel) o "S" (tijera).
 * - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".

"""

def juego(jugadas):
    ganador_1 = 0
    ganador_2 = 0

    for jugada in jugadas:
        if jugada[0] == jugada[1]:
            continue  # Empate, no se suma a nadie

        if (jugada[0] == "R" and jugada[1] == "S") or \
           (jugada[0] == "P" and jugada[1] == "R") or \
           (jugada[0] == "S" and jugada[1] == "P"):
            ganador_1 += 1
        else:
            ganador_2 += 1

    if ganador_1 > ganador_2:
        print(f"El jugador player1 ganó")
    elif ganador_1 < ganador_2:
        print(f"El jugador player2 ganó")
    else:
        print("Los jugadores empataron")


jugadas = [("R", "S"), ("S", "R"), ("P", "S")]

juego(jugadas)

