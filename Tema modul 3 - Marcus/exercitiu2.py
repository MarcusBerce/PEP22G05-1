caractere = input("introduceti un sir de caractere:")
lista = list(caractere)
vocale = 0
for i in lista:
    if i == "a" or i == "e" or i == "o" or i == "u" or i == "i":
        vocale = vocale + 1
print(vocale)