from django.shortcuts import render,redirect
from .forms import UtilisateurForm,ContactForm


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

def contacter(request):
	form=ContactForm(request.POST)
	if request.method== "POST" :
		if form.is_valid():
			contact=form.save(commit=False)
			contact.adr_ip=request.META['REMOTE_ADDR']
			contact.user_agent=request.META['HTTP_USER_AGENT']
			contact.save()
			return redirect('../redir')
	return render(request, 'honeypot/contact.html', {'form':form})


def redir(request):
	return render (request,'honeypot/redir.html')

def mention(request):
	title="Mention Légale"
	return render(request,'honeypot/paper.html',{'title':title})

def  dnsPerso(request):
	title="Données Personnelles"
	return render(request,'honeypot/paper.html',{'title':title})

def condition(request):
	title="Condition d'utilisations"
	return render(request,'honeypot/paper.html',{'title':title})
