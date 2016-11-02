from django import forms
from django.contrib.auth.models import User

class UserProfileForm(forms.Form):

	username = forms.CharField(required=True)
	image = forms.ImageField()

	def is_valid(self):
		valid = True
		if not super(UserProfileForm, self).is_valid():
			self.adiciona_erro('Dados do usuário invalido')
			valid = False
		if User.objects.filter(email=self.username) :
			self.adiciona_erro('Usuário já cadastrado')
			valid = False

		return valid

	def adiciona_erro(self, message):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(message)
