import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.django_assertions import assert_contains, assert_not_contains


@pytest.fixture
def resp(client, db):
    return client.get(reverse('login'))


def test_login_form_page(resp):
    assert resp.status_code == 200


@pytest.fixture
def usuario(db, django_user_model):
    usuario_model = mommy.make(django_user_model)
    senha = 'senha'
    usuario_model.set_password(senha)
    usuario_model.save()
    usuario_model.senha_plana = senha
    return usuario_model


@pytest.fixture
def resp_post(client, usuario):
    return client.post(reverse('login'),
                       {'username': usuario.email, 'password': usuario.senha_plana})


def test_login_redirect(resp_post):
    assert resp_post.status_code == 302
    assert resp_post.url == reverse('modulos:indice')


@pytest.fixture
def resp_home(client, db):
    return client.get(reverse('base:home'))


def test_botao_entrar_disponivel(resp_home):
    assert_contains(resp_home, 'Entrar')


def test_link_disponivel(resp_home):
    assert_contains(resp_home, reverse('login'))


@pytest.fixture
def resp_home_logado(client_com_usuario_logado, db):
    return client_com_usuario_logado.get(reverse('base:home'))


def test_botao_entrar_indisponivel(resp_home_logado):
    assert_not_contains(resp_home_logado, 'Entrar')


def test_link_indisponivel(resp_home_logado):
    assert_not_contains(resp_home_logado, reverse('login'))


def test_botao_sair_disponivel(resp_home_logado):
    assert_contains(resp_home_logado, 'Sair')


def test_nome_usuario_logado_disponivel(resp_home_logado, usuario_logado):
    assert_contains(resp_home_logado, usuario_logado.first_name)


def test_link_logout_disponivel(resp_home_logado):
    assert_contains(resp_home_logado, reverse('logout'))
