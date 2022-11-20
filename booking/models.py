from django.db import models
from authentication.models import Customer, Technician
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
SERVICE_CHOICES = (
    ("Gel Polish", "Gel Polish"),
    ("Biab First Application", "Biab First Application")
    ("Biab Infill", "Biab Infill")
    ("Apres Gel Extension", "Apres Gel Extension")
    ("Removal & Mani", "Removal & Mani")
)

TIME_CHOICES = (
    ("9:00", "9:00"),
    ("9:30", "9:30"),
    ("10:00", "10:00"),
    ("10:30", "10:30"),
    ("11:00", "11:00"),
    ("11:30", "11:30"),
    ("12:00", "12:00"),
    ("12:30", "12:30"),
    ("14:00", "14:00"),
    ("14:30", "14:30"),
    ("15:00", "15:00"),
    ("15:30", "15:30"),
    ("16:00", "16:00"),
    ("16:30", "16:30"),
)

class Appointment(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="Gel Polish")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="9:00")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField(max_length=2000)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):     
        return self.name


class Treatments(models.Model):
    manager = models.ForeignKey(Technician, on_delete=models.CASCADE)
    treatment_type = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
    price = models.FloatField(default=1000.00)
    no_of_days_advance = models.IntegerField()
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    treatment_image = models.ImageField(upload_to="media", 
        height_field=None, width_field=None, 
        max_length=None, default='0.jpeg')
    def __str__(self):
        return "Treatment No: "+str(self.id)


class Booking(models.Model):
    manager = models.ForeignKey(Treatments, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_day = models.DateField(auto_now=False, auto_now_add=False)
    end_day = models.DateField(auto_now=False, auto_now_add=False)
    amount = models.FloatField()
    booked_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return "Booking ID: " + str(self.id)