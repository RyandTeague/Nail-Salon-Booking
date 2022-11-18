from django.db import models
from django.db.models.deletion import CASCADE
import uuid

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    otp_code = models.CharField(max_length=6, unique=True, null=True)
    email_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.username

class Technician(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    avatar_url = models.CharField(max_length=260, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return f"Technician {self.first_name} {self.last_name}"

class TreatmentType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=30, unique=True)
    price = models.CharField(max_length=10)
    duration = models.DurationField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return f"Treatment: {self.type} price: {self.price} Duration: {self.duration}"

class TreatmentStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return f"Treatment {self.status}"

class Treatment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    treatment_type_id = models.ForeignKey(TreatmentType, on_delete=models.CASCADE)
    treatment_status_id = models.ForeignKey(TreatmentStatus, on_delete=models.CASCADE)
    treatment_name = models.CharField(max_length=5, unique=True)
    price = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return f"Treatment {self.treatment_name} price:{self.price} is currently {self.treatment_status_id}"

class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    treatment_id = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(User, on_delete=CASCADE)
    staff_id = models.ForeignKey(Technician, on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return f'Booking by customer {self.customer_id} paid {self.payment_id} for room {self.treatment_id}'