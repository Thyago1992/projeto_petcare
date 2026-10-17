from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView, UpdateView

from servico.models import Servico
from .forms import AtendimentoForm, PetForm, ServicoForm, TutorForm
from .models import Atendimento, Pet, Tutor


class FormularioMixin(LoginRequiredMixin):
    template_name = 'atendimento/form.html'


class ServicoListView(LoginRequiredMixin, ListView):
    model = Servico
    template_name = 'atendimento/servicos.html'
    context_object_name = 'servicos'


class ServicoCreateView(FormularioMixin, CreateView):
    model = Servico
    form_class = ServicoForm
    success_url = reverse_lazy('lista_servicos')
    extra_context = {'titulo': 'Novo serviço'}


class ServicoUpdateView(FormularioMixin, UpdateView):
    model = Servico
    form_class = ServicoForm
    success_url = reverse_lazy('lista_servicos')
    extra_context = {'titulo': 'Editar serviço'}


class TutorListView(LoginRequiredMixin, ListView):
    model = Tutor
    template_name = 'atendimento/tutores.html'
    context_object_name = 'tutores'


class TutorCreateView(FormularioMixin, CreateView):
    model = Tutor
    form_class = TutorForm
    success_url = reverse_lazy('lista_tutores')
    extra_context = {'titulo': 'Novo tutor'}


class TutorUpdateView(FormularioMixin, UpdateView):
    model = Tutor
    form_class = TutorForm
    success_url = reverse_lazy('lista_tutores')
    extra_context = {'titulo': 'Editar tutor'}


class PetListView(LoginRequiredMixin, ListView):
    queryset = Pet.objects.select_related('tutor')
    template_name = 'atendimento/pets.html'
    context_object_name = 'pets'


class PetCreateView(FormularioMixin, CreateView):
    model = Pet
    form_class = PetForm
    success_url = reverse_lazy('lista_pets')
    extra_context = {'titulo': 'Novo pet'}


class AtendimentoCreateView(FormularioMixin, CreateView):
    model = Atendimento
    form_class = AtendimentoForm
    success_url = reverse_lazy('painel')
    extra_context = {'titulo': 'Novo atendimento'}


class EntrarView(auth_views.LoginView):
    template_name = 'atendimento/login.html'
    redirect_authenticated_user = True


class CadastroView(CreateView):
    form_class = UserCreationForm
    template_name = 'atendimento/cadastro.html'
    success_url = reverse_lazy('login')


@login_required
def painel(request):
    atendimentos = (
        Atendimento.objects
        .filter(data__date=timezone.localdate())
        .select_related('pet__tutor', 'servico')
    )
    total = atendimentos.aggregate(total=Sum('preco_cobrado'))['total'] or 0
    return render(request, 'atendimento/painel.html', {
        'atendimentos': atendimentos,
        'total': total,
    })
