from django.urls import reverse


def test_home_view(client):
    url = reverse('ads.urls')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Welcome' in response.content.decode()