from django import forms
from .models import Ad


class AdForm(forms.ModelForm):
    """
    Форма для создания и редактирования объявления.

    Использует модель Ad для определения полей формы.
    """

    class Meta:
        model = Ad
        fields = ['title', 'description']
        