from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(blank=True)
    phone_no = PhoneNumberField(blank=True)
    linkedin = models.URLField(blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'