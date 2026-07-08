#!/bin/sh

# Quitter immédiatement si une commande échoue
set -e

echo "=== Application des migrations Django ==="
python manage.py migrate --noinput

echo "=== Démarrage de Gunicorn ==="
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000