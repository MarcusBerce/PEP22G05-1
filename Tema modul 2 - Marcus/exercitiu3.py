nume1 = input("introduceti primul nume:")
nume2 = input("Introduceti al doilea nume:")

print(len(nume1))
if nume1 == nume2:
    print("Cele doua nume sunt egale")
else:
    print("Cele doua nume nu sunt la fel")
if len(nume1)>len(nume2):
    print("primul nume este mai lung decat al doilea")
else:
    print("primul nume nu este mai lung decat al doilea")
print(nume1[0])
print(nume1[::-1])

numar = int(input("Introduceti un numar de la tastatura:"))
multiplicare = nume1 * numar
print(multiplicare)