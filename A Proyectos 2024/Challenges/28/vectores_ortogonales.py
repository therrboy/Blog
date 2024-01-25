"""

 * Enunciado: Crea un programa que determine si dos vectores son ortogonales.
 * - Los dos array deben tener la misma longitud.
 * - Cada vector se podría representar como un array. Ejemplo: [1, -2]

"""

def son_ortogonales(vector1, vector2):
    if len(vector1) != len(vector2):
        return False

    producto_escalar = sum(a * b for a, b in zip(vector1, vector2))

    return producto_escalar == 0

vector_a = [1, -2]
vector_b = [3, 1]

if son_ortogonales(vector_a, vector_b):
    print("Los vectores son ortogonales.")
else:
    print("Los vectores no son ortogonales.")