#!/usr/bin/env python

class employee:

	def __init__(self, name):
		self.name = name

	def getEmpDetails(self):
		print ("Employee : " + self.name)


Emp1 = employee("Kaps")
Emp2 = employee("Kat")

Emp1.getEmpDetails()
Emp2.getEmpDetails()
