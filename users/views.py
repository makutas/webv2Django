from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # DISPLAY BLANK REGISTER FORM
        form = UserCreationForm()
    else:
        # PROCESS COMPLETED FORM
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # LOG THE USER IN AND REDIRECT TO HOME PAGE
            login(request, new_user)
            return redirect('recipes:index')
    # DISPLAY A BLANK OR INVALID FORM
    context = {'form': form}
    return render(request, 'registration/registration.html', context)
