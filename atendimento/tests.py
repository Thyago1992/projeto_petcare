from datetime import timedelta
from decimal import Decimal

from django.contrib.auth.models import User
from django.db.models import ProtectedError
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from servico.models import Servico
from .models import Atendimento, Pet, Tutor


class DadosBase(TestCase):
    """Cria dados comuns que vários testes usam."""

    @classmethod
    def setUpTestData(cls):
        cls.usuario = User.objects.create_user(username='teste', password='senha-forte-123')
        cls.tutor = Tutor.objects.create(nome='Thyago Antonio', telefone='81999990000')
        cls.pet = Pet.objects.create(tutor=cls.tutor, nome='Spike', especie='Cachorro')
        cls.servico = Servico.objects.create(nome='Banho e Tosa', preco=Decimal('150.00'))

    def entrar(self):
        self.client.force_login(self.usuario)


# ---------------------------------------------------------------- Modelos

class AtendimentoModelTests(DadosBase):

    def test_preco_em_branco_usa_preco_do_servico(self):
        atendimento = Atendimento.objects.create(
            pet=self.pet, servico=self.servico, data=timezone.now()
        )
        self.assertEqual(atendimento.preco_cobrado, Decimal('150.00'))

    def test_preco_informado_e_mantido(self):
        atendimento = Atendimento.objects.create(
            pet=self.pet, servico=self.servico, data=timezone.now(),
            preco_cobrado=Decimal('120.00'),
        )
        self.assertEqual(atendimento.preco_cobrado, Decimal('120.00'))

    def test_texto_do_atendimento(self):
        atendimento = Atendimento.objects.create(
            pet=self.pet, servico=self.servico, data=timezone.now()
        )
        self.assertEqual(str(atendimento), 'Spike - Banho e Tosa')

    def test_texto_do_pet_inclui_tutor(self):
        self.assertEqual(str(self.pet), 'Spike (Thyago Antonio)')

    def test_nao_apaga_tutor_que_tem_pet(self):
        with self.assertRaises(ProtectedError):
            self.tutor.delete()


# ---------------------------------------------------------------- Login

ROTAS_PROTEGIDAS = ['painel', 'lista_servicos', 'lista_tutores', 'novo_tutor',
                    'lista_pets', 'novo_pet', 'novo_atendimento']


class AcessoTests(DadosBase):

    def test_paginas_exigem_login(self):
        for rota in ROTAS_PROTEGIDAS:
            with self.subTest(rota=rota):
                resposta = self.client.get(reverse(rota))
                self.assertRedirects(resposta, f"{reverse('login')}?next={reverse(rota)}")

    def test_paginas_abrem_com_login(self):
        self.entrar()
        for rota in ROTAS_PROTEGIDAS:
            with self.subTest(rota=rota):
                self.assertEqual(self.client.get(reverse(rota)).status_code, 200)

    def test_login_redireciona_para_painel(self):
        resposta = self.client.post(reverse('login'), {
            'username': 'teste', 'password': 'senha-forte-123',
        })
        self.assertRedirects(resposta, reverse('painel'))

    def test_sair_desloga_usuario(self):
        self.entrar()
        resposta = self.client.post(reverse('sair'))
        self.assertRedirects(resposta, reverse('login'))
        resposta = self.client.get(reverse('painel'))
        self.assertEqual(resposta.status_code, 302)

    def test_cadastro_cria_usuario(self):
        resposta = self.client.post(reverse('cadastro'), {
            'username': 'novo',
            'password1': 'OutraSenha#2026',
            'password2': 'OutraSenha#2026',
        })
        self.assertRedirects(resposta, reverse('login'))
        self.assertTrue(User.objects.filter(username='novo').exists())


# ---------------------------------------------------------------- Painel

class PainelTests(DadosBase):

    def test_painel_vazio(self):
        self.entrar()
        resposta = self.client.get(reverse('painel'))
        self.assertContains(resposta, 'Nenhum atendimento registrado hoje.')
        self.assertEqual(resposta.context['total'], 0)

    def test_painel_mostra_so_atendimentos_de_hoje(self):
        agora = timezone.now()
        Atendimento.objects.create(pet=self.pet, servico=self.servico, data=agora)
        Atendimento.objects.create(pet=self.pet, servico=self.servico,
                                   data=agora - timedelta(days=1))
        self.entrar()
        resposta = self.client.get(reverse('painel'))
        self.assertEqual(len(resposta.context['atendimentos']), 1)

    def test_painel_soma_valor_total(self):
        agora = timezone.now()
        Atendimento.objects.create(pet=self.pet, servico=self.servico, data=agora)
        Atendimento.objects.create(pet=self.pet, servico=self.servico, data=agora,
                                   preco_cobrado=Decimal('50.00'))
        self.entrar()
        resposta = self.client.get(reverse('painel'))
        self.assertEqual(resposta.context['total'], Decimal('200.00'))
        self.assertContains(resposta, 'Spike')


# ---------------------------------------------------------------- Cadastros

class CadastrosTests(DadosBase):

    def setUp(self):
        self.entrar()

    def test_cria_tutor(self):
        resposta = self.client.post(reverse('novo_tutor'), {
            'nome': 'Maria', 'telefone': '81988887777',
        })
        self.assertRedirects(resposta, reverse('lista_tutores'))
        self.assertTrue(Tutor.objects.filter(nome='Maria').exists())

    def test_tutor_sem_nome_nao_salva(self):
        resposta = self.client.post(reverse('novo_tutor'), {
            'nome': '', 'telefone': '81988887777',
        })
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(Tutor.objects.count(), 1)

    def test_edita_tutor(self):
        self.client.post(reverse('editar_tutor', args=[self.tutor.pk]), {
            'nome': 'Thyago A.', 'telefone': '81999990000',
        })
        self.tutor.refresh_from_db()
        self.assertEqual(self.tutor.nome, 'Thyago A.')

    def test_cria_pet(self):
        resposta = self.client.post(reverse('novo_pet'), {
            'tutor': self.tutor.pk, 'nome': 'Mel', 'especie': 'Gato',
        })
        self.assertRedirects(resposta, reverse('lista_pets'))
        self.assertTrue(self.tutor.pets.filter(nome='Mel').exists())

    def test_cria_servico(self):
        resposta = self.client.post(reverse('novo_servico'), {
            'nome': 'Consulta', 'preco': '90.00',
        })
        self.assertRedirects(resposta, reverse('lista_servicos'))
        self.assertTrue(Servico.objects.filter(nome='Consulta').exists())

    def test_cria_atendimento_sem_preco(self):
        resposta = self.client.post(reverse('novo_atendimento'), {
            'pet': self.pet.pk,
            'servico': self.servico.pk,
            'data': timezone.localtime().strftime('%Y-%m-%dT%H:%M'),
            'preco_cobrado': '',
        })
        self.assertRedirects(resposta, reverse('painel'))
        self.assertEqual(Atendimento.objects.get().preco_cobrado, Decimal('150.00'))
