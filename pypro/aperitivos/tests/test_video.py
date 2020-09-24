import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.aperitivos.models import Video
from pypro.django_assertions import assert_contains


@pytest.fixture
def video(db):
    return mommy.make(Video)


@pytest.fixture
def resp(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug, )))


@pytest.fixture
def resp_video_notfound(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug+'_video_notfound', )))


def test_status_code(resp):
    return resp.status_code == 200


def test_status_code_video_notfound(resp_video_notfound):
    return resp_video_notfound.status_code == 404


def test_title_video(resp, video):
    assert_contains(resp, video.title)


def test_content_video(resp, video):
    assert_contains(resp, f'<iframe src="https://www.youtube.com/embed/{video.v_id}"')
