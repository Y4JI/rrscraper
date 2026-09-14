from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegistrationForm

def register_view(request):
    """Renders the registration page and creates a validated user account."""
    if request.user.is_authenticated:
        return redirect('home:home')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Registration successful! Please log in.")
            return redirect('login:login')
    else:
        form = UserRegistrationForm()

    return render(request, 'register/register.html', {'form': form})
