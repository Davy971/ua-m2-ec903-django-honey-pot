Utilisation classique:

1. Activer son virtualenv avec: sourve venv/bin/activate
2. Se placer dans le dossier de requirements.txt
3  Lancer la commande pip install -r requirements.txt
4. Lancer la commande: python manage.py makemigrations
5. lancer la commande python manage.py migrate
6. Créer un superuser avec la commande: python manage.py createsuperuser


Utiliser Docker-compose:
1. Activer son virtualenv avec: sourve venv/bin/activate
2. Installer docker-compose: https://docs.docker.com/compose/install/   et s'ajouter dans le groupe docker : sudo usermod -aG docker $USER
3. Vérifier d'être dans le dossier contenant manage.py
4. Lancer la commande: python manage.py makemigrations
5. Lancer la commande python manage.py migrate
6. Créer un superuser avec la commande: python manage.py createsuperuser
7. Utiliser la commande docker-compose build pour construire l'Image avec le Dockerfile
8. Utiliser la commande docker-compose up pour lancer le service web et lancer le serveur à l'adresse http://0.0.0.0:8000/ 
