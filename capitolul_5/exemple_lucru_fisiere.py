# my_file = open(file="fisier_nou.txt", mode="wt", encoding="utf-8")
# my_file.write("Primul fisier scris in Python. \n")
# my_file.write("Continuarea textului din fisierul meu. \n")
# my_file.write("Text pe a doua linie din fisierul meu. \n")
# my_file.write("Ultima linie din fisierul meu.")
# my_file.close()

# my_file=open(file="fisier_nou.txt", mode="rt", encoding="utf-8")
# print(my_file.read(6))
# my_file.seek(0)
# print(my_file.readline())
# my_file.seek(3)
# print(my_file.readlines())
# my_file.close()

# my_file=open("fisier_nou.txt", "a")
# my_file.write("\no noua linie adaugata in fisierul meu.\n")
# my_file.writelines(["linie noua la finalul fisierului. \n", ":)\n", ":(\n"])
# my_file.close()

with open("alt_fisier.txt", "wt") as my_file:
    my_file.write("Am creat un nou fisier cu ajutorul Context Manager")

my_file.write("ABC")

