class Dreptunghi:
    def __init__(self, lungime, latime):
        self.lungime = lungime
        self.latime = latime

    def aria(self):
        return self.lungime * self.latime

    def perimetru(self):
        return 2 * self.lungime + 2 * self.latime


# Folosind super, se apeleaza constructorul din Dreptunghi
class Patrat(Dreptunghi):
    def __init__(selfself, lungime):
        super().__init__(lungime, lungime)


# Folosind super, se apeleaza aria din Dreptunghi
class Cub(Patrat):
    def volum(self):
        return super().aria() * self.lungime


patrat = Patrat(4)

print("Patrat cu latura de: " + str(patrat.lungime) + " , " + str(patrat.latime))

cub = Cub(3)

print("Volumul cubului " + str(cub.volum()))
