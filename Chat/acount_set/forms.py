from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'cover']
    title = forms.ImageField(
        label='Мої фото',
        required=False,
    )
