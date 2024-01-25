"""

* Enunciado: Crea una función que evalúe si un/a atleta ha superado correctamente una
 * carrera de obstáculos.
 * - La función recibirá dos parámetros:
 *      - Un array que sólo puede contener String con las palabras "run" o "jump"
 *      - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
 * - La función imprimirá cómo ha finalizado la carrera:
 *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no
 *        variará el símbolo de esa parte de la pista.
 *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
 *      - Si hace "run" en "|" (valla), se variará la pista por "/".
 * - La función retornará un Boolean que indique si ha superado la carrera.
 * Para ello tiene que realizar la opción correcta en cada tramo de la pista.

la funcion recibe 2 parametros
el primer parametro es un Array que contiene un string que es "run" o "jump"
el segundo parametro es un String que solo contiene "_" = suelo o "/" = valla
la funcion imprime como finaliza la carrera con un booleano
el primer parametro es el atleta que hace "run" o "jump"
el segundo parametro es la pista que hace "_" = suelo o "/" = valla
si el primer parametro hace "jump" en suelo la pista pone X, si hace "run" en valla se pone "-" sino la pista queda igual
hay que comparar paso por paso de ambas listas, en sus posiciones iguales

"""

atleta_mov = ["run", "jump", "run", "jump", "run", "run", "run"]
pista_mov = "_ / _ / _ _ _"

def carrera(atleta, pista):
    contador = 0
    pista_separado = pista.split(' ')

    while len(pista_separado) > contador:
        if atleta[contador] == "run" and pista_separado[contador] == "_":
            contador += 1
        elif atleta[contador] == "jump" and pista_separado[contador] == "/":
            contador += 1
        else:
            return False
    return True


print(carrera(atleta_mov, pista_mov))
