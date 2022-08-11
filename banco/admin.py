from django.contrib import admin
from banco.models import Usuario, ContaBancaria, Transacoes

class Usuarios(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'email', 'cpf_cnpj', 'senha','Lojista','ativo')
    list_display_links = ('id', 'nome_completo')
    search_fields = ('id','nome_completo','cpf_cnpj',)
    list_filter = ('ativo',)
    list_editable = ('ativo',)
    list_per_page = 10
    ordering = ('id',)

admin.site.register(Usuario, Usuarios)

class Conta(admin.ModelAdmin):
    list_display = ('id', 'idUsuario', 'numero_conta', 'saldo','BitAtivo')
    list_display_links = ('id', 'idUsuario')
    search_fields = ('id','idUsuario','numero_conta',)
    list_filter = ('BitAtivo',)
    list_editable = ('BitAtivo',)
    list_per_page = 10
    ordering = ('numero_conta',)

admin.site.register(ContaBancaria, Conta)

class transacao(admin.ModelAdmin):
    list_display = ('id', 'idUsuario_origem', 'idUsuario_destino', 'valor_transferencia')
    list_display_links = ('id', 'idUsuario_origem')
    search_fields = ('id','idUsuario_origem',)
    # list_filter = ('BitAtivo',)
    # list_editable = ('BitAtivo',)
    list_per_page = 10
    ordering = ('idUsuario_origem',)

admin.site.register(Transacoes, transacao)