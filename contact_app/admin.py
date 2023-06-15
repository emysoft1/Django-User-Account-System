from django.contrib import admin
from .models import Department, Contact

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'email')
    search_fields = ('department_name', 'email')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'subject')
    search_fields = ('user__username', 'department__department_name', 'subject')
    list_filter = ('department',)
