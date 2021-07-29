from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label='username',
    )
    password = forms.CharField(widget=forms.PasswordInput())

class NewTaskForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'New task',
            }))