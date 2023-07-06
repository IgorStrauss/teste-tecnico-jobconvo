from django import forms
from django.forms import ModelForm

from .models import Company, ContactCompany, Jobs, Requirements


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'cnpj']


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
        fields = [
            'company',
            'title',
            'requirements',
            'minimum_schooling',
            'salary_range',
            'description',
        ]


class JobsUpdateForm(ModelForm):

    class Meta:
        model = Jobs
        fields = [
            'title',
            'requirements',
            'minimum_schooling',
            'salary_range',
            'description',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 10}),
        }
