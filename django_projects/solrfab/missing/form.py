# -*- encoding:UTF-8 -*-
from django import forms


class MissingForm(forms.Form):

	name = forms.CharField(required=True)
	age = forms.CharField(required=True)
	hair_color = forms.CharField(required=True)
	eye_color = forms.CharField(required=True)
	height = forms.CharField(required=True)
	skin_color = forms.CharField(required=True)
	approximate_weight = forms.CharField(required=False)
	street = forms.CharField(required=False)
	city = forms.CharField(required=False)
	state = forms.CharField(required=False)
	country = forms.CharField(required=False)
	district = forms.CharField(required=False)
	approximate_number = forms.CharField(required=False)
	gender = forms.CharField(required=True)
	cloutes = forms.CharField(required=False)
	reason = forms.CharField(required=False)
	image = forms.ImageField(required=False)

	def is_valid(self):
		valid = True
		if not super(MissingForm, self).is_valid():
			self.adiciona_erro('Preencha corretamente os dados do desaparecido há informações obrigatorias')
			valid = False

		return valid

	def adiciona_erro(self, message):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(message)
