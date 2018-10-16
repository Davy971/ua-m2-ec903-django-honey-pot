from django.contrib import admin
from .models import Utilisateur,Contact



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['adr_ip', 'date']
    ordering = ['date']

@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ['adr_ip', 'date']
    ordering = ['date']
