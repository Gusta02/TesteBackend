from django.db import models

class UsuarioComum(models.Model):
    nome_completo = models.CharField(blank=False, max_length=150)
    email = models.EmailField(blank=False, max_length=30, unique=True )
    cpf = models.CharField(blank=False, max_length=11, unique=True)
    senha = models.CharField(blank=False, max_length=30)
    ativo = models.BooleanField()

    def __str__(self):
        return self.nome_completo

class Lojista(models.Model):
    nome_completo = models.CharField(blank=False, max_length=150)
    email = models.EmailField(blank=False, max_length=30, unique=True )
    cnpj = models.CharField(blank=False, max_length=14, unique=True)
    senha = models.CharField(blank=False, max_length=30)
    ativo = models.BooleanField()

    def __str__(self):
        return self.nome_completo