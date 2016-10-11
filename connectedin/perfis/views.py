from django.shortcuts import render
from perfis.models import *

def index(request):
	return render(request, "index.html")

def exibir(request,perfil_id):
	perfil = None
	if perfil_id == '1' : 
		perfil = Perfil('leleco', 'leleco@gmail.com', '0000', 'walmart.com')
	if perfil_id == '2' : 
		perfil = Perfil('pita', 'pita@gmail.com', '1111', 'walmart.com')

	return render(request, 'perfil.html', { 'perfil' : perfil})