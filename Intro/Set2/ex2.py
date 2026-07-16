import math
def este_prim(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(2,math.isqrt(n),1):
        if n % i == 0:
            return False
    return True

def lista_prim(lista):
    listanou=[]
    for n in lista:
        if este_prim(n)==True:
            listanou.append(n)
    return listanou

list=[344,3,65,5,98]
print(lista_prim(list))