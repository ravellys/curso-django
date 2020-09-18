import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    return resp.status_code == 200


@pytest.mark.parametrize(
    'title',
    [
        'Video Aperitivo: Motivação',
        'Video Aperitivo: Instalação do Windows'
    ]
)
def test_titulo_video(resp, title):
    assert_contains(resp, title)


@pytest.mark.parametrize(
    'slug',
    [
        'motivacao',
        'instalacao-windows'
    ]
)
def test_link_video(resp, slug):
    link = reverse('aperitivos:video', args=(slug, ))
    assert_contains(resp, f'href={link}')
