from django.db import models
from django.db.models import Model
from datetime import date, datetime
from django.contrib.auth.models import User

# Create your models here.
SERVICE_CHOICES = (
    ("Gel Polish", "Gel Polish"),
    ("Biab First Application", "Biab First Application"),
    ("Biab Infill", "Biab Infill"),
    ("Apres Gel Extension", "Apres Gel Extension"),
    ("Removal & Mani", "Removal & Mani"),
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="Gel Polish")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="9:00")
#    time_ordered = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField(max_length=2000)

    def __str__(self):     
        return self.name