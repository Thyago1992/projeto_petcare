from django import forms

from servico.models import Servico
from .models import Atendimento, Pet, Tutor


class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['nome', 'preco']


class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['nome', 'telefone']


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['tutor', 'nome', 'especie']


class AtendimentoForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = ['pet', 'servico', 'data', 'preco_cobrado']
        widgets = {
            'data': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M',
            ),
        }
        help_texts = {
            'preco_cobrado': 'Deixe em branco para usar o preço do serviço.',
        }
