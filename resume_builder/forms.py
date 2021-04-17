from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


# Resume Builder Form Here

class EducationForm(forms.ModelForm):     

    class Meta:
        model = Education
        fields = ['degree', 'stream', 'starting_year', 'passing_year', 'cgpa']
        labels = {
            'cgpa': 'CGPA'
        }



class WorkExperienceForm(forms.ModelForm): 

    class Meta:
        model = WorkExperience
        fields = ['title1', 'start_date1', 'end_date1', 'description1', 'title2', 'start_date2', 'end_date2', 'description2']
        labels = {
            'title1': 'Title',
            'start_date1': 'Start Date',
            'end_date1': 'End Date',
            'description1': 'Description',
            'title2': 'Title',
            'start_date2': 'Start Date',
            'end_date2': 'End Date',
            'description2': 'Description'
        }


class ProfessionalSkillsForm(forms.ModelForm): 

    class Meta:
        model = ProfessionalSkills
        fields = ['skill1', 'skill2', 'skill3']
        labels = {
            'skill1': '#1 Skill',
            'skill2': '#2 Skill',
            'skill3': '#3 Skill'
        }


class InterestForm(forms.ModelForm): 

    class Meta:
        model = Interest
        fields = ['interest1', 'interest2', 'interest3']
        labels = {
            'interest1': '#1 Interest',
            'interest2': '#2 Interest',
            'interest3': '#3 Interest'
        }