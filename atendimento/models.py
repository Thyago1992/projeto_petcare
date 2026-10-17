from django.db import models
from servico.models import Servico


class Tutor(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Pet(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.PROTECT, related_name='pets')
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome} ({self.tutor.nome})"


class Atendimento(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.PROTECT)
    servico = models.ForeignKey(Servico, on_delete=models.PROTECT)
    data = models.DateTimeField()
    preco_cobrado = models.DecimalField(max_digits=8, decimal_places=2, blank=True)

    class Meta:
        ordering = ['-data']

    def save(self, *args, **kwargs):
        if self.preco_cobrado is None:
            self.preco_cobrado = self.servico.preco
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.pet.nome} - {self.servico.nome}"
