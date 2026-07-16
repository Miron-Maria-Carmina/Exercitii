
def siruri(st1:str,st2:str):
    numara=0
    cuv_st2=st2.lower().split()
    for cuv in cuv_st2:
        if cuv==st1:
            numara+=1
    return numara
sir1=('alb')
sir2=('casa albinuta alb altceva')
print(siruri(sir1,sir2))