from django.contrib import admin

from .models import Company, ContactCompany, Jobs, Requirements

admin.site.register(Company)
admin.site.register(ContactCompany)
admin.site.register(Requirements)
admin.site.register(Jobs)
