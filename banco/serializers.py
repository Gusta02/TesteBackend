from pyexpat import model
from rest_framework import serializers
from banco.models import Usuario, ContaBancaria, Transacoes
from banco.validators import *

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
            else:
                raise 
            return data
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

class TransacaoBancariaSerializer(serializers.ModelSerializer):
    model = Transacoes
    fields = '__all__'
    def validate(self, data):
        if not permissao_user(data['idUsuario_origem']):
            raise serializers.ValidationError({'idUsuario_origem':"Esse usuario não pode realizar transações."})

        # if not Valida_valorTransferencia(data[''])
        # return data



