# Generated by Django 2.1.2 on 2018-10-14 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('honeypot', '0002_auto_20181014_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=12)),
                ('sujet', models.CharField(max_length=50)),
            ],
        ),
    ]
