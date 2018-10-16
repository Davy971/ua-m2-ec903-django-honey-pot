from django.shortcuts import render,redirect
from .forms import UtilisateurForm,ContactForm


def login(request):

	form=UtilisateurForm(request.POST)
	if request.method== "POST" :
		if form.is_valid():
			user=form.save(commit=False)
			x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
			if x_forwarded_for:
				user.adr_ip = x_forwarded_for.split(',')[0]
			else:
				user.adr_ip = request.META.get('REMOTE_ADDR')
			user.user_agent=request.META['HTTP_USER_AGENT']
			user.save()
			return redirect('../redir')

	return render(request, 'honeypot/login.html', {'form':form})

def contacter(request):
	form=ContactForm(request.POST)
	if request.method== "POST" :
		if form.is_valid():
			contact=form.save(commit=False)
			x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
			if x_forwarded_for:
				contact.adr_ip = x_forwarded_for.split(',')[0]
			else:
				contact.adr_ip = request.META.get('REMOTE_ADDR')
			contact.user_agent=request.META['HTTP_USER_AGENT']
			contact.save()
			return redirect('../redir')
	return render(request, 'honeypot/contact.html', {'form':form})


def redir(request):
	return render (request,'honeypot/redir.html')

def mention(request):
	title="Mention Légale"
	return render(request,'honeypot/paper1.html')

def  dnsPerso(request):
	title="Données Personnelles"
	return render(request,'honeypot/paper2.html')

def condition(request):
	title="Condition d'utilisations"
	return render(request,'honeypot/paper3.html')
