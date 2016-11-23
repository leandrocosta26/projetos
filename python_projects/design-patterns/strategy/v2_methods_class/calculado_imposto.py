from impostos import ISS, ICMS

class Calculador_de_imposto(object):

	def realiza_calculo(self, orcamento, calcula_imposto):
		imposto_caculado = calcula_imposto(orcamento)
		print(imposto_caculado)


if __name__ == "__main__":

	from orcamento import Orcamento

	orcamento = Orcamento(500)
	calculo = Calculador_de_imposto()
	calculo.realiza_calculo(orcamento, ISS.calcula)
	calculo.realiza_calculo(orcamento, ICMS.calcula)