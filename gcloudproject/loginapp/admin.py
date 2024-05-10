
# Register your models here.

from django.contrib import admin
from loginapp.models import *
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    # Define the fields to display in the admin interface
    list_display = ('cuid','username',  'email', 'phone', 'is_staff', 'is_active','is_verified')
    # Define the fields that can be used to search for users
    search_fields = ('cuid','username',  'email', 'phone_number' )
    # Define the fieldsets to use in the admin interface
    fieldsets = (
        (None, {'fields': ('cuid','username',  'email', 'phone', 'password',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'registered_date',)}),
        ('Additional Information', {'fields': (  'is_verified','country' )})
    )
    # Define the fields that can be used for adding users
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username',  'email', 'phone', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )
    

# Register your CustomUser model with the admin site using the CustomUserAdmin class
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Storedotps)
# admin.site.register(EmailVerificationToken)
