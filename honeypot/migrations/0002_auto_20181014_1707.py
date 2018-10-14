# Generated by Django 2.1.2 on 2018-10-14 17:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('honeypot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='adr_ip',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='user_agent',
            field=models.CharField(max_length=100, null=True),
        ),
    ]