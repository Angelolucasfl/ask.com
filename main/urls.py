from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('pergunta/<str:id>/', views.pergunta, name='pergunta'),
    path('pergunta/fazer_pergunta', views.perguntar, name='perguntar'),
    path('pergunta/editar_pergunta/<str:id>/', views.editar_pergunta, name='editar_pergunta'),
    path('pergunta/deletar_pergunta/<str:id>/', views.deletar, name='deletar'),

    path('pergunta/deletar_resposta/<str:id>/', views.deletar_resposta, name='deletar_resposta'),

    path('pergunta/topicos', views.topicos, name='topicos'),
    path('pergunta/feed_perguntas', views.feed_perguntas, name='feed_perguntas'),
]