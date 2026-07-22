#!/bin/sh

# Quitter immédiatement si une commande échoue
set -e

echo "=== Exécution du nettoyage ciblé de l'authentification ==="
python clean_auth.py

echo "=== Application des migrations Django ==="
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "=== Création du Superuser ==="
python create_admin.py

echo "=== Démarrage de Gunicorn ==="
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000