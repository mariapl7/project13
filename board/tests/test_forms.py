from django import forms
from .forms import YourForm  # Замените YourForm на вашу форму


def test_form_valid_data():
    form = YourForm(data={'field1': 'value1', 'field2': 'value2'})  # Замените поля на ваши
    assert form.is_valid()


def test_form_invalid_data():
    form = YourForm(data={'field1': '', 'field2': 'value2'})  # Поле field1 пустое, должно быть невалидным
    assert not form.is_valid()