my_dict=dict()
my_dict={}

# curs=["Python Fundamentals", "vineri", 6, "Alex", 10, 12]
curs ={
    "nume": "Python Fundamentals",
    "zi_desfasurare": "vineri",
    "sala": 6,
    "instructor": "Alex",
    "data_incepere": 10,
    "numar_participanti": 12
}

# print(curs["instructor"])
# print(curs["nume"])
# print(curs["data_incepere"])
# # print(curs["ora_incepere"])
#
# curs["examen"] = True
# print(curs)
# curs.update({"data_incepere": 17,
#              "reguli_promovare": True})
# print(curs)

# if "data_incepere" in curs:
#     print("Cursul incepe la data de: " + str(curs["data_incepere"]))
#
# print(curs.get("data_incepere"))
# print(curs.get("ora_incepere"))
# print(curs.get("ora_incepere", 22))

# for key in curs.keys():
#     print(key, end=" ")
# print()
#
# for value in curs.values():
#     print(value, end=" ")
# print()
#
# for key, values in curs.items():
#     print(f"Cheia: {key}, Valoarea: {values}")
# print()

curs_javascript={"nume":"JavaScript Fundamentals",
                 "zi_desfasurare": ["joi", "vineri", "sambata"],
                 "instructor": {
                     "nume": "Bogdan",
                     "experienta": 3
                 },
                 "sala": 7}
print(curs_javascript.get("nume"))
print(curs_javascript.get("instructor"))
print(curs_javascript.get("instructor").get("nume"))
print(curs_javascript["instructor"]["nume"])