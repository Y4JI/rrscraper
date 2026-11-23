from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse


class AccountFlowTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('reader', 'reader@example.net', 'Reader*94258')
        self.login_url = reverse('login:login')

    def test_login_preserves_protected_destination(self):
        destination = '/novels/42/'
        response = self.client.get(self.login_url, {'next': destination})
        self.assertContains(response, 'value="/novels/42/"')
        response = self.client.post(self.login_url, {
            'username': self.user.email, 'password': 'Reader*94258', 'next': destination,
        })
        self.assertRedirects(response, destination, fetch_redirect_response=False)

    def test_login_rejects_external_destination(self):
        response = self.client.post(self.login_url, {
            'username': self.user.username, 'password': 'Reader*94258', 'next': 'https://evil.example/path',
        })
        self.assertRedirects(response, reverse('home:home'), fetch_redirect_response=False)

    def test_failed_login_retains_destination(self):
        response = self.client.post(self.login_url, {
            'username': self.user.username, 'password': 'wrong', 'next': '/profile/',
        })
        self.assertContains(response, 'value="/profile/"')

    def test_logout_requires_post_and_csrf(self):
        client = Client(enforce_csrf_checks=True)
        client.force_login(self.user)
        url = reverse('login:logout')
        self.assertEqual(client.get(url).status_code, 405)
        self.assertEqual(client.post(url).status_code, 403)
        client.get(reverse('profile:profile'))
        response = client.post(url, {'csrfmiddlewaretoken': client.cookies['csrftoken'].value})
        self.assertRedirects(response, self.login_url)
        self.assertNotIn('_auth_user_id', client.session)
