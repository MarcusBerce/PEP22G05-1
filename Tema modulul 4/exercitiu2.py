nr = input("Cate carti doriti sa adaugati in biblioteca")
lista_carti = []
for i in range (int(nr)):
    nume_var = input("Numele cartii")
    autor_var = input("Autorul cartii")
    an_var = input("Anul fabricatiei")
    biblioteca = {'nume':nume_var,'autor':autor_var,'an':an_var}
    lista_carti.append(biblioteca)

print(lista_carti)