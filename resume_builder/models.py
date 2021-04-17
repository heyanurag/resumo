from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Education(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    degree = models.CharField(max_length=50)
    stream = models.CharField(max_length=100)
    starting_year = models.DateField()
    passing_year = models.DateField()
    cgpa = models.FloatField()


class WorkExperience(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    title1 = models.CharField(max_length=100, blank=True)
    start_date1 = models.DateField(blank=True)
    end_date1 = models.DateField(blank=True)
    description1 = models.TextField(blank=True)

    title2 = models.CharField(max_length=100, blank=True)
    start_date2 = models.DateField(blank=True)
    end_date2 = models.DateField(blank=True)
    description2 = models.TextField(blank=True)


class ProfessionalSkills(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    skill1 = models.CharField(max_length=100)
    skill2 = models.CharField(max_length=100, blank=True)
    skill3 = models.CharField(max_length=100,blank=True)


class Interest(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    interest1 = models.CharField(max_length=100)
    interest2 = models.CharField(max_length=100, blank=True)
    interest3 = models.CharField(max_length=100, blank=True)