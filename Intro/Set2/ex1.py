
def fibonacci(n):
    a=1
    b=1
    print(a,b,end=" ")
    for i in range(n-2):
        c=a+b
        print(c,end=" ")
        a=b
        b=c

n=input('introdiceti cate elemente ale sirului lui fibonacci doriti')
print(fibonacci(int(n)))