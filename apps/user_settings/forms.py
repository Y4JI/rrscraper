from django import forms
from .models import UserSettings


class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserSettings
        fields = ['dark_mode', 'email_notifications']
        widgets = {
            'dark_mode': forms.CheckboxInput(attrs={
                'class': 'toggle-checkbox',
                'id': 'darkModeToggle',
                'aria-labelledby': 'appearance-label',
            }),
            'email_notifications': forms.CheckboxInput(attrs={
                'class': 'toggle-checkbox',
                'id': 'emailNotificationsToggle',
                'aria-labelledby': 'digest-label',
            }),
        }
