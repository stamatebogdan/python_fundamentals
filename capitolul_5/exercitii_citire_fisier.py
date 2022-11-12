g = open("test_citire.txt", mode="rt", encoding="utf-8") # deschidem fișierul în modul citire
print(g.read(10)) # citim primele 10 caractere din fișier
print(g.read()) # citim restul fișierului.
print(g.read()) # pentru că întreg conținutul fișierului a fost citit la instrucțiunea anterioară, această citire nu întoarce nimic
g.seek(0) # seek este folosit pentru a reseta locația de unde se face citirea. g.seek(0) restaurează citirea de la poziția 0 (începutul fișierului)
print(g.readline()) # citește o linie din fișier
print(g.readline()) # citește o nouă linie din fișier
print(g.readlines()) # citește restul liniilor din fișier, rezultatul este o listă de elemente de tip string, fiecare element corespunde unei linii din fișier
g.close() # închidem fișierul atunci când am terminat procesarea