import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.db import connection

with connection.cursor() as cursor:
    print("Dropping public schema...")
    cursor.execute("DROP SCHEMA public CASCADE;")
    print("Recreating public schema...")
    cursor.execute("CREATE SCHEMA public;")
    print("Database schema reset successfully.")
