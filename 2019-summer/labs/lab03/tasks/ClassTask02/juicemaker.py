# -*- coding: utf-8 -*-

"""
Author: Cebere Tudor
Course: Python Programming @ ccna.ro
"""

class Fruct:
	def __init__(self, cantitate):
		self.cantitate = cantitate
		print(self.cantitate)

	def shake(self):
		pass

class Mar(Fruct):
	def __init__(self, cantitate):
		super().__init__(cantitate)
		
	def shake(self):
		print("Marul este in blender.")

class Portocala(Fruct):
	def __init__(self, cantitate):
		super().__init__(cantitate)

	def shake(self):
		print("Portocala este in blender.")

class Ananas(Frunct):
	def __init__(self, cantitate):
		super().__init__(cantitate)

	def shake(self):
		print("Ananas-ul este in blender.")

class Blender:
	def __init__(self, consumabile, recipes):
		pass

	def asteapta_comanda(self, comanda):
		pass

	def list(self):
		pass

	def status(self):
		pass

	def make(self, reteta_de_facut):
		pass	
