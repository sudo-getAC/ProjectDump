from django.shortcuts import render

# Create your views here.
def dashboard(request):
	return render(request, 'dashboard.html')

def tasks(request):
	return render(request, 'tasks.html')

def discussions(request):
	return render(request, 'discussions.html')

def teams(request):
	return render(request, 'teams.html')
