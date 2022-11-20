class Pisica:

    rasa = "birmaneza"

    def __init__(self, nume, culoare, greutate, varsta=5, adresa=""):
        self.nume = nume
        self.culoare = culoare
        self.greutate = greutate
        self.__varsta = varsta
        self._adresa = adresa

    def get_varsta(self):
        return self.__varsta

    def set_varsta(self, new_varsta):
        self.__varsta = new_varsta

    def spune_miau(self):
        print(f"MEOW MEOW! Ma numesc {self.nume}")

    def se_joaca(self, partener_joaca):
        print(f"Pisica {self.nume} se joaca cu {partener_joaca.nume}")

p1 = Pisica("Leia", "gri", 6.5, 6)
p2 = Pisica("Sheba", "neagra", 6.7)
print(Pisica.rasa)
print(p1.rasa)

# p1.se_joaca(p2)
# p2.se_joaca(p1)

# p1.spune_miau()
# p2.spune_miau()

# p1._adresa="Apaca"
# print(p1._adresa)

# p2.set_varsta(3)#
# print(p1.get_varsta())
# print(p2.get_varsta())
# print(p1.__varsta)

# p1.nume = "Nume nou"
# p2.culoare = "albastra"
# p2.greutate = 6.3
#
# print(p1.nume)
# print(p2.culoare)
# print(p2.greutate)
# print(p1.varsta)
