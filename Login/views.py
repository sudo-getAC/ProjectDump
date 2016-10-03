from django.shortcuts import render,redirect
from .forms import *
from .models import *
import hashlib
from Team.views import dashboard

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST) 
		if form.is_valid():
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			try:
				a = User.objects.get(email=email,password=password)
			except:
				return render(request, 'home.html')
			else:
				return dashboard(request)
		else:
			return render(request, 'home.html')

def signup(request):
	return render(request, 'home.html')
