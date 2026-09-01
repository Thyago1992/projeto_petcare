from django.shortcuts import render
from django.http import HttpResponse

def lista_servicos(request):
    return HttpResponse("Página de Serviços do PetCare")
# Create your views here.
