from django.test import TestCase
from .forms import RegisterUserForm

class TestRegisterUserForm(TestCase):
    def test_email_is_required(self):
        form = RegisterUserForm(email = '')
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')