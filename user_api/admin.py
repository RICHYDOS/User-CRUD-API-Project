from django.contrib import admin
from .models import *
from .forms import *

from django.contrib.auth.admin import UserAdmin
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = [
        "username",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets
    add_fieldsets =  UserAdmin.add_fieldsets

admin.site.register(CustomUser, CustomUserAdmin)


