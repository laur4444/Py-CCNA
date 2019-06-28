# -*- coding: utf-8 -*-

"""
Author: Dorin Geman
Course: Python Programming @ ccna.ro
"""

class Car:

	def __init__(self):
		pass

	#2
	def sound(self):
		pass

class Audi(Car):

	def __init__(self):
		self.model = 'Audi'
		self.price = 10500
		self.engine = 'diesel'

	#2
	def sound(self):
		return 'roar'

class Dacia(Car):

	def __init__(self):
		self.model = 'Dacia'
		self.price = 1200
		self.engine = 'diesel'

	#2
	def sound(self):
		return 'miau'

audi = Audi()
print(audi.model + ' sounds like ' + audi.sound())
dacia = Dacia()
print(dacia.model + ' sounds like ' + dacia.sound())
print(str(audi))
