from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        label='username',
    )
    password = forms.CharField(widget=forms.PasswordInput())


class NewTaskForm(forms.Form):
    title = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'New task',
            }))


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,
                                 required=False,
                                 help_text='Optional.')
    last_name = forms.CharField(max_length=30,
                                required=False,
                                help_text='Optional.')
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']


class RenameTaskForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'New task name',
            }))
