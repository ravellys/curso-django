from django.urls import path

from pypro.turma import views

app_name = 'turma'
urlpatterns = [
    path('', views.indice, name='indice'),
]
