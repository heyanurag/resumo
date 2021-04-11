from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Account has been created, you will now be able to Log In')
            return redirect('sign-in')
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Create an Account',
        'form': form
    }
    return render(request, 'users/register.html', context)