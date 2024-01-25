"""

 * Enunciado: Crea una función que sume 2 números y retorne su resultado pasados unos segundos.
 * - Recibirá por parámetros los 2 números a sumar y los segundos que debe tardar en
 finalizar su ejecución.
 * - Si el lenguaje lo soporta, deberá retornar el resultado de forma asíncrona,
 es decir, sin detener la ejecución del programa principal. Se podría ejecutar varias veces
 al mismo tiempo.


"""
import asyncio

async def parando_el_tiempo(num1, num2, segundos):
    while True:
        await asyncio.sleep(segundos)
        total = num1 + num2
        print(total)

asyncio.run(parando_el_tiempo(2, 3, 3))


