import sys

# print(sys.argv)
# print(sys.modules)

sys.stdout = open(file="fisier_consola.txt", mode="wt")
print("HELLO WORLD")
print("TELECOM ACADEMY2")
sys.stdout.close()
print("HY THERE")
