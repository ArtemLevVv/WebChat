from django import forms
from .models import UserPostModel, TagModel

class UserPostForm(forms.Form):
    name = forms.CharField(
        label="Ім'я посту",
        required= True,
        widget= forms.TextInput(
            attrs={
                'class': 'name'
            }
        )
    )
    topic = forms.CharField(
        label="Тема посту",
        required= True,
        widget= forms.Textarea(
        attrs= {
            'class': 'topic'
            }
        )
    )
    tags = forms.ChoiceField(
        label="Оберіть відповідьні геги до посту",
        required= True,
        widget= forms.CheckboxInput(
            attrs={
            'class': 'tags'
            }
        )
    )
    link = forms.CharField(
        label='Вкажіть додаткове посилання до теми',
        required= False,
        widget= forms.TextInput(
            attrs={
                'class': 'link'
            }
        )
    )
    # image = forms.ImageField(
    #     label='Завантажте фото',
    #     required=False,
    #     widget=  forms.FileInput(
    #         attrs={
    #             'class': 'image'
    #         }
    #     )
    # )
    