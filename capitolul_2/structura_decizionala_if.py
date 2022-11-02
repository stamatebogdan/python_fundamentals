var = 100

#if var > 50:
#    print("HELLO WORLD")
#    print("SECOND LINE")
#print ("ANOTHER WORLD")

# if "telacad" : # <=> bool("telacad")
#     print("Curs de python luni seara")
#
# if 1:  # <=> boool(1)
#     print("De asemenea adevarat")

# var = 26
# if var > 101:
#     print(f"{var} este mai mare decat 101.")
# else:
#     print(f"{var} nu este mai mare decat 101.")

# var = 26
# if var == 101:
#     print("Valoarea este chiar 101.")
# elif var < 25:
#     print("Valoarea este mai mica de 25")
# elif var < 50:
#     print("Valoarea este mai mica de 50")
# else:
#     print("Valoarea NU  se incadreaza in niciuna din conditiile prezentate")

"""
Cititi o valoare numerica de la tastatura, corespunzatoare inaltimii in centrimetrii
- daca valoarea este 174 - afisati: "Sunteti de inaltime medie in Romania"
- daca valoarea este mai mica de 160 - afisati: "poate sunteti in crestere..."
- daca valoarea este mai mare de 190 - afisati: "poate sunteti suedezi..."
Restul situatiilor afisam - "Sunteti deosebiti."
"""
inaltime = int(input("Va rugam sa introduceti ce inaltime aveti, in cm: "))
# if inaltime == 174:
#     print("Sunteti de inaltime medie in Romania")
# elif inaltime < 160:
#     print("poate sunteti in crestere...")
# elif inaltime > 190:
#     print("poate sunteti suedezi...")
# else:
#     print("Sunteti deosebiti.")

if inaltime == 174:
    print("Sunteti de inaltime medie in Romania")
else:
    if inaltime < 160:
        print("poate sunteti in crestere...")
    else:
        if inaltime > 190:
            print("poate sunteti suedezi...")
        else:
            print("Sunteti deosebiti.")