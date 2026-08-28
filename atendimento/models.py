from django.db import models
from servico.models import Servico

# Create your models here.

class Tutor(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Atendimento(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.PROTECT)
    data = models.DateTimeField()

    def __str__(self):
        return f"{self.tutor.nome} - {self.servico.nome}"
