from rest_framework.exceptions import ValidationError
from .serializers import YourSerializer  # Замените YourSerializer на ваш сериализатор

def test_serializer_valid_data():
    serializer = YourSerializer(data={'field1': 'value1', 'field2': 'value2'})  # Замените поля на ваши
    assert serializer.is_valid()

def test_serializer_invalid_data():
    serializer = YourSerializer(data={'field1': '', 'field2': 'value2'})  # Поле field1 пустое, должно быть невалидным
    assert not serializer.is_valid()