from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone_no = PhoneField(blank=True)
    linkedin = models.URLField()
    