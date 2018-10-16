from django import forms
from .models import Utilisateur,Contact

class UtilisateurForm(forms.ModelForm) :
	class Meta :
		model= Utilisateur
		fields = ('login', 'password',)
		widgets={
		'password': forms.PasswordInput(),
		}

class ContactForm(forms.ModelForm):
	class Meta :
		model= Contact
		exclude = ('adr_ip','user_agent','date',)
