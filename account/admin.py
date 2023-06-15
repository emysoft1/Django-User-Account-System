from django.contrib import admin
from .models import User, Profile


class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['email', 'first_name', 'last_name']}),
        ('Permissions', {'fields': ['is_staff', 'is_superuser']}),
    ]


class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user', 'bio', 'date_of_birth', 'profile_picture']}),
    ]


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
