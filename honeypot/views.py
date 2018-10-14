from django.shortcuts import render,redirect
from .forms import UtilisateurForm


def login(request):

	form=UtilisateurForm(request.POST)
	if request.method== "POST" :
		if form.is_valid():
			form.save()
			return redirect('../accueil')

	return render(request, 'honeypot/login.html', {'form':form})

def accueil(request):
	return render (request,'honeypot/accueil.html')
