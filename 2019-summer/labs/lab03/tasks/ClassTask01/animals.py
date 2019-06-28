# -*- coding: utf-8 -*-

"""
Author: Cebere Tudor
Course: Python Programming @ ccna.ro
"""

class BasicLivingCreature:
	
	no_of_creatures = 0

	def __init__(self):
		BasicLivingCreature.no_of_creatures += 1

class Mamal(BasicLivingCreature):
	def is_mamal(self):
		return True

class Om(Mamal):
	def is_smecher(self):
		return True

class Tiger(Mamal):
	def is_tiger(self):
		return True

	def be_awesome(self, enemy):
		if issubclass(type(enemy), Om):
			print("Delicios!")

		elif issubclass(type(enemy), Arachnide):
			print("BIG ROAR!")

		elif issubclass(type(enemy), Tiger):
			print("Hello, awesome friend")

		else:
			print("Ignore!")

class BabyTiger(Tiger):
	def is_baby_tiger(self):
		return True

	def save(self, enemy):
		if(type(enemy) == Arachnide):
			print("ROAR!")
		
		if(type(enemy) == OmulPaianjen):
			print("Call Mary Jane!")

		if(type(enemy) == BabyTiger):
			print("For those about to roar, we salute you!")

		if(type(enemy) == Om):
			print("Delicios.")

		if(type(enemy) == Tiger):
			print("Miau.")

class Arachnide(BasicLivingCreature):
	def is_smecher(self):
		return False

	def is_scary(self):
		return True

class OmulPaianjen(Om, Arachnide):
	def kiss_mary_jane(self):
		return True

omida = BasicLivingCreature()
panda = Mamal()
tudor = Tiger()
dorin = BabyTiger()
rughinis = Om()
laur = OmulPaianjen()

dorin.save(laur)
tudor.be_awesome(OmulPaianjen)
# try:
# 	print(rughinis.kiss_mary_jane())
# except:
# 	print("Rughinis nu e Spider Man!")

# print("Laur este smecher: " + str(laur.is_smecher()))

# print("Dorin este BabyTiger: " + str(dorin.is_baby_tiger()))
