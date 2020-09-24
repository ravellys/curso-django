import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.aperitivos.models import Video
from pypro.django_assertions import assert_contains


@pytest.fixture
def videos(db):
    return mommy.make(Video, 3)


@pytest.fixture
def resp(client, videos):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    return resp.status_code == 200


def test_titulo_video(resp, videos):
    for video in videos:
        assert_contains(resp, video.title)


def test_link_video(resp, videos):
    for video in videos:
        link = reverse('aperitivos:video', args=(video.slug,))
        assert_contains(resp, f'href={link}')
