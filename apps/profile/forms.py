from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'bio', 'profile_image']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter your full name',
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Tell us about yourself and your favorite web fiction genres...',
                'rows': 4,
            }),
            'profile_image': forms.FileInput(attrs={
                'class': 'form-file-input',
                'accept': 'image/*',
            }),
        }
