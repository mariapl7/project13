# tests/test_models.py
import pytest

from board.ads.models import Product


@pytest.mark.django_db
def test_model_creation():
    instance = Product.objects.create(field1='value1', field2='value2')  # Замените поля на ваши
    assert instance.pk is not None  # Проверяем, что объект был создан и имеет первичный ключ
