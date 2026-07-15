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
        print('numarul este palindrom')
    else:
        print('numarul nu este palindrom')

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
    palindrom(int(x))
    x = input('Intoduceti numarul pentru a verifica daca e palindrom')
    palindrom(int(x))

    print('ex9')
    prim=este_prim(a)
    if prim==False:
        print('Numarul ',a,' nu este prim')
    else :
        print('Numarul ',a,' este prim')

    print('ex10')
    lista=[1,4,2,6,78]
    afisare_lista(lista)

    print('ex11')
    medii(lista)

if __name__ == "__main__":
    main()
