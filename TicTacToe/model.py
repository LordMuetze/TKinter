from Person import *
from Feld import *
#--------------------------------------------------------------------------------


class Spielfeld:
	def __init__(self, format = 3):
		self.format = format
		self.spielfeldliste = []
		self.zustandsliste = []
		self.spieler1 = Person("X")
		self.spieler2 = Person("O")
		self.spielerliste = [self.spieler2, self.spieler1]
		self.aktuellerspieler = self.spieler1
		
		for x in range(1, self.format+1):
			for y in range(1, self.format+1):
				exec("global f_"+str(x) + "_" + str(y)+";f_"+str(x) + "_" + str(y) + "= Feld("+str(x) + "," + str(y) + ",self)")
				exec("self.spielfeldliste.append("+str(x) + "_" + str(y)+")")
				self.zustandsliste.append(0)
				print(self.spielfeldliste)
				
	
	def spielfeldlisteErgaenzen(self, feld):
		self.spielfeldliste.append(feld)
	
	def gibSpielfeldliste(self):
		return self.spielfeldliste

	
	def gibZustandsliste(self):
		return self.zustandsliste
	
	def gibFormat(self):
		return self.format
	
	
	def setzen(self, feld):
		if self.zustandsliste[feld] == 0:
			self.aktuellerspieler.felderListeErgaenzen(feld)
			#feld.setzeZustand(self.aktuellerspieler.gibZeichen())
			self.zustandsliste[feld] = self.aktuellerspieler.gibZeichen()
			self.siegpruefen()
			self.spielerliste.append(self.aktuellerspieler)
			self.aktuellerspieler = self.spielerliste.pop(0)
		
	
	def siegpruefen(self):
		self.d1_boolliste = []
		self.d2_boolliste = []
		
		for i in range(1, self.format + 1):
			self.z_boolliste = []
			self.s_boolliste = []
			
			for x in range(1, self.format + 1):
				self.z_feld = str(x) + "_" + str(i)
				self.s_feld = str(i) + "_" + str(x)
				self.z_bool = self.z_feld in self.aktuellerspieler.gibFelderListe()
				self.s_bool = self.s_feld in self.aktuellerspieler.gibFelderListe()
				self.z_boolliste.append(self.z_bool)
				self.s_boolliste.append(self.s_bool)
				if x == i:
					self.d1_boolliste.append(self.z_bool)
				if x + i == self.format + 1:
					self.d2_boolliste.append(self.z_bool)
					self.d2_boolliste.append(self.s_bool)
			
			if False not in self.z_boolliste or False not in self.s_boolliste:
				return True
		if False not in self.d1_boolliste or False not in self.d2_boolliste:
			return True
		else:
			return False