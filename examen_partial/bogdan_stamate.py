# 1. Creati o lista goala. Adaugati 5 elemente de tip integer la acea lista, apoi scoateti
# un element si o sa ramaneti cu 4. La lista ramasa, adunati 1 la fiecare element.
# Creati un dictionar cu 5 elemente si listati-le pe un rand nou.

lista=[]
lista.append(10)
lista.append(20)
lista.append(30)
lista.append(40)
lista.append(50)

print("Elementele din lista sunt: " + str(lista))

lista.pop()
print("Elementele din lista sunt: " + str(lista))

for i in range(len(lista)):
    lista[i]=lista[i]+1
print("Am adaugat 1 la fiecare element: " + str(lista))

dict={"Elena":24, "Maria":35, "Daniel": 38, "Anton":42, "Bogdan": 22}
print("Dictionarul cu 5 elemente: " + str(dict))

# 2. Creati un program care are trei functii. Pasand lista [1, 2, 5, 7, 8, 9, 11, 12, 13, 14,
# 15, 21] ca argument al functiei, o functie trebuie sa calculeze suma numerelor
# pare, cealalta suma numerelor impare, iar a treia functie suma numerelor prime.
# Fiecare functie trebuie sa returneze acea suma si apoi cu print trebuie sa afisati
# informatia pe ecran.

list=[1, 2, 5, 7, 8, 9, 11, 12, 13, 14,15, 21]

def numere_pare(lista_mea):
    suma=0
    for i in range(len(lista_mea)):
        if lista_mea[i] % 2 == 0:
            suma = suma+lista_mea[i]
    return suma

def numere_impare(lista_mea):
    suma = 0
    for i in range(len(lista_mea)):
        if lista_mea[i] % 2 != 0:
            suma = suma + lista_mea[i]
    return suma

def numere_prime(lista_mea):
    suma=0
    for i in range(len(lista_mea)):
        numar = lista_mea[i]
        if numar !=1:
            for j in range(2,numar):
                if numar % j == 0:
                    break
            else:
               suma = suma + numar
    return suma

print("Suma numerelor pare din lista este: " + str(numere_pare(list)))
print("Suma numerelor impare din lista este: " + str(numere_impare(list)))
print("Suma numerelor prime din lista este: " + str(numere_prime(list)))

# 3. Care sunt problemele la secventa de program de mai jos?
# d = 10
# while d:
#  if d == 5:
#  continue
#  d = d - 1
#  print(d)
# Va rog sa corectati astfel incat outputul programului sa fie cel de mai jos:
# /usr/bin/python3.5
# /home/pandelegeorge/projects/telacad/sedinta5/testwhile.py
# 9
# 8
# 7
# 6
# 4
# 3
# 2
# 1
# 0

d = 10
while d:
    d = d - 1
    if d == 5:
        continue
    print(d)
