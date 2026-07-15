
def num_vocale(cuvant:str):
    numara=0
    for i in cuvant.lower():
        if i in 'aeiou':
            numara+=1

    return numara

sir=input('Introduceti cuvant')
print(num_vocale(sir))