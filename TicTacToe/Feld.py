class Feld:

    def __init__(self, x, y, nummer):
        self.x = x
        self.y = y
        self.nummer = nummer
        self.zustand = 0


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