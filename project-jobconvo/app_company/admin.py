from django.contrib import admin

from .models import Company, ContactCompany, Jobs, Requirements

admin.site.register(Requirements)
admin.site.register(Jobs)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'cnpj', 'created_at')


class ContactCompanyAdmin(admin.ModelAdmin):
    list_display = ('company',
                    'manager',
                    'email',
                    'format_cellphone',
                    'format_phone_commercial')


admin.site.register(Company, CompanyAdmin)
admin.site.register(ContactCompany, ContactCompanyAdmin)
