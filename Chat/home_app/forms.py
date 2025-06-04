from django import forms

class ModalFormExtraInfo(forms):
    username = forms.CharField(
        label="Ім'я",
        required=True,
        widget= forms.TextInput(
            attrs={
                'class': 'name',
                'placeholder': "Введіть Ваше ім'я",
            }
        )
    )
    last_name = forms.CharField(
        label='Прізвище',
        required=True,
        widget= forms.TextInput(
            attrs={
                'class': "last_name",
                'placeholder': "Введіть Ваше прізвище",
            }
        )
    )
    login = forms.CharField(
        label="Ім'я користувача",
        required=True,
        widget= forms.TextInput(
            attrs={
                'class': "login",
                'placeholder': '@',
            }
        )
    )