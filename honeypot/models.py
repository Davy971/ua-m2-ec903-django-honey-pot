from django.db import models
from django import forms
from datetime import datetime

# Create your models here.

class Utilisateur(models.Model):
	login= models.CharField(max_length=100,blank=True)
	password=models.CharField(max_length=50,blank=True)
	adr_ip=models.CharField(max_length=100,null=True)
	user_agent=models.CharField(max_length=100,null=True)
	date=models.DateTimeField(default=datetime.now, blank=True)

class Contact(models.Model):
	Nom=models.CharField(max_length=50)
	prenom=models.CharField(max_length=50)
	email=forms.EmailField(label="Votre adresse e-mail")
	tel=models.CharField(max_length=12)
	sujet=models.CharField(max_length=50)
	message=models.TextField(max_length=1000,null=True)
	adr_ip=models.CharField(max_length=100,null=True)
	user_agent=models.CharField(max_length=100,null=True)
	date=models.DateTimeField(default=datetime.now, blank=True)
