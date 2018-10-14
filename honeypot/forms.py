from django import forms
from .models import Utilisateur

class UtilisateurForm(forms.ModelForm) :

	password= forms.CharField(widget=forms.PasswordInput)
	class Meta :
		model= Utilisateur
		fields = ('login', 'password',)
