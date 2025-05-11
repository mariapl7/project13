import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_home_view(client):
    response = client.get(reverse('home'))  # Замените 'home' на имя вашего URL
    assert response.status_code == 200
    assert 'Welcome' in response.content.decode()  # Замените 'Welcome' на текст, который должен быть на странице