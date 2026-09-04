from django.shortcuts import render
from django.http import HttpResponse
from .models import Servico

def lista_servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'atendimento/servicos.html', {'servicos': servicos})
