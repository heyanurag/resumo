from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


# Resume Builder Form Here

class EducationForm(forms.ModelForm):     

    class Meta:
        model = Education
        fields = ['person', 'degree', 'stream', 'starting_year', 'passing_year', 'cgpa']


class WorkExperienceForm(forms.ModelForm): 

    class Meta:
        model = WorkExperience
        fields = ['person', 'title1', 'start_date1', 'end_date1', 'description1', 'title2', 'start_date2', 'end_date2', 'description2']

class ProfessionalSkillsForm(forms.ModelForm): 

    class Meta:
        model = ProfessionalSkills
        fields = ['person', 'skill1', 'skill2', 'skill3']

class InterestForm(forms.ModelForm): 

    class Meta:
        model = Interest
        fields = ['person', 'interest1', 'interest2', 'interest3']