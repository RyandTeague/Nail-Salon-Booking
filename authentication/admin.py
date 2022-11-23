from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as OriginalUserAdmin

class UserAdmin(OriginalUserAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_staff')
    list_filter = ('is_staff', 'first_name')
    search_fields = ('first_name', 'last_name', 'username', 'email')
    actions = ['hired', 'fired']

    def hired(self, request, queryset):
        queryset.update(is_staff=True)

    def fired(self, request, queryset):
        queryset.update(is_staff=False)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)