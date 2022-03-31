from attr import fields
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal information', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active','is_staff','is_superuser','groups','user_permissions')}),
        ('Social Networks', {'fields': ('web_site', 'github')}),
    )
    list_display = ['username', 'email','github','is_staff']
    pass


