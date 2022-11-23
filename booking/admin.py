from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

admin.site.register(Appointment)
@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):

    list_display = ('name', 'email', 'created_on', 'message')
    search_fields = ['name', 'message']
    filter = ('created_on')
    summernote_fields = ('message',)
