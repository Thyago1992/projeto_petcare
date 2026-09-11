from django.shortcuts import render
from django.http import HttpResponse
from servico.models import Servico
from .models import Tutor

def lista_servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'atendimento/servicos.html', {'servicos': servicos})

def lista_tutores(request):
    tutores = Tutor.objects.all()
    return render(request, 'atendimento/tutores.html', {'tutores': tutores})