from django.urls import reverse
from rest_framework.test import APITestCase
from banco.models import ContaBancaria
from rest_framework import status
from django.http import response

class BancoTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('ContaBancaria-list')
        self.conta_1 = ContaBancaria.objects.create(
           idUsuario=15, numero_conta=16582, saldo=8000.00, BitAtivo=True
        )
        self.conta_2 = ContaBancaria.objects.create(
            idUsuario=16, numero_conta=16682, saldo=7000.00, BitAtivo=False
        )

    def test_requisicao_get_para_listar_ContaBancaria(self):
        """Teste para verificar a requisição GET para listar as Contas"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_ContaBancaria(self):
        """Teste para verificar a requisição POST para criar uma Conta"""
        data = {
            'idUsuario': 17,
            'numero_conta': 12357,
            'saldo': 15000.00,
            'BitAtivo': True
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_para_deletar_ContaBancaria(self):
        """Teste para verificar a requisição DELETE não permitida para deletar uma conta"""
        response = self.client.delete('/ContaBancaria/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_requisicao_put_para_atualizar_ContaBancaria(self):
        """Teste para verificar a requisição PUT para atualizar uma conta"""
        data = {
            'idUsuario': 17,
            'numero_conta': 12357,
            'saldo': 18000.00,
            'BitAtivo': True
        }
        response = self.client.put('/usuarios/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
