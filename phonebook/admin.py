from django.contrib import admin
from .models import Contact, Phone

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class PhoneAdmin(admin.ModelAdmin):
    list_display = ['number', 'contact']
    search_fields = ['number']

admin.site.register(Contact, ContactAdmin)
admin.site.register(Phone, PhoneAdmin)
