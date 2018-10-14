from django.db import models
from datetime import datetime

# Create your models here.

class Utilisateur(models.Model):
	login= models.CharField(max_length=100)
	password=models.CharField(max_length=50)
	adr_ip=models.CharField(max_length=100,null=True)
	user_agent=models.CharField(max_length=100,null=True)
	date=models.DateTimeField(default=datetime.now, blank=True)
