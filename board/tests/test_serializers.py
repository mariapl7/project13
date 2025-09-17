from board.ads.serializers import ProductSerializer


def test_serializer_valid_data():
    """Проверка, что сериализатор валиден при корректных данных."""
    serializer = ProductSerializer(data={
        'name': 'Тестовый товар',
        'description': 'Описание товара',
        'price': '99.99'
    })
    assert serializer.is_valid()


def test_serializer_invalid_data():
    """Проверка, что сериализатор недействителен при пустом обязательном поле 'name'."""
    serializer = ProductSerializer(data={
        'name': '',
        'description': 'Описание товара',
        'price': '99.99'
    })
    assert not serializer.is_valid()
    assert 'name' in serializer.errors

