from django.db import models

class Usuario(models.Model):
    nome_completo = models.CharField(blank=False, max_length=150)
    email = models.EmailField(blank=False, max_length=40, unique=True)
    cpf_cnpj = models.CharField(blank=False, max_length=14, unique=True)
    senha = models.CharField(blank=False, max_length=30)
    Lojista = models.BooleanField(null=True)
    ativo = models.BooleanField()

    def __str__(self):
        return self.nome_completo

class ContaBancaria(models.Model):
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    numero_conta = models.IntegerField(unique=True)
    saldo = models.DecimalField(max_digits=19, decimal_places=2)
    BitAtivo = models.BooleanField()
    
    def __str__(self):
        return self.idUsuario
