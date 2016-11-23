from django.views.generic.base import View
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from missing.models import Missing
from missing.form import MissingForm
from user.models import UserProfiler
#import pdb

def index(request):
	missings = Missing.objects.all()
	return render(request,'index.html', {"missings" : missings })

def information(request, id_missing):
	missing = Missing.objects.get(id=id_missing)
	return render(request, 'information.html', { 'missing' : missing })

class MissingRegistrationView(View):

	def post(self, request):
#		pdb.set_trace()
		form  = MissingForm(request.POST, request.FILES)

		if form.is_valid():

			data = form.data

			user = UserProfiler.objects.get(id=1)

			missing = Missing(name = data['name'],age = int(data['age']),hair_color = data['hair_color'],eye_color = data['eye_color'],height = data['height'],skin_color = data['skin_color'], approximate_weight = float(data['approximate_weight']), street = data['street'], city = data['city'], state = data['state'], country = data['country'], district = data['district'], approximate_number = int(data['approximate_number']), gender = data['gender'], cloutes = data['cloutes'], reason = data['reason'], user = user)

			missing.image = form.cleaned_data['image']

			missing.save()

			return redirect(index)


		return render(request, 'missing.html', {'form' : form })

	def get(self, request):
		return render(request, 'missing.html')

