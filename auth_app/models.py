from django.db import models
import random
import string
from datetime import timedelta
from django.utils import timezone


class AllowedDomain(models.Model):
    """Model to store allowed email domains"""
    domain = models.CharField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.domain
    
    @classmethod
    def is_email_allowed(cls, email):
        """Check if an email's domain is in the allowed list"""
        if not email or '@' not in email:
            return False
        
        domain = email.split('@')[-1].lower()
        return cls.objects.filter(domain=domain, active=True).exists()


class AuthCode(models.Model):
    """Model to store authentication codes"""
    email = models.EmailField()
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    used = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.email} - {self.code}"
    
    def is_valid(self):
        """Check if the code is still valid"""
        return not self.used and timezone.now() < self.expires_at
    
    @classmethod
    def generate_code(cls, email, expiry_minutes=10):
        """Generate a new 6-digit authentication code"""
        # Generate a random 6-digit code
        code = ''.join(random.choices(string.digits, k=6))
        
        # Create expiration time
        expires_at = timezone.now() + timedelta(minutes=expiry_minutes)
        
        # Create the auth code in the database
        auth_code = cls.objects.create(
            email=email,
            code=code,
            expires_at=expires_at
        )
        
        return auth_code
