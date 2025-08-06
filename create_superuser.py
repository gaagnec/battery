import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'batteryRental.settings')
django.setup()

from django.contrib.auth.models import User

# Check if the user already exists
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Superuser created successfully!")
else:
    print("Superuser already exists.")