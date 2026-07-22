import os
import django

# Configuration de l'environnement Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.db import connection

print("=== NETTOYAGE DES TABLES D'AUTHENTIFICATION ===")

with connection.cursor() as cursor:
    # 1. Supprime les anciennes tables d'authentification et d'admin
    cursor.execute("DROP TABLE IF EXISTS django_admin_log CASCADE;")
    cursor.execute("DROP TABLE IF EXISTS auth_user CASCADE;")
    cursor.execute("DROP TABLE IF EXISTS app_auth_customuser CASCADE;")
    
    # 2. Re-crée les séquences si nécessaire et nettoie l'historique de migration
    cursor.execute("""
        DELETE FROM django_migrations 
        WHERE app IN ('admin', 'auth', 'app_auth', 'authtoken', 'sessions');
    """)

print("=== NETTOYAGE TERMINÉ AVEC SUCCÈS ===")