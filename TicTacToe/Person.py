class Person:
    def __init__(self, name, zeichen):
        self.name = name
        self.zeichen = zeichen
        self.felderListe = []
    def felderListeErgaenzen(self, feld):
        self.felderListe.append(feld)
    def gibFelderList(self):
        return self.felderListe
    def gibName(self):
        return self.name
    def gibZeichen(self):
        return self.zeichen
