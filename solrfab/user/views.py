from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.models import User
from user.models import Profiler
from user.form import ProfileForm
import pdb

class UserView(View):

	def post(self, request):

		form  = ProfileForm(request.POST, request.FILES)

		if not form.is_valid():
			return render(request, 'user.html', { 'form' : form })

		data = form.data
		user = User(email=data['email'], password=data['password'])
		profile = Profiler(name=data['username'],image=data[''])
		profile.image = form.cleaned_data['image']

		profile.save()

		return redirect(index)



	def get(self, request):
		return render(request, 'user.html')
