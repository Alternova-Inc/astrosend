import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'astrosend.settings')
django.setup()

from apps.auth_app.models import AllowedDomain

# Define allowed domains
allowed_domains = [
    'alternova.com',
    'alternova.dev',
    # Add more domains as needed
]

# Create allowed domains
for domain in allowed_domains:
    AllowedDomain.objects.get_or_create(domain=domain)

print(f"Created {len(allowed_domains)} allowed domains:")
for domain in AllowedDomain.objects.all():
    print(f"- {domain.domain}") 