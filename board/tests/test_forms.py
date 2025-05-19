def test_form_valid_data():
    """Проверка, что форма валидна при корректных данных."""
    form = ProductForm(data={
        'name': 'Тестовый товар',
        'description': 'Описание товара',
        'price': 100
    })
    assert form.is_valid()


def test_form_invalid_data():
    """Проверка, что форма недействительна при пустом поле 'name'."""
    form = ProductForm(data={
        'name': '',
        'description': 'Описание товара',
        'price': 100
    })
    assert not form.is_valid()


def test_form_errors_for_invalid_data():
    """Проверка наличия ошибок формы при пустом обязательном поле 'name'."""
    form = ProductForm(data={
        'name': '',
        'description': 'Описание товара',
        'price': 100
    })
    assert not form.is_valid()
    assert 'name' in form.errors
