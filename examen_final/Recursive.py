# 2.Creați un program care să folosească recursivitate pentru a returna un dicționar.
# a) Dicționarul va avea: keys – “director/nume fișier” și values – o listă al cărei element este un
# rând din fișier
# b) Dicționarul va avea: keys – “director/nume fișier” și values – o listă al cărei element este un
# rând din fișier doar dacă fișierul nu conține cuvântul Stop.

dictionarA={}
dictionarB={}

lista2 = list()
lista3 = list()
lista4 = list()
lista5 = list()
lista6 = list()

if __name__ == "__main__":
    fisier2 = open("1/2/test2.txt", mode="rt", encoding="utf-8")
    for i in fisier2:
        lista2.append(i)
    fisier2.close()

    fisier3 = open("1/3/test3.txt", mode="rt", encoding="utf-8")
    for i in fisier3:
        lista3.append(i)
    fisier3.close()

    fisier4 = open("1/4/test4.txt", mode="rt", encoding="utf-8")
    for i in fisier4:
        lista4.append(i)
    fisier4.close()

    fisier5 = open("1/2/5/test5.txt", mode="rt")
    for i in fisier5:
        lista5.append(i)
    fisier5.close()

    fisier6 = open("1/2/6/test6.txt", mode="rt", encoding="utf-8")
    for i in fisier6:
        lista6.append(i)
    fisier6.close()


    dictionarA["1/2/test2.txt"] = lista2
    dictionarA["1/3/test3.txt"] = lista3
    dictionarA["1/4/test4.txt"] = lista4
    dictionarA["1/2/5/test5.txt"] = lista5
    dictionarA["1/2/6/test6.txt"] = lista6

    lista_stop=list()
    lista_generala=[lista2, lista3, lista4, lista5, lista6]

    for a in range(0,len(lista_generala)):
        for b in lista_generala[a]:
            if b == 'Stop':
                lista_generala.pop(a)


    for i,j in dictionarA.items():
        if j != lista3:
            dictionarB[i]=j


    print("Dictionarul punctului a) este: " + str(dictionarA))
    print("Dictionarul punctului b) este: " + str(dictionarB))

















    # lungime_liste["lista2"] = len(lista2)
    # lungime_liste["lista3"] = len(lista3)
    # lungime_liste["lista4"] = len(lista4)
    # lungime_liste["lista5"] = len(lista5)
    # lungime_liste["lista6"] = len(lista6)
    #
    # for i in lungime_liste.values():
    #     if i < 4:
    #         break
    #         # lungime_liste.pop('{}'.format(lungime_liste.keys()))
    #
    # print(lungime_liste)
    #         # for j in lungime_liste.keys():
    #         #  if lungime_liste.keys() == 'lista2':
    #         #     dictionarB["1/{}/test{}.txt".format(2,2)] = lista2
    #         #  elif lungime_liste.keys() == 'lista3':
    #         #     dictionarB["1/{}/test{}.txt".format(3, 3)] = lista3
    #         #  elif lungime_liste.keys() == 'lista4':
    #         #     dictionarB["1/{}/test{}.txt".format(4, 4)] = lista4
    #         #  elif lungime_liste.keys() == 'lista5':
    #         #     dictionarB["1/2/{}/test{}.txt".format(5, 5)] = lista5
    #         #  elif lungime_liste.keys() == 'lista6':
    #         #     dictionarB["1/2/{}/test{}.txt".format(6, 6)] = lista6
    #












