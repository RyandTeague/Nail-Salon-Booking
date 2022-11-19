from django.contrib import admin
from authentication.models import Customer, RoomManager
from booking.models import Contact, Rooms, Booking

admin.site.register(Customer)
admin.site.register(RoomManager)