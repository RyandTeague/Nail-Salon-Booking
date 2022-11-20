from django.db import models
from PIL import Image


class Customer(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=50, unique=True)
    profile_pic = models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None,blank=True)
    phone_no = models.CharField(max_length=50)
    
    def __str__(self):
        return "Customer: "+self.username


class Technician(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    position = models.CharField(max_length=50) #Whether or not the staff member is trainee,senior,owner etc.
    #Customers can opt ot of having a profile picture but staff members cannot
    profile_pic = models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None,blank=False)
    phone_no = models.CharField(max_length=50)
    # Allows approval of staff accounts not everyone can create a technician account
    approved = models.BooleanField(default=False)
    
    def __str__(self):
        return "Technician: "+self.username
