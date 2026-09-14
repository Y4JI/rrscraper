from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import UserSettings


class UserSettingsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123',
            email='test@example.com'
        )

    def test_settings_creation(self):
        settings_obj = UserSettings.objects.create(
            user=self.user,
            dark_mode=True,
            email_notifications=False
        )
        self.assertEqual(str(settings_obj), 'Settings for testuser')
        self.assertTrue(settings_obj.dark_mode)
        self.assertFalse(settings_obj.email_notifications)

    def test_settings_view_login_required(self):
        response = self.client.get(reverse('user_settings:settings'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_settings_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('user_settings:settings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_settings/user_settings.html')

    def test_settings_update(self):
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.post(reverse('user_settings:settings'), {
            'dark_mode': 'on',
            'email_notifications': 'on',
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        settings_obj = UserSettings.objects.get(user=self.user)
        self.assertTrue(settings_obj.dark_mode)
        self.assertTrue(settings_obj.email_notifications)
