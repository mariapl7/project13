from django import forms
from .models import Product, Comment


class ProductForm(forms.ModelForm):
    """Форма для создания и редактирования товара."""

    class Meta:
        model = Product
        fields = ['name', 'description', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название товара'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание товара'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите цену'}),
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        return price


class CommentForm(forms.ModelForm):
    """Форма для добавления комментария к товару."""

    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите ваш комментарий'}),
        }
