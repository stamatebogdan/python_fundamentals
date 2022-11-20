# 1. Creați o clasă Melodii care să aibă un atribut nume_melodii. Atributul va primi ca valoare o listă
# de melodii la inițializarea clasei. Creați o metodă denumită Amestec care să returneze la apelare
# melodiile amestecate folosind shuffle, ce aparține de modulul random.

import random

class Melodii():

    def __init__(self, nume_melodii):
        self.nume_melodii = nume_melodii

    def amestec(self):
        random.shuffle(self.nume_melodii)
        print(self.nume_melodii)

lista_melodii = ["I love you", "Gangsta paradise", "Bailando", "Single ladies", "Macarena", "Coco Jambo"]

if __name__ == "__main__":
    melodiile_disponibile = Melodii(lista_melodii)
    melodiile_disponibile.amestec()

