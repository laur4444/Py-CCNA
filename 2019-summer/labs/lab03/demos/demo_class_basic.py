# -*- coding: utf-8 -*-

"""
Author: Dorin Geman
Course: Python Programming @ ccna.ro
"""

#1
class Student:

	species = 'human'

	def __init__(self, name, age = 100):
		self.name = name
		self.age = age
		self.species = 'robot'
		self.is_tired = True

	#2
	def speak(self):
		print('Hello, I am ' + self.name)

	#3
	def go_to_holiday(self):
		self.is_tired = False

print(Student.species)
a = Student('Alex', 10)
print(a.name +  ', the ' + a.species + ', has ' + str(a.age))
a.speak()

b = Student('Vlad', 20)
print(b.name +  ', the ' + b.species + ', has ' + str(b.age))
b.speak

print(b.is_tired)
b.go_to_holiday()
print(b.is_tired)
