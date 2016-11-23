from impostos import ISS, ICMS, ICPP, IKCV

class Calculador_de_imposto(object):

	def realiza_calculo(self, orcamento, strategy):
		imposto_caculado = strategy.calcula(orcamento)
		print(imposto_caculado)


if __name__ == "__main__":

	from orcamento import Orcamento, Item

	orcamento = Orcamento()

	orcamento.adiciona_item(Item('Item a', 100.0))
	orcamento.adiciona_item(Item('Item b', 50.0))
	orcamento.adiciona_item(Item('Item c', 400.0))


	calculo = Calculador_de_imposto()
	calculo.realiza_calculo(orcamento, ISS())
	calculo.realiza_calculo(orcamento, ICMS())

	print "ICPP IKCV"
	calculo.realiza_calculo(orcamento, ICPP())
	calculo.realiza_calculo(orcamento, IKCV())