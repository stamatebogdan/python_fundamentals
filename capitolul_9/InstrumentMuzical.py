class InstrumentMuzical:

    def __init__(self, material):
        self.material = material

    def scoate_sunet(self):
        print("Sunet general de instrument muzical")

    def canta_concert(self):
        raise NotImplementedError("Metoda NU a fost inca definitva/suprascrisa.")

class Chitara(InstrumentMuzical):

    def __init__(self, material, nr_corzi):
        super().__init__(material)
        self.nr_corzi = nr_corzi

    def plange_chitara(self):
        print("Plange chitara mea")

    def canta_concert(self):
        print("Chitara mea canta in concert diseara")

class Pian(InstrumentMuzical):

    def __init__(self, material, nr_clape):
        super().__init__(material)
        self.nr_clape = nr_clape

    def scoate_sunet(self):
        print(f"Sunet scos de un pian facut din {self.material} cu {self.nr_clape} clape.")

    def canta_concert(self):
        print("Pianul meu este folosit in concert la opera")

if __name__ == "__main__":
    i1 = InstrumentMuzical("marmura")
    c1 = Chitara("lemn", 5)
    p1 = Pian("marmura", 64)
    p1.scoate_sunet()
    p1.canta_concert()
    # print(c1.nr_corzi)
    # print(c1.material)
    c1.scoate_sunet()
    c1.canta_concert()
    # print(i1.material)
    # i1.scoate_sunet()
    # c1.plange_chitara()
    # i1.plange_chitara()
    # print(i1.nr_corzi)