from django.contrib import admin
from banco.models import Usuario

class Usuarios(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'email', 'cpf_cnpj', 'senha','Lojista','ativo')
    list_display_links = ('id', 'nome_completo')
    search_fields = ('id','nome_completo','cpf_cnpj',)
    list_filter = ('ativo',)
    list_editable = ('ativo',)
    list_per_page = 10
    ordering = ('nome_completo',)

admin.site.register(Usuario, Usuarios)