from rest_framework import viewsets, filters
from banco.serializers import UsuarioSerializer
from banco.models import Usuario
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class UsuarioViewSet(viewsets.ModelViewSet):
    """Listando todos os Usuarios"""
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome_completo']
    search_fields = ['nome_completo', 'cpf_cnpj']
    filterset_fields = ['ativo']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    