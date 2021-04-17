from django.shortcuts import render, redirect
from .models import Education, WorkExperience, ProfessionalSkills, Interest
from .forms import EducationForm, WorkExperienceForm, ProfessionalSkillsForm, InterestForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'resume_builder/home.html', context)


def create(request):
    context = {
        'title': 'Create A Resume'
    }
    return render(request, 'resume_builder/create.html', context)


class EducationCreateView(CreateView):
    model = Education
    form_class = EducationForm
    template_name = 'resume_builder/education_form.html'
    success_url = reverse_lazy('create')

    def form_valid(self, form):
        form.instance.person = self.request.user
        return super().form_valid(form)


class WorkExperienceCreateView(CreateView):
    model = WorkExperience
    form_class = WorkExperienceForm
    template_name = 'resume_builder/workexp_form.html'
    success_url = reverse_lazy('create')

    def form_valid(self, form):
        form.instance.person = self.request.user
        return super().form_valid(form)



class SkillsCreateView(CreateView):
    model = ProfessionalSkills
    form_class = ProfessionalSkillsForm
    template_name = 'resume_builder/skills_form.html'
    success_url = reverse_lazy('create')

    def form_valid(self, form):
        form.instance.person = self.request.user
        return super().form_valid(form)



class InterestCreateView(CreateView):
    model = Interest
    form_class = InterestForm
    template_name = 'resume_builder/interest_form.html'
    success_url = reverse_lazy('create')

    def form_valid(self, form):
        form.instance.person = self.request.user
        return super().form_valid(form)



def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'resume_builder/about.html', context)


def resume(request):
    context = {
        'workexp': WorkExperience.objects.filter(person=request.user).first(),
        'skills': ProfessionalSkills.objects.filter(person=request.user).first(),
        'education': Education.objects.filter(person=request.user).first(),
        'interest': Interest.objects.filter(person=request.user).first(),
        'title': 'Resume'
    }
    return render(request, 'resume_builder/resume.html', context)