nr = input("Cate carti doriti sa adaugati in biblioteca")
lista_carti = []
lista_nume_carti = []
an_referinta = int(input("Introduceti anul de referinta"))
for i in range (int(nr)):
    nume_var = input("Numele cartii")
    autor_var = input("Autorul cartii")
    an_var = int(input("Anul fabricatiei"))
    biblioteca = {'nume':nume_var,'autor':autor_var,'an':an_var}
    lista_carti.append(biblioteca)
    if an_referinta <= an_var:
        lista_nume_carti.append(nume_var)

print(lista_carti)
for i in lista_nume_carti:
    print(i,"a fost publicata dupa ", an_referinta)

