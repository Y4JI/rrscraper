from django.test import TestCase

from .forms import UserRegistrationForm


class RegistrationPasswordTests(TestCase):
    def form(self, password):
        return UserRegistrationForm({
            'username': 'reader', 'email': 'reader@example.net',
            'password': password, 'confirm_password': password,
        })

    def test_configured_password_validators_apply(self):
        for password in ('123456', 'password', 'reader'):
            with self.subTest(password=password):
                form = self.form(password)
                self.assertFalse(form.is_valid())
                self.assertIn('password', form.errors)

    def test_valid_password_is_hashed(self):
        form = self.form('Unique*Cathedral824')
        self.assertTrue(form.is_valid(), form.errors)
        user = form.save()
        self.assertTrue(user.check_password('Unique*Cathedral824'))
