from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "get_full_name", "role", "is_active")
    list_filter = ("role", "is_active")

    fieldsets = UserAdmin.fieldsets + (
        ("Hospital Info", {"fields": ("role", "phone_number")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Hospital Info", {"fields": ("role", "phone_number")}),
    )
