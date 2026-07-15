import math

def maxim(a,b,c):
    if a>b and a>c:
        return a
    else:
        if b>c:
            return b
        else:
            return c

def operatii(a,b,op):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    elif op=='/':
        return a/b

def palindrom(x:int):
    n=x
    ogl=0
    while n!=0:
        c=n%10
        n=n//10
        ogl=ogl*10+c
    if x==ogl:

        return True
    else:
        return False

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
def afisare_lista(lista):
    print('Lista are elementele')
    for i in range(0,len(lista)):
        print(lista[i])

def medii(lista):
    min=lista[0]
    max=lista[0]
    sum=lista[0]
    for i in range(1, len(lista)):
        sum+=lista[i]
        if min>lista[i]:
            min=lista[i]
        if max<lista[i]:
            max=lista[i]
    med=sum/len(lista)
    print("Media numerelor din lista este: ", med)
    mg=math.sqrt(min*max)
    print("Media geometrica a numerelor din lista este: ", mg)

def min_si_max(lista):
    mijloc=len(lista)//2
    max_list=lista[:mijloc]
    min_list=lista[mijloc:]
    maximul=max(max_list)
    minim=min(min_list)
    print('Maximul din prima jumatate a listei ', maximul)
    print('Minimul din din a doua jumatate a listei ',minim)

def palindrom_si_par(lista):
    rezultat=[]
    for i in range(0,len(lista)):
        ok=palindrom(lista[i])
        sir_numar = str(abs(lista[i]))
        if ok==True and len(sir_numar) % 2 == 0:
            rezultat.append(lista[i])
    return rezultat
def sublista_intre_min_si_max(lista):

    valoare_min = min(lista)
    valoare_max = max(lista)

    index_min = lista.index(valoare_min)
    index_max = lista.index(valoare_max)

    start = min(index_min, index_max)
    end = max(index_min, index_max)

    return lista[start : end + 1]


def diagonala_sortata(matrice):

    diagonala = [matrice[i][i] for i in range(len(matrice))]
    return sorted(diagonala, reverse=True)

def main():
    print('ex5')
    x=2**1024
    x=str(x)
    print( len(x))

    print('ex6')
    a=7
    b=9
    c=4
    m=maxim(a,b,c)
    print('Maximul este' , m)

    print('ex7')
    op=input('Alegeti operatia ')
    print(operatii(a,b,op))

    print('ex8')
    x=input('Intoduceti numarul pentru a verifica daca e palindrom')
    ok=palindrom(int(x))
    if ok==True:
        print('numarul este palindrom')
    else:
        print('numarul nu este palindrom')
    x = input('Intoduceti numarul pentru a verifica daca e palindrom')
    ok=palindrom(int(x))
    if ok==True:
        print('numarul este palindrom')
    else:
        print('numarul nu este palindrom')

    print('ex9')
    prim=este_prim(a)
    if prim==False:
        print('Numarul ',a,' nu este prim')
    else :
        print('Numarul ',a,' este prim')

    print('ex10')
    lista=[4,2,7,6,78,5]
    afisare_lista(lista)

    print('ex11')
    medii(lista)
    print('ex12')
    min_si_max(lista)

    print('ex13')
    numere = [121, 1221, 3443, 56, 123, 77, 8888]
    print(palindrom_si_par(numere))

    print('ex14')
    print(sublista_intre_min_si_max(lista))

    print('ex15')
    matrice = [[10, 2, 3],[4, 50, 6],[7, 8, 5]]
    print(diagonala_sortata(matrice))

if __name__ == "__main__":
    main()
