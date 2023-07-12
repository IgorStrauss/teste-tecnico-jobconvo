from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Experience


class CandidateForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=30, required=True, min_length=3, label='Nome')
    last_name = forms.CharField(
        max_length=30, required=True, min_length=3, label='Sobrenome')
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        self.cleaned_data['username'] = email
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email já cadastrado.")
        return email


class CandidateUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
        ]


class CandidateLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(label="Password", max_length=30, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            'name',
            'description',
        ]
