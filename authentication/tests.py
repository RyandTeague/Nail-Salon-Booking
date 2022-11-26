from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase
from django.apps import apps
from authentication import forms
from .forms import RegisterUserForm
from .views import register_user, login_user, logout_user

#testing testing tests correctly


class TestDjango(TestCase):

    def test_this_thing_works(self):
        self.assertEqual(1, 1)

# This test will run through the invalid data sets and make sure they flag as invalid
# before finally testing a valid dataset


class TestRegisterUserForm(TestCase):

    def setUp(self) -> None:
        self.username = 'testuser'
        self.first_name = 'test'
        self.last_name = 'user'
        self.email = 'testuser@email.com'
        self.password = 'AGoodPassword'

    def test_registration_form(self):
        invalid_data_dicts = [
            # Non-alphanumeric username.
            {
              'data':
              {'username': 'foo/bar',
               'email': 'tests@example.com',
               'password1': '12345678',
               'password2': '12345678'},
            },
            # Non-valid email.
            {
              'data':
              {'username': 'user',
               'email': 'notanemail',
               'first_name': 'user',
               'last_name': 'test',
               'password1': 'AGoodPassword',
               'password2': 'AGoodPassword', },
            },
            # Empty username.
            {
              'data':
              {'username': '',
               'email': 'tests@example.com',
               'first_name': 'user',
               'last_name': 'test',
               'password1': 'AGoodPassword',
               'password2': 'AGoodPassword', },
            },
            # Empty first name.
            {
              'data':
              {'username': 'user',
               'email': 'tests@example.com',
               'first_name': '',
               'last_name': 'test',
               'password1': 'AGoodPassword',
               'password2': 'AGoodPassword', },
            },
            # Empty last name.
            {
              'data':
              {'username': 'user',
               'email': 'tests@example.com',
               'first_name': 'user',
               'last_name': '',
               'password1': 'AGoodPassword',
               'password2': 'AGoodPassword', },
            },
            # Bad Password.
            {
              'data':
              {'username': 'user',
               'email': 'tests@example.com',
               'first_name': 'user',
               'last_name': 'test',
               'password1': 'Password',
               'password2': 'Password', },
            },
            # Empty email.
            {
              'data':
              {'username': 'user',
               'email': '',
               'first_name': 'user',
               'last_name': 'test',
               'password1': 'AGoodPassword',
               'password2': 'AGoodPassword', },
            },
            # passwords not-matching.
            {
              'data':
              {'username': 'user',
               'email': 'tests@example.com',
               'first_name': 'user',
               'last_name': 'test',
               'password1': 'AGoodPassword',
               'password2': 'ABadPassword', },
            },
        ]

        for invalid_dict in invalid_data_dicts:
            form = forms.RegisterUserForm(data=invalid_dict['data'])
            self.failIf(form.is_valid())

        form = forms.RegisterUserForm(data={'username': 'user',
                                            'email': 'tests@example.com',
                                            'first_name': 'user',
                                            'last_name': 'test',
                                            'password1': 'AGoodPassword',
                                            'password2': 'AGoodPassword', })
        self.assertTrue(form.is_valid())

# Testing Views


class LogInTest(TestCase):
    
  def test_get_home(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'index.html', 'layout.html')

  def test_get_login(self):
    response = self.client.get('/user/login_user')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'registration/login.html', 'layout.html')

  def test_get_registration(self):
    response = self.client.get('/user/register_user')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'register_user.html', 'layout.html')
