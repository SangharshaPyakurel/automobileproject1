from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )



class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Name"
            }
        )
    )
    email = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email"
            }
        )
    )
    password1 = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password"
            }
        )
    )
    password2 = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirm Password"
            }
        )
    )
    password2 = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirm Password"
            }
        )
    )
    class Meta:
        model = User
        fields = ['username','email','password1','password2','is_superuser', 'is_staff', 'is_customer']