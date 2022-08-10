from rest_framework import serializers
from banco.models import UsuarioComum, Lojista
from banco.validators import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioComum
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"Número de CPF inválido"})
        if not nome_valido(data['nome_completo']):
            raise serializers.ValidationError({'nome_completo':"Não inclua números neste campo"})
        return data
    
class LojistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lojista
        fields = '__all__'
    def validate(self, data):
        if not cnpj_valido(data['cnpj']):
            raise serializers.ValidationError({'cnpj':"Número de CNPJ inválido"})
        if not nome_valido(data['nome_completo']):
            raise serializers.ValidationError({'nome_completo':"Não inclua números neste campo"})
        return data