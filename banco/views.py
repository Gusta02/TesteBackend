from rest_framework import viewsets, filters, generics
from banco.serializers import UsuarioSerializer, ContaBancariaSerializer, ConsultaSaldoSerializer, ConsultaUserSerializer, TransacaoBancariaSerializer, ConsulaContaBancariaSerializer
from banco.models import Usuario, ContaBancaria, Transacoes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class UsuarioViewSet(viewsets.ModelViewSet):
    """Listando todos os Usuarios"""
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id']
    search_fields = ['nome_completo', 'cpf_cnpj']
    filterset_fields = ['ativo']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ContaBancariaViewSet(viewsets.ModelViewSet):
    """Listando todos os Usuarios"""
    queryset = ContaBancaria.objects.all()
    serializer_class = ContaBancariaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['idUsuario']
    search_fields = ['idUsuario', 'numero_conta']
    # filterset_fields = ['ativo']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ConsultaSaldoViewSet(generics.ListAPIView):
    """consultando saldo de um usuario"""
    def get_queryset(self):
        queryset = ContaBancaria.objects.filter(idUsuario = self.kwargs['pk'])
        return queryset
    serializer_class = ConsultaSaldoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ConsultaContaBancariaViewSet(generics.ListAPIView):
    """consultando saldo de um usuario"""
    def get_queryset(self):
        queryset = ContaBancaria.objects.filter(idUsuario = self.kwargs['pk'])
        return queryset
    serializer_class = ConsulaContaBancariaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ConsultaUserViewset(generics.ListAPIView):
    def get_queryset(self):
        queryset = Usuario.objects.filter(id = self.kwargs['pk'])
        return queryset

    serializer_class = ConsultaUserSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class TransacaoViewSet(viewsets.ModelViewSet):
    """Listando todos os Usuarios"""
    queryset = Transacoes.objects.all()
    serializer_class = TransacaoBancariaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['idUsuario_origem']
    search_fields = ['idUsuario_origem']
    filterset_fields = ['idUsuario_origem']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]