from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm


@login_required(login_url='login:login')
def profile_view(request):
    """View and update user profile."""
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile:profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile/profile.html', {
        'form': form,
        'profile': profile,
    })
