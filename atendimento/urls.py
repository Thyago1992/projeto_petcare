from django.urls import path
from . import views

urlpatterns = [
    path('servicos/', views.lista_servicos, name='lista_servicos'), # Adiciona as URLs do painel de administração do Django  
]