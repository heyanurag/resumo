from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone_no = PhoneNumberField()
    linkedin = models.URLField(default=None)
    
    def __str__(self):
        return f'{self.user.username} Profile'