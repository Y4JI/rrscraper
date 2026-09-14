from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Profile


class ProfileTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123',
            email='test@example.com'
        )

    def test_profile_creation(self):
        profile = Profile.objects.create(
            user=self.user,
            full_name='Test Reader',
            bio='Loves progression fantasy'
        )
        self.assertEqual(str(profile), 'testuser')
        self.assertEqual(profile.full_name, 'Test Reader')

    def test_profile_view_login_required(self):
        response = self.client.get(reverse('profile:profile'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_profile_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('profile:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/profile.html')

    def test_profile_update(self):
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.post(reverse('profile:profile'), {
            'full_name': 'Updated Name',
            'bio': 'Updated Bio',
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.full_name, 'Updated Name')
        self.assertEqual(profile.bio, 'Updated Bio')
