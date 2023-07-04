from django import forms
from django.forms import ModelForm

from .models import Company, ContactCompany, Jobs, Requirements


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name']


class ContactCompanyForm(forms.ModelForm):
    class Meta:
        model = ContactCompany
        exclude = ['company']
        fields = [
            'manager',
            'email',
            'cellphone',
            'commercial_phone'
        ]


class RequirementsForm(ModelForm):
    class Meta:
        model = Requirements
        fields = ['name']


class JobsForm(ModelForm):
    class Meta:
        model = Jobs
        fields = []
