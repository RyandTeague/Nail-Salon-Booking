from django.contrib import admin
from .models import Appointment, Contact
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = ('user', 'service', 'day', 'time')
    search_fields = ['user', 'service', 'day']
    list_filter = ('day', 'service', 'time')


@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):

    list_display = ('name', 'email', 'message')
    search_fields = ['name', 'message']
    summernote_fields = ('message',)
