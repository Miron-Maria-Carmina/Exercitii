
def caractere_speciale(text:str)->bool:
    speciale={'\r', '\t', '\n', '\a', '\b', '\f', '\v'}
    for i in text:
        if i in speciale:
            return True

    return False

print(caractere_speciale('Hello\n'))
print(caractere_speciale('Salut'))