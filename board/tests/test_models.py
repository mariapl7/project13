import pytest

from board.ads.models import Product


@pytest.mark.django_db
def test_model_creation():
    """Проверка создания экземпляра модели Product и автоматического присвоения первичного ключа."""
    # Создаем объект Product с примерными данными
    instance = Product.objects.create(field1='name', field2='description')
    # Проверяем, что объект успешно создан и имеет первичный ключ
    assert instance.pk is not None
