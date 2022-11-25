from django.urls import reverse
from django.test import TestCase
from django.apps import apps
from authentication import forms
from .forms import RegisterUserForm
from .views import register_user

#testing testing tests correctly
class TestDjango(TestCase):

    def test_this_thing_works(self):
        self.assertEqual(1, 1)

class TestRegisterUserForm(TestCase):

    def setUp(self) -> None:
        self.username = 'testuser'
        self.first_name = 'test'
        self.last_name = 'user'
        self.email = 'testuser@email.com'
        self.password = '12345678'

    def test_registration_form(self):
        invalid_data_dicts = [
            # Non-alphanumeric username.
            {
            'data':
            { 'username': 'foo/bar',
              'email': 'tests@example.com',
              'password1': '12345678',
              'password2': '12345678' },
            'error':
            ('username', [u"Enter a valid value."])
            },
            # Non-valid email.
            {
            'data':
            { 'username': 'user',
              'email': 'notanemail',
              'password1': '12345678',
              'password2': '12345678' },
            'error':
            ('email', [u"must enter a valid email address."])
            },
            # Already-existing username.
            {
            'data':
            { 'username': 'testuser',
              'email': 'tests@example.com',
              'password1': '12345678',
              'password2': '12345678' },
            'error':
            ('username', [u"This username is already taken. Please choose another."])
            },
            # passwords not-matching.
            {
            'data':
            { 'username': 'user',
              'email': 'tests@example.com',
              'password1': '12345678',
              'password2': '87654321' },
            'error':
            ('username', [u"This username is already taken. Please choose another."])
            },
        ]

        for invalid_dict in invalid_data_dicts:
            form = forms.RegisterUserForm(data=invalid_dict['data'])
            self.failIf(form.is_valid())
            self.assertEqual(form.errors[invalid_dict['error'][0]], invalid_dict['error'][1])

        form = forms.RegisterUserForm(data={ 'username': 'user',
                                             'email': 'tests@example.com',
                                             'password1': '12345678',
                                             'password2': '12345678' })
        self.failUnless(form.is_valid())



    def test_register_page_url(self):
        response = self.client.get("/user/register_user")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='register_user.html')

        #testing that a user is created when you register
        user = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)