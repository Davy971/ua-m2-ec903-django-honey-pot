from django import forms
from .models import Utilisateur,Contact

class UtilisateurForm(forms.ModelForm) :

	password= forms.CharField(widget=forms.PasswordInput)
	class Meta :
		model= Utilisateur
		fields = ('login', 'password',)

class ContactForm(forms.ModelForm):
	class Meta :
		model= Contact
		exclude = ('adr_ip','user_agent','date',)
