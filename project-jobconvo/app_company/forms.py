from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Company, ContactCompany, Jobs, Requirements


class CompanyOwnerRegisterForm(UserCreationForm):

    email = forms.EmailField(required=True, label='Email')
    cnpj = forms.CharField(required=True, max_length=14,
                           min_length=14, label='CNPJ')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'cnpj',
            'password1',
            'password2',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email já cadastrado.")
        return email


class CompanyOwnerLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(label="Password", max_length=30, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))


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

    def __init__(self, company_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['requirements'].queryset = Requirements.objects.all()
        self.company_id = company_id

    class Meta:
        model = Jobs
        fields = [
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
