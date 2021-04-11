from django.shortcuts import render


def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'resume_builder/home.html', context)

def create(request):
    context = {
        'title': 'Create'
    }
    return render(request, 'resume_builder/create.html', context)