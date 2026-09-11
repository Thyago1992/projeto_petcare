from django.urls import path
from . import views

urlpatterns = [
    path('catalogo/', views.lista_servicos, name='lista_servicos'),
    path('tutores/', views.lista_tutores, name='lista_tutores'),
]