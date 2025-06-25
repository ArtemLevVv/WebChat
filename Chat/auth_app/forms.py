from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    username = forms.EmailField(
        label="Електронна пошта",
        required= True,
        widget= forms.EmailInput(
            attrs={
                'class':'email',
                'placeholder':'you@example.com',
            }
        )
    )

    password1 = forms.CharField(
        label="Пароль",
        required= True,
        widget= forms.PasswordInput(
            attrs={
                'class':'password',
                'placeholder':'Введи пароль',
            }
        )
    )

    password2 = forms.CharField(
        label="Підтведи пароль",
        required= True,
        widget= forms.PasswordInput(
            attrs={
                'class':'confirm_password',
                'placeholder':'Повтори пароль',
            }
        )
    )
class CustomAuthenticatedForm(AuthenticationForm):
    username = forms.EmailField(
        label="Електронна пошта",
        required= True,
        widget= forms.EmailInput(
            attrs={
                'class':'email',
                'placeholder':'you@example.com',
            }
        )
    )

    password = forms.CharField(
        label="Пароль",
        required= True,
        widget= forms.PasswordInput(
            attrs={
                'class':'password',
                'placeholder':'Введи пароль',
            }
        )
    )
