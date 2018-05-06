class Feld:

    def __init__(self, x, y, master):
        self.x = x
        self.y = y
        self.koordinaten = [x,y]
        self.master = master
        self.nummer = (self.y-1) * self.master.gibFormat() + self.x
        self.zustand = 0
        #self.master.spielfeldlisteErgaenzen(self)


    def setzeZustand(self,z):
        self.zustand = z
    def gibZustand(self):
        return self.zustand


    def gibNummer(self):
        return self.nummer
    def setzeNummer(self,n):
        self.nummer = n


    def gibBezeichner(self):
        return self.bezeichner
    def setzeBezeichner(self,b):
        self.bezeichner = b


    def gibX(self):
        return self.x
    def setzeX(self, x):
        self.x = x


    def gibY(self):
        return self.y
    def setzeY(self, y):
        self.y = y
        
    
    def gibKoordinaten(self):
        return self.koordinaten