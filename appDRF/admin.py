from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Fields", {"fields": ("phone_number","profile_picture")}),
    )
    list_display = ['username', 'email', 'phone_number', 'is_staff', 'is_superuser']
