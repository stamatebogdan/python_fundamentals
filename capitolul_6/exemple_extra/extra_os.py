import os

print("Directorul in care ne aflam acum este: ")

for intrare in os.listdir():
    print(intrare)

print("Cream directorul test in directorul curent: ")

os.mkdir("test")
for intrare in os.listdir():
    print(intrare)

print("Stergem directorul anterior creat")
os.rmdir("test")

for intrare in os.listdir():
    print(intrare)