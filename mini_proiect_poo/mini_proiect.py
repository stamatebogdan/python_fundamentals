from datetime import datetime, timedelta

class Persoana:

    def __init__(self, nume, prenume, varsta):
        self.nume = nume
        self.prenume = prenume
        self.varsta = varsta

class Membru(Persoana):

    def __init__(self, nume, prenume, varsta, id_membru, carti_imprumutate):
        super().__init__(nume, prenume, varsta)
        self.id_membru = id_membru
        self.carti_imprumutate = carti_imprumutate

    def imprumuta_carte(self, carte_fizica):
        self.carti_imprumutate.append(carte_fizica)
        carte_fizica.data_retur += timedelta(weeks = 4)

    def returnare_carte(self, carte_fizica):
        self.carti_imprumutate.remove(carte_fizica)

class Bibliotecar(Persoana):

    def __init__(self, nume, prenume, varsta, data_angajarii):
        super().__init__(nume, prenume, varsta)
        self.data_angajarii = data_angajarii

    def verifica_disponibilitate(self, carte_fizica):
        if carte_fizica == 'neimprumutata':
            print("Cartea " + carte_fizica.autor + ". " + carte_fizica.titlu + " este disponibila")
            return True
        else:
            print("Cartea " + carte_fizica.autor + ". " + carte_fizica.titlu + " NU este disponibila")
            return False



class Carte:

    def __init__(self, titlu, autor):
        self.titlu = titlu
        self.autor = autor

class CarteFizica(Carte):

    def __init__(self, titlu, autor,locatie, status, editura):
        super().__init__(titlu, autor)
        self.locatie = locatie
        self.status = status
        self.editura = editura
        self.data_retur = datetime.now()

class Notificare:

    def __init__(self, adresa_from, adresa_to, subiect, text_email):
        self.adresa_from = adresa_from
        self.adresa_to = adresa_to
        self.subiect = subiect
        self.text_email = text_email

    def trimite_notificare(self):
        import smtplib

        mesaj =""" Subiect: %s
                    Mesaj: %s
            """ %(self.subiect, self.text_email)
        server = smtplib.SMTP("localhost", 5555)
        print("Se va trimite un email pentru ca data de retur a fost depasita")
        server.sendmail(self.adresa_from, self.adresa_to, mesaj)
        server.quit()


if __name__ == "__main__":
    carte_fizica = CarteFizica("Luceafarul","Mihai Eminescu", "Raft 2", "neimprumutata", "Telacad")
    membru = Membru("Popescu", "Ion", "34", "123", [])
    bibliotecar = Bibliotecar("Ionescu", "Ioana", "24", datetime(2018, 12, 2))

    if bibliotecar.verifica_disponibilitate(carte_fizica):
        membru.imprumuta_carte(carte_fizica)

        if carte_fizica.data_retur > datetime.now() - timedelta(weeks =5):
            notificare = Notificare("local@telacad.ro", "dest@telacad.ro", "Alerta returnare carte",
                                    "Va rugam sa returnati cartea: " + carte_fizica.titlu + ", "
                                    + carte_fizica.autor )
            notificare.trimite_notificare()
