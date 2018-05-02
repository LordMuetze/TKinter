def aufSiegPruefen(self):
    self.d1_boolliste = []
    self.d2_boolliste = []

    for i in range(1, self.format+1):
        self.z_boolliste = []
        self.s_boolliste = []

        for x in range(1, self.format+1):
            self.z_feld = "f_"+str(x) + "_" + str(i)
            self.s_feld = "f_"+str(i) + "_" + str(x)
            self.z_bool = z_feld in self.aktuellerSpieler.gibFelderListe()
            self.s_bool = s_feld in self.aktuellerSpieler.gibFelderListe()
            self.z_boolliste.append(z_bool)
            self.s_boolliste.append(s_bool)
            if x == i:
                self.d1_boolliste.append(z_bool)
            if x + i == self.format + 1:
                self.d2_boolliste.append(z_bool)
                self.d2_boolliste.append(s_bool)

        if False not in self.z_boolliste or False not in self.s_boolliste:
            return True
    if False not in self.d1_boolliste or False not in self.d2_boolliste:
        return True
    else:
        return False