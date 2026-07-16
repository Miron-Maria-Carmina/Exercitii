
def numara_cuvinte(text:str):
    for semn in ',;?!.':
        text = text.replace(semn, ' ')

    cuvinte = text.split()
    return len(cuvinte)


sir='Numaram mai, multe!cuvinte.'
print(numara_cuvinte(sir))