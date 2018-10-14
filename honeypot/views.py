from django.shortcuts import render,redirect
from .forms import UtilisateurForm


def login(request):

	form=UtilisateurForm(request.POST)
	if request.method== "POST" :
		if form.is_valid():
			user=form.save(commit=False)
			user.adr_ip= request.META['REMOTE_ADDR']
			user.user_agent=request.META['HTTP_USER_AGENT']
			user.save()
			return redirect('../redir')

	return render(request, 'honeypot/login.html', {'form':form})

def redir(request):
	return render (request,'honeypot/redir.html')
