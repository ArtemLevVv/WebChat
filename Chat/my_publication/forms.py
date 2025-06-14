from django import forms
from .models import UserPostModel, TagModel

class UserPostForm(forms.ModelForm):
    class Meta:
        model = UserPostModel
        fields = ['name', 'topic', 'tags', 'text', 'link', 'image']

    name = forms.CharField(
        label="Ім'я посту",
        required=True,
        widget=
        forms.TextInput(
            attrs={  
                    'class': 'name',
                    'placeholder': "Природа, книга і спокій 🌿"
        })
    )

    topic = forms.CharField(
        label="Тема посту",
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'topic',
                'placeholder': "Напишіть тему публікації"
                })
    )

    tags = forms.ModelChoiceField(
        label="Оберіть тег до посту",
        queryset=TagModel.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'tags'})
    )

    text = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'text'})
    )

    link = forms.CharField(
        label='посилання',
        required=False,
        widget=forms.TextInput(attrs={'class': 'link'})
    )

    image = forms.ImageField(
        label='Завантажте фото',
        required=False,
        widget=forms.FileInput(attrs={'class': 'image'})
    )
