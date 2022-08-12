from django.urls import reverse
from rest_framework.test import APITestCase
from banco.models import Transacoes
from rest_framework import status
from django.http import response

class TransacaoTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('ContaBancaria-list')
        self.conta_1 = Transacoes.objects.create(
           idUsuario_origem = 1, idUsuario_destino=2, valor_transferencia=2000.00
        )
        self.conta_2 = Transacoes.objects.create(
            idUsuario_origem = 1, idUsuario_destino=4, valor_transferencia=2200.00
        )

    def test_requisicao_get_para_listar_Transacao(self):
        """Teste para verificar a requisição GET para listar as Transacoes"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_Transacao(self):
        """Teste para verificar a requisição POST para criar uma Transacao"""
        data = {
            'idUsuario_origem': 1,
            'idUsuario_destino': 2, 
            'valor_transferencia': 1000.00
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_para_deletar_Transacao(self):
        """Teste para verificar a requisição DELETE não permitida para deletar uma Transacao"""
        response = self.client.delete('/Transacao/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_requisicao_put_para_atualizar_Transacao(self):
        """Teste para verificar a requisição PUT para atualizar uma Transacao"""
        data = {
            'idUsuario_origem': 1,
            'idUsuario_destino': 5, 
            'valor_transferencia': 3000.00
        }
        response = self.client.put('/usuarios/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
