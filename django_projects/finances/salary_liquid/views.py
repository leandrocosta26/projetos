from django.shortcuts import render
from salary_liquid.models import *

def index(request, sal):
	sal1 = salario(float(sal))
	return render(request, 'index.html', { 'salario' : sal1 })
