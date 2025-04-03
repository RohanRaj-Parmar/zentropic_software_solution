# requests/admin.py
from django.contrib import admin
from .models import CustomerRequest

@admin.register(CustomerRequest)
class CustomerRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service_type', 'created_at', 'status')
    list_filter = ('service_type', 'status', 'created_at')
    search_fields = ('name', 'email', 'description')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Client Information', {
            'fields': ('name', 'email', 'company', 'phone')
        }),
        ('Request Details', {
            'fields': ('service_type', 'description', 'budget', 'timeline')
        }),
        ('Status', {
            'fields': ('status', 'admin_notes')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )