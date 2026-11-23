from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

def login_view(request):
    next_url = request.POST.get('next', request.GET.get('next', ''))
    if not url_has_allowed_host_and_scheme(next_url, {request.get_host()}, require_https=request.is_secure()):
        next_url = ''
    if request.user.is_authenticated:
        return redirect(next_url or 'home:home')

    if request.method == 'POST':
        login_input = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        # Support login with either username or email
        if '@' in login_input:
            user_obj = User.objects.filter(email__iexact=login_input).first()
            if user_obj:
                login_input = user_obj.username

        user = authenticate(request, username=login_input, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect(next_url or 'home:home')
        else:
            return render(request, 'login/login.html', {
                'error': 'Invalid username or password.', 'next': next_url,
            })

    return render(request, 'login/login.html', {'next': next_url})

@require_POST
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login:login')
