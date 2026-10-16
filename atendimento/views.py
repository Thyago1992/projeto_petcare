from django.http import HttpResponse
from servico.models import Servico
from .models import Tutor, Atendimento
from .forms import ServicoForm, TutorForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from datetime import date
from django.db.models import Sum
from django.utils import timezone



@login_required
def lista_servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'atendimento/servicos.html', {'servicos': servicos})


@login_required
def lista_tutores(request):
    tutores = Tutor.objects.all()
    return render(request, 'atendimento/tutores.html', {'tutores': tutores})


@login_required
def novo_servico(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_servicos')
    else:
        form = ServicoForm()
    return render(request, 'atendimento/servico_form.html', {'form': form})


@login_required
def novo_tutor(request):
    if request.method == 'POST':
        form = TutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tutores')
    else:
        form = TutorForm()
    return render(request, 'atendimento/tutor_form.html', {'form': form})


@login_required
def editar_servico(request, id):
    servico = get_object_or_404(Servico, id=id)
    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            return redirect('lista_servicos')
    else:
        form = ServicoForm(instance=servico)
    return render(request, 'atendimento/servico_form.html', {'form': form})


@login_required
def editar_tutor(request, id):
    tutor = get_object_or_404(Tutor, id=id)
    if request.method == 'POST':
        form = TutorForm(request.POST, instance=tutor)
        if form.is_valid():
            form.save()
            return redirect('lista_tutores')
    else:
        form = TutorForm(instance=tutor)
    return render(request, 'atendimento/tutor_form.html', {'form': form})


def entrar(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('lista_servicos')
    else:
        form = AuthenticationForm()
    return render(request, 'atendimento/login.html', {'form': form})


@login_required
def sair(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login')


def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'atendimento/cadastro.html', {'form': form})

@login_required
def painel(request):
    atendimentos = (
        Atendimento.objects
        .filter(data__date=timezone.localdate())
        .select_related('tutor', 'servico')
    )
    total = atendimentos.aggregate(total=Sum('servico__preco'))['total'] or 0
    return render(request, 'atendimento/painel.html', {
        'atendimentos': atendimentos,
        'total': total,
    })