from django.shortcuts import render
from perfis.models import *

def index(request):
	return render(request, "index.html")

def exibir(request,perfil_id):
	perfil = None
	try:
		perfil = Perfil.objects.get(id=perfil_id)
	except Exception as e:
		perfil = Perfil()
	
	return render(request, 'perfil.html', { 'perfil' : perfil})

def search_by_email(request, email):
	print(email)
	perfil = None
	try:
		perfil = Perfil.objects.get(nome=r'^Gabriel\w+')
	except Exception as e:
		perfil = Perfil()
	
	return render(request, 'perfil.html', { 'perfil' : perfil})	