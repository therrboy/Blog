"""
* Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de
calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
"""

class Poligono:
    def triangulo(self, base, altura):  # triángulo Isósceles area = base x altura / 2
        area = base * altura / 2
        print(f"el area de un triangulo es {int(area)} centimetros cuadrados")

    def cuadrado(self, lado=None):
        area = lado * lado
        print(f"el area de un cuadrado es {int(area)} centimetros cuadrados")

    def rectangulo(self, base, altura):
        area = base * altura
        print(f"el area de un rectangulo es {int(area)} centimetros cuadrados")

mi_poligono = Poligono()

mi_poligono.cuadrado(4)
mi_poligono.triangulo(4, 4)
mi_poligono.rectangulo(4, 8)


