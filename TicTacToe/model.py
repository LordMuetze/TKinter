from Person import *


class Feld:
    def __init__(self, nummer, bezeichner):
        self.bezeichner = bezeichner
        self.nummer = nummer
        self.zustand = 0
    def gibBezeichner(self):
        return self.bezeichner
    def gibNummer(self):
        return self.nummer



class Spielfeld:


    def __init__(self, format=3):
        self.felderBelegung = []
        self.format = format
        for i in range (1, format+1):
            for x in range (1, format+1):
                exec("self.feld_" + str(i)+'_'+str(x) + " = Feld(str(i*format+x), str(i)+'_'+str(x))")
                self.felderBelegung.append(0)


        self.spieler1 = Person("spieler1", "x")
        self.spieler2 = Person("spieler2", "o")


    def zeichenSetzen(self, spieler, feld):
        spieler.felderListeErgaenzen(feld)
        self.felderBelegung[feld] = spieler.gibZeichen()
        return True

    def aufSiegPruefen(self, spieler):
        self.d1_boolliste = []
        self.d2_boolliste = []

        for i in range(1,self.format+1):
            self.z_boolliste = []
            self.s_boolliste = []

            for x in range (1,self.format+1):
                self.z_feld = str(x) + "_" + str(i)
                self.s_feld = str(i) + "_" + str(x)
                self.z_bool = z_feld in spieler.felderListe
                self.s_bool = s_feld in spieler.felderListe
                self.z_boolliste.append(z_bool)
                self.s_boolliste.append(s_bool)
                if x==i:
                    self.d1_boolliste.append(z_bool)
                if x+i == self.format+1:
                    self.d2_boolliste.append(z_bool)
                    self.d2_boolliste.append(s_bool)

            if False not in z_boolliste or False not in s_boolliste:
                return True
        if False not in d1_boolliste or False not in d2_boolliste:
            return True
        else:
            return False