from django.contrib import admin
from authentication.models import Customer, Technician
from booking.models import Contact, Treatments, Booking
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Customer)
admin.site.register(Technician)

@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):

    list_display = ('name', 'email', '', 'message')
    search_fields = ['name', 'message']
    list_filter = ('created_on')
    summernote_fields = ('message',)

admin.site.register(Treatments)
admin.site.register(Booking)