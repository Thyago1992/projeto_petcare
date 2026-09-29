from django.urls import path
from . import views

urlpatterns = [
    path('catalogo/', views.lista_servicos, name='lista_servicos'),
    path('tutores/', views.lista_tutores, name='lista_tutores'),
    path('tutores/novo/', views.novo_tutor, name='novo_tutor'),
    path('servicos/novo/', views.novo_servico, name='novo_servico'),
    path('servicos/<int:id>/editar/', views.editar_servico, name='editar_servico'),
    path('tutores/<int:id>/editar/', views.editar_tutor, name='editar_tutor'),
    path('login/', views.entrar, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('sair/', views.sair, name='sair'),
]