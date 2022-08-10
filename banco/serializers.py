from wsgiref.validate import validator
from rest_framework import serializers
from banco.models import Usuario, ContaBancaria
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
            return data