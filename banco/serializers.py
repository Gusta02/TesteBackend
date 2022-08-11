from pyexpat import model
from rest_framework import serializers
from banco.models import Usuario, ContaBancaria, Transacoes
from banco.validators import *
from banco.transacao import *

# Rotas Consulta get
class ConsultaSaldoSerializer(serializers.ModelSerializer):
    saldo_total = serializers.ReadOnlyField(source = 'saldo')
    class Meta:
        model = ContaBancaria
        fields = ['saldo_total']
class ConsultaUserSerializer(serializers.ModelSerializer):
    Usuario = serializers.ReadOnlyField(source = 'Lojista')
    class Meta:
        model = Usuario
        fields = ['Usuario']
class ConsulaContaBancariaSerializer(serializers.ModelSerializer):
    banco = serializers.ALL_FIELDS
    class Meta:
        model = ContaBancaria
        fields = '__all__'

# Rotas Padrões Post
class TransacaoBancariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacoes
        fields = '__all__'
    def validate(self, data):
        if not permissao_user(data['idUsuario_origem']):
            raise serializers.ValidationError({'idUsuario_origem':"Esse usuario não pode realizar transações."})
        if not Valida_valorTransferencia(data['idUsuario_origem'], data['valor_transferencia']):
            raise serializers.ValidationError({'valor_transferencia':"Saldo insuficiente para essa transação."})
        if not valida_api():
            raise serializers.ValidationError('Falha na autenticação da transferencia.')
        transferencia( data['idUsuario_destino'], data['idUsuario_origem'], data['valor_transferencia'])
        return data
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
    def validate(self, data):
        if not cpf_cnpj_valido(data['cpf_cnpj']):
            raise serializers.ValidationError({'cpf_cnpj':"Número de CNPJ/CPF inválido"})
           
        if not nome_valido(data['nome_completo']):
            raise serializers.ValidationError({'nome_completo':"Não inclua números neste campo"})
        return data
class ContaBancariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContaBancaria
        fields = '__all__'
        def validate(self, data):
            if not numero_conta(data['numero_conta']):
                raise serializers.ValidationError({'numero_conta':"Número de Conta inválido, por favor preencha somente com numeros"})
            return data

