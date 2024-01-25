"""

* Enunciado: Simula el funcionamiento de una máquina expendedora creando una operación
 * que reciba dinero (array de monedas) y un número que indique la selección del producto.
 * - El programa retornará el nombre del producto y un array con el dinero de vuelta
 (con el menor número de monedas).
 * - Si el dinero es insuficiente o el número de producto no existe, deberá indicarse con
 un mensaje y retornar todas las monedas.
 * - Si no hay dinero de vuelta, el array se retornará vacío.
 * - Para que resulte más simple, trabajaremos en céntimos con monedas de 5, 10, 50, 100 y 200.
 * - Debemos controlar que las monedas enviadas estén dentro de las soportadas.

"""

productos = {
    1: {'nombre': 'Gaseosa', 'precio': 2.00},
    2: {'nombre': 'Chocolate', 'precio': 3.00},
    3: {'nombre': 'Alfajor', 'precio': 2.00},
    4: {'nombre': 'Papas fritas', 'precio': 4.00},
    5: {'nombre': 'Caramelos', 'precio': 3.00}
}

cambio = [200, 100, 50, 25, 10, 5]

def vuelto(monedas):
    efectivo_ingresado = monedas
    diferencia = 0
    monedas_devueltas = [0] * len(cambio)

    while efectivo_ingresado > diferencia:
        for i in range(len(cambio)):                                # Ejemplos primera vuelta
            if efectivo_ingresado >= cambio[i]:                     # 1055 >= 200 , True
                cantidad = efectivo_ingresado // cambio[i]          # cantidad = 1055 // 200 , es igual a 5 (ignoramos 55)
                monedas_devueltas[i] += cantidad                    # monedas_devueltas[0] == 5 , [5, 0, 0, 0, 0, 0]
                for j in range(len(cambio)):
                    diferencia += monedas_devueltas[j] * cambio[j]  # diferencia = monedas_devueltas[i] (5) * cambio[i] (200) quedaria en 1000
                efectivo_ingresado -= cantidad * cambio[i]          # efectivo_ingresado -= 5 * 200 , quedaria en 55

    totales = []
    for i in range(len(cambio)):
        if monedas_devueltas[i] > 0:
            descripcion = f"{monedas_devueltas[i]} billetes de: {cambio[i]}"

            totales.append(descripcion)

    return ', '.join(totales)
def maquina(monedas, seleccion):
    nombre_producto = productos[seleccion]["nombre"]
    precio_producto = int(productos[seleccion]["precio"] * 100)
    monedas = sum(monedas)


    if monedas > precio_producto:
        return f"Aqui tienes tu {nombre_producto} y tu vuelto: {vuelto(monedas)}"

    elif monedas < precio_producto:
        faltante = monedas - precio_producto
        return f"No te alcanza, te faltan {abs(faltante)} monedas"


    return nombre_producto, precio_producto


dinero = [10]
print(maquina(dinero, 1))