from Person import *
from Feld import *


class Spielfeld:
	
	
	def __init__(self, format):
		
		self.format = format
		self.diagonale_1 = []
		self.diagonale_2 = []
		self.spieler_1 = Person("X")
		self.spieler_2 = Person("O")
		self.spielerliste = [self.spieler_2, self.spieler_1]
		self.aktuellerSpieler = self.spieler_1
		
#---------------------------------------------Spielfeld erstellen---------------------------------------------
#--------------------------------------------------------------------------------------------------------------
		for x in range (1, self.format+1):
			for y in range (1, self.format+1):
				exec("self.zeile_" + str(y) + " = []")
			exec("self.spalte_" + str(x) + " = []")
		
		for x in range (1, self.format+1):
			for y in range (1, self.format+1):
				exec("self.feld_" + str(x) + "_" + str(y)  + " = Feld("+str(x)+","+str(y)+", self)")
				#print("self.feld_" + str(x) + "_" + str(y) + " = Feld("+str(x)+","+str(y)+", self)")
				exec("self.zeile_" + str(y) + ".append(self.feld_" + str(x) + "_" + str(y) + ")")
				#print("self.zeile_" + str(y) + ".append(self.feld_" + str(x) + "_" + str(y) + ")")
				exec("self.spalte_" + str(x) + ".append(self.feld_" + str(x) + "_" + str(y) + ")")
				#print("self.spalte_" + str(x) + ".append(self.feld_" + str(x) + "_" + str(y) + ")")
				if x == y:
					exec("self.diagonale_1.append(self.feld_" + str(x) + "_" + str(y) + ")")
					print("self.diagonale_1.append(self.feld_" + str(x) + "_" + str(y) + ")")
				if x+y == self.format+1:
					exec("self.diagonale_2.append(self.feld_" + str(x) + "_" + str(y) + ")")
					print("self.diagonale_2.append(self.feld_" + str(x) + "_" + str(y) + ")")
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
	def gibFormat(self):
		return self.format
	
	def setzen(self, feld):
		if feld.gibZustand() == 0:
			feld.setzeZustand(self.aktuellerSpieler.gibZeichen())
			self.aktuellerSpieler.felderListeErgaenzen(feld)
			sieg = self.sieg()
			if sieg:
				return True
			self.spielerliste.append(self.aktuellerSpieler)
			self.aktuellerSpieler = self.spielerliste.pop(0)
			return False
	
	def sieg(self):
		if all(elem in self.aktuellerSpieler.gibFelderListe() for elem in self.diagonale_1):
			return True
		if all(elem in self.aktuellerSpieler.gibFelderListe() for elem in self.diagonale_2):
			return True
		
		for x in range(1, self.format+1):
			for y in range(1, self.format+1):
				print("bool = all(elem in self.aktuellerSpieler.gibFelderListe() for elem in self.zeile_" + str(y) + ")")
				exec("bool = all(elem in self.aktuellerSpieler.gibFelderListe() for elem in self.zeile_" + str(y) + ")")
				if bool:
					return True
			print("bool = all(elem in self.aktuellerSpieler.gibFelderListe() for elem in self.spalte_" + str(x) + ")")
			exec("bool = all(elem in self.aktuellerSpieler.gibFelderListe() for elem in self.spalte_" + str(x) + ")")
			if bool:
				return True
			
		return False