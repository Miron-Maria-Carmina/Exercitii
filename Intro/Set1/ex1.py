import math
from functools import reduce

def cmmdc_manual(lista_numere):

    rezultat = lista_numere[0]

    for i in range(1, len(lista_numere)):
        a = rezultat
        b = lista_numere[i]

        while b != 0:
             a=b
             b =  a % b

        rezultat = a

        if rezultat == 1:
            break

    return rezultat


def cmmdc_multiplu(*args):

    if not args:
        return None

    return reduce(math.gcd, args)

numere = [48, 70, 12]
print(cmmdc_manual(numere))