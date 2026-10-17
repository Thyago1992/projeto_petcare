from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('catalogo/', views.ServicoListView.as_view(), name='lista_servicos'),
    path('servicos/novo/', views.ServicoCreateView.as_view(), name='novo_servico'),
    path('servicos/<int:pk>/editar/', views.ServicoUpdateView.as_view(), name='editar_servico'),
    path('tutores/', views.TutorListView.as_view(), name='lista_tutores'),
    path('tutores/novo/', views.TutorCreateView.as_view(), name='novo_tutor'),
    path('tutores/<int:pk>/editar/', views.TutorUpdateView.as_view(), name='editar_tutor'),
    path('pets/', views.PetListView.as_view(), name='lista_pets'),
    path('pets/novo/', views.PetCreateView.as_view(), name='novo_pet'),
    path('atendimentos/novo/', views.AtendimentoCreateView.as_view(), name='novo_atendimento'),
    path('login/', views.EntrarView.as_view(), name='login'),
    path('cadastro/', views.CadastroView.as_view(), name='cadastro'),
    path('sair/', LogoutView.as_view(), name='sair'),
    path('painel/', views.painel, name='painel'),
    path('', views.painel, name='inicio'),
]
