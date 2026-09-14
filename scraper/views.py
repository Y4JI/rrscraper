from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegistrationForm

def login_view(request):
    """Renders the login page and handles user authentication."""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        login_input = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        # Support login with either username or email
        user_obj = None
        if '@' in login_input:
            user_obj = User.objects.filter(email__iexact=login_input).first()
            if user_obj:
                login_input = user_obj.username

        user = authenticate(request, username=login_input, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            messages.error(request, "Invalid username/email or password.")

    return render(request, 'scraper/login.html')

def register_view(request):
    """Renders the registration page and creates a validated user account."""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto log-in after registration
            messages.success(request, f"Registration successful! Welcome, {user.username}.")
            return redirect('home')
        else:
            # Form errors will be rendered by the template
            pass
    else:
        form = UserRegistrationForm()

    return render(request, 'scraper/register.html', {'form': form})

def logout_view(request):
    """Logs out the user and redirects to login."""
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')

@login_required(login_url='login')
def home_view(request):
    """Renders the main home screen (protected)."""
    return render(request, 'scraper/home.html')

