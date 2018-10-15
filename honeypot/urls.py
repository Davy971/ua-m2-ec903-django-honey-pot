from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name='honeypot_accueil'),
    path('redir/',views.redir),
    path('contact/',views.contacter,name='honeypot_contact'),
    path('mention/',views.mention,name='honeypot_mention'),
    path('donnees/',views.dnsPerso,name='honeypot_dnsPerso'),
    path('condition/',views.condition,name='honeypot_condition'),


]
