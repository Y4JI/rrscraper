# pyrefly: ignore [missing-import]
from django.shortcuts import render

# Create your views here.

def login_view(request):
    """Renders the login page for the scraper application."""
    return render(request, 'scraper/login.html')

def register_view(request):
    """Renders the registration page."""
    return render(request, 'scraper/register.html')

def home_view(request):
    """Renders the main home screen."""
    return render(request, 'scraper/home.html')

