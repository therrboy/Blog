"""

* Enunciado: Crea una función que calcule y retorne cuántos días hay entre dos cadenas
de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará
 una excepción.

la funcion toma 2 cadenas de textos como dia/mes/año
esas cadenas hay que pasarlas a numero
hay que comparar las 2 cadenas para saber cuantos dias tienen entre si
la comparacion tiene que ser indiferente como ingresaron las fechas, ej: 12/12/2023 - 12/12/2000 (al reves digamos)
el retorno es un INT no un STRING
si la fecha se ingreso mal se envia una excepcion
"""

from datetime import datetime

def fechas(fecha1, fecha2):
    # Dividir la cadena en partes usando '/'
    fecha1_lista = fecha1.split('/')
    fecha2_lista = fecha2.split('/')

    if len(fecha1_lista) == 3 and len(fecha2_lista) == 3:
        try:
            # Convertir las fechas a objetos datetime
            fecha1 = datetime.strptime("-".join(fecha1_lista), "%d-%m-%Y")
            fecha2 = datetime.strptime("-".join(fecha2_lista), "%d-%m-%Y")
            diferencia_en_dias = abs((fecha2 - fecha1).days)

            # Verificar si el año tiene 4 dígitos
            if len(fecha1_lista[2]) != 4 or len(fecha2_lista[2]) != 4:
                raise ValueError("Año debe tener 4 dígitos")

            print("Fechas válidas")
            print(f"La diferencia en dias es de {diferencia_en_dias}")
        except ValueError as e:
            print(f"Error en las fechas: {e}")
    else:
        print("Formato de fecha incorrecto")


fechas("12/12/1991", "14/12/1999")