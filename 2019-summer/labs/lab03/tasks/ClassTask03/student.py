# -*- coding: utf-8 -*-

"""
Author: Dorin Geman
Course: Python Programming @ ccna.ro
"""

class Student:

	species = 'human'

	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.is_tired = True

	def go_to_holiday(self):
		self.is_tired = False

