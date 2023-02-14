from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pergunta/<str:id>/', views.pergunta, name='pergunta')
]