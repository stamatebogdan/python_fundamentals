# 1. Câte din cuvintele de mai jos sunt anagrame ale cuvântului "hkfidipwlabsellcegkjebqdbxbyqzopnqascthnesgnwfmdxz" ?

anagrama = "hkfidipwlabsellcegkjebqdbxbyqzopnqascthnesgnwfmdxz"
test1 = "qqlomsztslfnldaskgndebbigczcbhhapwqxkeypjiefenbdxw"
test2 = "odesfbkylxsqkhaztehgaljminwgbcnbcweidlzpqdfspbenqx"
test3 = "mfuznfhbfchljypjbqvzvchkifhcbjcblnbrmbtawkjgwgzcwu"
test4 = "nzddsmiypqesslixmytygaqlzpaloedihgfequtqxmvcoxaopx"
test5 = "wubbckhmjbcupmjczazgvfhnffbwljbickhwrqgnbyvhjzfctl"
test6 = "sgqqchelpqmeibainencnddefylsxhbflwdtsowjgxakpzbzbk"
test7 = "wbzwjvbubchglbhhyfzcqfvjfazficcjbngmprkhlcbmwtunjk"
test8 = "ppsqosoamextpmihxgseaixqfiaegqlzcluvdodmtyzxnylqyd"
test9 = "mxsnmdqhfeqtogstydegxyclpyoeiislpalqaqzidmzopvaxux"
d = dict()
t=dict()
numar = 0

for i in range(len(anagrama)):
    for j in anagrama:
        if anagrama[i] == j:
            numar = numar + 1

    d[f"{anagrama[i]}"] = numar
    numar =0


def este_anagrama(testul, dictionar):
    increment = 0

    for i in range(len(testul)):
        for j in testul:
            if testul[i] == j:
                increment = increment + 1

        t[f"{testul[i]}"] = increment
        increment = 0

    if t == dictionar:
        print("Cuvantul este anagrama")
    else:
        print("Cuvantul nu este anagrama")



print(este_anagrama(test9,d))