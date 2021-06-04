from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Education(models.Model):
    degree = models.CharField(max_length=50)
    stream = models.CharField(max_length=100)
    starting_year = models.IntegerField()
    passing_year = models.IntegerField()
    cgpa = models.FloatField()
    modify_date = models.DateTimeField(auto_now_add=True)
    person = models.ForeignKey(User, on_delete=models.CASCADE)


class WorkExperience(models.Model):
    title1 = models.CharField(max_length=100, blank=True)
    start_date1 = models.CharField(max_length=15, blank=True)
    end_date1 = models.CharField(max_length=15, blank=True)
    description1 = models.TextField(blank=True)
    title2 = models.CharField(max_length=100, blank=True)
    start_date2 = models.CharField(max_length=15, blank=True)
    end_date2 = models.CharField(max_length=15, blank=True)
    description2 = models.TextField(blank=True)
    modify_date = models.DateTimeField(auto_now_add=True, blank=True)
    person = models.ForeignKey(User, on_delete=models.CASCADE)


class ProfessionalSkills(models.Model):
    skill1 = models.CharField(max_length=100)
    skill2 = models.CharField(max_length=100, blank=True)
    skill3 = models.CharField(max_length=100,blank=True)
    modify_date = models.DateTimeField(auto_now_add=True)
    person = models.ForeignKey(User, on_delete=models.CASCADE)


class Interest(models.Model):
    interest1 = models.CharField(max_length=100)
    interest2 = models.CharField(max_length=100, blank=True)
    interest3 = models.CharField(max_length=100, blank=True)
    modify_date = models.DateTimeField(auto_now_add=True)
    person = models.ForeignKey(User, on_delete=models.CASCADE)