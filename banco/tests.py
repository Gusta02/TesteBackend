from django.urls import reverse
from rest_framework.test import APITestCase
from banco.models import Usuario, ContaBancaria, Transacoes
from rest_framework import status
from django.http import response

class UsuarioTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Usuarios-list')
        self.usuario_1 = Usuario.objects.create(
            nome_completo = 'Teste1', email= 'teste@teste1.com', cpf_cnpj= '72222767000176', senha = '1234', Lojista = True, ativo = True
        )
        self.usuario_2 = Usuario.objects.create(
            nome_completo = 'Teste2', email= 'teste@teste2.com', cpf_cnpj= '12469861000100', senha = '1234', Lojista = False, ativo = True
        )

    def test_requisicao_get_para_listar_usuarios(self):
        """Teste para verificar a requisição GET para listar os usuarios"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_usuario(self):
        """Teste para verificar a requisição POST para criar um Usuario"""
        data = {
            'nome_completo':'Teste3',
            'email':'teste@teste3.com',
            'cpf_cnpj':'55726603000167',
            'senha':'1234',
            'Lojista':True,
            "ativo":True
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_para_deletar_usuario(self):
        """Teste para verificar a requisição DELETE não permitida para deletar um Usuario"""
        response = self.client.delete('/Usuarios/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_requisicao_put_para_atualizar_usuario(self):
        """Teste para verificar a requisição PUT para atualizar um Usuario"""
        data = {
            'nome_completo':'Teste2',
            'email':'teste@teste2.com',
            'cpf_cnpj':'12469861000100',
            'senha':'1234',
            'Lojista':False,
            "ativo":True
        }
        response = self.client.put('/usuarios/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
