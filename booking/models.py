from django.db import models
from django.db import models
from authentication.models import Customer, Technician
from datetime import date

# Create your models here.


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