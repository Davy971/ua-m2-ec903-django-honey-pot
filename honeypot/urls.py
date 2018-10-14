from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login),
    path('redir/',views.redir),
    path('contact/',views.contacter),
]
