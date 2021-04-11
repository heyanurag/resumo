from django.shortcuts import render


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

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'resume_builder/about.html', context)