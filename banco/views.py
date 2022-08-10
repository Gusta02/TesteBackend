from rest_framework import viewsets, filters
from banco.serializers import UsuarioSerializer, LojistaSerializer
from banco.models import UsuarioComum, Lojista
from django_filters.rest_framework import DjangoFilterBackend

class UsuarioViewSet(viewsets.ModelViewSet):
    """Listando todos os Usuarios"""
    queryset = UsuarioComum.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome_completo']
    search_fields = ['nome_completo', 'cpf']
    filterset_fields = ['ativo']
    
class LojistaViewSet(viewsets.ModelViewSet):
    """Listando todos os Lojistas"""
    queryset = Lojista.objects.all()
    serializer_class = LojistaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome_completo']
    search_fields = ['nome_completo', 'cnpj']
    filterset_fields = ['ativo']