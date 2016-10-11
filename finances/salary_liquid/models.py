from django.db import models

class desconto(object):
	def __init__(self, sal):
		self.vt = sal * 0.06
		self.va = sal * 0.06
		self.inss = sal * 0.11

	def total_desconto(self):
		return self.vt + self.va + self.inss

class salario(object):
	def __init__(self, sal):
		self.bruto = sal
		self.desconto = desconto(sal)
		self.liquido = sal - self.desconto.total_desconto()
