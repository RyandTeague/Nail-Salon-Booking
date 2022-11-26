# Nail Salon

![Mock up of website on several differently sized devices](media/images/mockup.png)

The nail salon website is an appointment managing website for the fictitious salon "nailed it" where users can book,edit, update and delete appointments and staff members can view appointments. This website was built using the Django python framework.

Customers are also able to send a form directly to the website which is stored and readable for staff on the administration page.

The live link can be found here - https://nail-salon-booking.herokuapp.com

## Features

### Existing Features

- Landing Page
    - On the landing page, new users will see this nav bar. allowing them to access the contact page, booking or sign in/sign up.

![Nav bar for signed out users](media/images/navbarnotsignedin.PNG)

    - When a regular customer signs in they will see this version of the nav bar, the user option will give them a drop down menu that allows them to access the user panel or logout.
![Nav bar for signed in customers](media/images/navbarnotstaff.PNG)

    -The full landing page and nav bar that staff members will see is shown below. The booking button will take users to the online booking feature.
![Landing Page for signed in staff](media/images/index.PNG)

    - The code that changes this view is in the layout.html template:
```                     
                        {% if user.is_authenticated %}
                        {% if user.is_staff %}
                        <!--Staff Link-->
                        <li class="nav-item">
                            <a class="nav-link active cHover" href="{% url 'staffPanel' %}">Staff Panel</a>
                        </li>
                        {% endif %}
                        <li class="nav-item dropdown me-3 fs-5">
                            <a class="nav-link active dropdown-toggle cHover" href="#" role="button"
                                data-bs-toggle="dropdown" aria-expanded="false">
                                User
                            </a>
                            <ul class="dropdown-menu  border zNav" style="background-color: #F0E6EF;">
                                <li><a class="dropdown-item" href="{% url 'userPanel' %}">User Panel</a></li>
                                <li>
                                    <hr class="">
                                </li>
                                <li><a class="dropdown-item" href="{% url 'logout' %}?next=/">Sign Out</a></li>
                            </ul>
                        </li>
                        {% else %}
                        <li class="nav-item me-3">
                            <a class="nav-link active cHover" href="{% url 'register' %}">Sign in/Sign Up</a>
                        </li>
                        {% endif %}

```
- Combat
    - In some rooms there are enemies that will take the player's HP and the player will have to either attack and kill the enemy or flee
        - Currently the only implemented enemy is the giant spider.

![Screenshot of player being attacked by a spider](images/enemy.PNG)

- Finding Loot
    - the player is able to find different kind of items in the dungeon and add them to their inventory
        -currently implemented is the ability to find a dagger which does more damage than the default rock
    - The player is also able to find gold which updates their total gold amount

![Screen where player finds dagger](images/finddagger.PNG)
![Inventory screen with dagger and 15 gold](images/Inventory.PNG)
![Screen where player finds gold](images/foundgold.PNG)
![Inventory screen with 20 gold](images/inventorygold.PNG)

- Winning and losing the game
    - The player is able to win the game by finding the room that is the exit to the cave

![Screen that says the player has won the game](images/winstate.PNG)
![Screen that says the player has died and lost the game](images/gameover.PNG)

- Gathering feedback data from Player
    - When the player enters a command that isn't on the list of available actions they are told that their input is invalid. They are then asked what they were trying to do.
    The input and the explanation are then dat and timestamped and sent to a google sheet where the developer can see this information. The intent behind this is that there are many different ways of giving a similar command (eg. 'Move North', 'Go North', 'North' etc...) so this way the developer can easily copy in words player are trying to use for available commands into action's keywords. The developer can also use inputs that were trying to do actions that arn't in the game as inspiration to add features that player's want.

![Screenshot that says the player has entered a wrong input and asks what they were trying to do](images/feedback.PNG)
![Screenshot of google sheet where feedback input is sent](images/feedbacksheet.PNG)

### Future Features

- Staff CRUD
    - A useful feature for future implementation would be allowing staff members to edit and delete appointments form the staff panel

- Multiple calenders
    - If the salon had multiple technicians then the appointment calender would need to be changed so that each technician had their own calenders that customers could select from

- E-mail Reminders
    - A useful feature to implement would be to have an automated email be sent to customers reminding them of their appointment.

## Data Model

- The website is made up of two apps. The authentication app handles user registration and sign-in/out. The book app handles the creation and management of appointments.

### Authentication

- This authenitication uses the default django user model.
- There is one form in this app which allows users to fill in the fields for the user model.
- There are three views associated with the authenitication app:
    - login_user takes the post from login.html and authenticates the username and password submited.
    if the user exists then the user is redirected to their user-panel, otherwise they are redirected back to the login page.
    - logout_user calls the logout function and redirects the user to the landing page.
    - register_user takes the post from RegisterUserForm form and checks if the form is valid then if successful it also calls the log in user function and redirects the user to the landing page

### Booking

- The booking app contains two models:
    - The contact model has three fields which users fill out manually: name, email, and message.
    - The Appointment model has five fields. 


## Testing

### Validator Testing

- Html
    - Using w3 validator templates were passing ignoring Django html template syntax
    - https://validator.w3.org/nu/

- Python
    - Passed pycodestyle formatting

### Compatibility Testing

Site was tested across multiple virtual devices through chrome developor tools.

Site was tested to work on Google chrome, firefox, microsoft edge and internet explorer.

### Manual Testing

#### Booking

```

class BookUrlTests(TestCase):

    def test_get_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        response2 = self.client.get(reverse('index'))
        self.assertEqual(response2.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'layout.html')

    def test_get_contact_us(self):
        response = self.client.get('/contact-us')
        self.assertEqual(response.status_code, 200)
        response2 = self.client.get(reverse('contact-us'))
        self.assertEqual(response2.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html', 'layout.html')

    def test_get_booking(self):
        response = self.client.get('/booking')
        self.assertEqual(response.status_code, 200)
        response2 = self.client.get(reverse('booking'))
        self.assertEqual(response2.status_code, 200)
        self.assertTemplateUsed(response, 'booking.html', 'layout.html')

    def test_get_booking_submit(self):
        response = self.client.get('/booking-submit')
        self.assertEqual(response.status_code, 200)
        response2 = self.client.get(reverse('bookingSubmit'))
        self.assertEqual(response2.status_code, 200)
        self.assertTemplateUsed(response, 'bookingSubmit.html', 'layout.html')

    def test_get_staff_panel(self):
        response = self.client.get('/staff-panel')
        self.assertEqual(response.status_code, 200)
        response2 = self.client.get(reverse('staffPanel'))
        self.assertEqual(response2.status_code, 200)
        self.assertTemplateUsed(response, 'staffPanel.html', 'layout.html')

    #login required pages
    def test_get_user_panel(self):
        test_user = User.objects.create_user(username='testuser', password='AGoodPassword')
        login = self.client.login(username='testuser', password='AGoodPassword')
        response = self.client.get('/user-panel')
        self.assertEqual(str(response.context['user']), 'testuser')
        self.assertEqual(response.status_code, 200)
        response2 = self.client.get(reverse('userPanel'))
        self.assertEqual(response2.status_code, 200)
        self.assertTemplateUsed(response, 'userPanel.html', 'layout.html')

```

#### Authentication

```
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

```

## Deployment

- The site was deployed using Code Institute's mock terminal for Heorku. The steps to deploy are as follows
    - Create a new Heroku App
    - Set the buildbacks to Python and NodeJS in that order
    - Link the heroku app to a PostgreSQL database hosted on https://www.elephantsql.com
    - Link the heroku app to the repository
    - Click on Deploy

## Credits

- To complete this project I used Code Institute student template: [gitpod full template](https://github.com/Code-Institute-Org/python-essentials-template)

- Bootstrap framework was used to help write the html and css in the templates.

### Code

- Tutorials I followed to create the basis of this code are as follows:
    -https://www.thetechplatform.com/post/develop-an-hotel-management-system-with-django
- https://www.google.co.uk/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiMw-7868r7AhVjxDgGHUkHC98QwqsBegQIChAF&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DrHZwE1AK1h8&usg=AOvVaw3cyttpzMTyD7QJFg-lzosP
- https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78

