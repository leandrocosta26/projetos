# -*- coding: Utf-8 -*-

from desconto import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhetos_reais, Sem_desconto

class Calculador_de_desconto(object):

	def calcula(self, orcamento):
		
		desconto = Desconto_por_mais_de_quinhetos_reais(Desconto_por_mais_de_quinhetos_reais(Sem_desconto())).calcula(orcamento)

		return desconto
		



if __name__ == "__main__":

	from orcamento import Orcamento, Item

	orcamento = Orcamento()

	orcamento.adiciona_item(Item('Item a', 100.0))
	orcamento.adiciona_item(Item('Item b', 50.0))
	orcamento.adiciona_item(Item('Item c', 400.0))

	desconto = Calculador_de_desconto().calcula(orcamento) 
	print('Desconto calculado : %s' % (desconto))