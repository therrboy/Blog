"""

 * Enunciado: Escribe una función que calcule si un número dado es un número de Amstrong
 (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información al respecto.

número natural que es igual a la suma de sus propios dígitos cada uno elevado a la potencia
de la cantidad total de dígitos. Para entenderlo más claramente, considera un número de N
digitos "abcd" donde a, b, c, d son digitos individuales. El numero es un numero de armstrong
si:

a^n + b^n + c^n + d^n = abcd
1^4 + 6^4 + 3^4 + 4^4 = 1634
1   + 1296+ 81  + 256 = 1634

la funcion toma un numero
se guarda ese numero para compararlo mas adelante
se hace la cuenta para ver cuanto da
se compara el numero final
"""

def armstrong(numero):
    numero_original = numero                        # 1634
    numero_suma = 0
    cantidad_num = len(str(numero))                 # esto es 4

    temp_numero = numero                            # copia del numero original
    while temp_numero > 0:                          # mientras el numero sea mayor a 0
        digito = temp_numero % 10                   # La operación % 10 obtiene el último dígito del número (temp_numero)
        numero_suma += digito ** cantidad_num
        temp_numero //= 10                          # Se elimina el ultimo digito

    return numero_suma == numero_original

print(armstrong(1634))