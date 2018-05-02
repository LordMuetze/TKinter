class Person:

    def __init__(self, zeichen):
        self.zeichen = zeichen
        self.felderListe = []


    def felderListeErgaenzen(self, feld):
        self.felderListe.append(feld)

    def gibFelderListe(self):
        return self.felderListe

    def felderListeLeeren(self):
        self.felderListe = []


    def gibZeichen(self):
        return self.zeichen
    def setzeZeichen(self, z):
        self.zeichen = z