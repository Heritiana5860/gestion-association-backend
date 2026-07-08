# FROM python:3.11-slim

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install -r requirements.txt --no-cache-dir

# COPY . .

# EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


FROM python:3.11-slim

# Éviter que Python écrive des fichiers .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# Éviter que Python mette en tampon les sorties (utile pour les logs Koyeb)
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Installer les dépendances Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du projet
COPY . /app/

# Exposer le port par défaut de Koyeb (8000)
EXPOSE 8000

# Commande pour démarrer l'application avec Gunicorn (fortement recommandé en prod)
# Remplace "mon_projet" par le nom de ton dossier contenant wsgi.py
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]