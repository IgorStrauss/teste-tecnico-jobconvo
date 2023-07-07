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

    requirements = forms.ModelMultipleChoiceField(
        queryset=Requirements.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

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
    is_active = forms.BooleanField(label='Status da vaga', required=False)

    requirements = forms.ModelMultipleChoiceField(
        queryset=Requirements.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Jobs
        fields = [
            'title',
            'requirements',
            'minimum_schooling',
            'salary_range',
            'description',
            'is_active'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 10}),
        }
