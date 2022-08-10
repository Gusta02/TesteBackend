from django.contrib import admin
from banco.models import UsuarioComum, Lojista

class Usuarios(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'rg', 'celular', 'ativo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome','cpf',)
    list_filter = ('ativo',)
    list_editable = ('ativo',)
    list_per_page = 10
    ordering = ('nome',)

admin.site.register(UsuarioComum, Usuarios)