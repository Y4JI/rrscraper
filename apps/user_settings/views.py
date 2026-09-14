from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import UserSettings
from .forms import UserSettingsForm


@login_required(login_url='login:login')
def settings_view(request):
    """View and update user preferences and settings."""
    settings_obj, _ = UserSettings.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserSettingsForm(request.POST, instance=settings_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Settings saved successfully!')
            return redirect('user_settings:settings')
    else:
        form = UserSettingsForm(instance=settings_obj)

    return render(request, 'user_settings/user_settings.html', {
        'form': form,
        'settings': settings_obj,
    })
