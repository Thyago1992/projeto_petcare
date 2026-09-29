from django import forms
from .models import Servico, Tutor

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['nome', 'preco']
        
class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['nome', 'telefone']