lista = ["abc",123,"1",1]
numarstr = 0
numarfloat = 0
numarint = 0
for i in lista:
    print(type(i))
    if type(i) == str:
        numarstr = numarstr + 1
    if type(i) == float:
        numarfloat = numarfloat + 1
    if type(i) == int:
        numarint = numarint + 1
print(numarint,numarfloat,numarstr)
