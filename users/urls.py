from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.logar, name='logar'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('perfil/', views.perfil, name='perfil'),
    path('sair/', views.sair, name='sair'),
]