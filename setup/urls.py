from django.contrib import admin
from django.urls import path,include
from banco.views import ConsultaContaBancariaViewSet, ConsultaUserViewset, ContaBancariaViewSet, TransacaoViewSet, UsuarioViewSet, ConsultaSaldoViewSet
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Teste Backend",
      default_version='v1',
      description="Api de Transações bancarias, tendo internamente rotas para Cadastro de Usuario, Criação de Contas Bancarias, e Tratativa de usuarios.",
      terms_of_service="#",
      contact=openapi.Contact(email="gustavo.olivsantos@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


router = routers.DefaultRouter()
router.register('usuarios', UsuarioViewSet, basename='Usuarios')
router.register('contaBancaria', ContaBancariaViewSet, basename='ContaBancaria')
router.register('transacao', TransacaoViewSet, basename='Transacao')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('SaldoBancario/<int:pk>/Saldo/', ConsultaSaldoViewSet.as_view()),
    path('Usuario/<int:pk>/Tipo/', ConsultaUserViewset.as_view()),
    path('Banco/Contabancaria/<int:pk>/', ConsultaContaBancariaViewSet.as_view()),
    path('documentacao/v1/', schema_view.with_ui('redoc', cache_timeout=0), name='DocumentacaoV1'),
    path('documentacao/v2/', schema_view.with_ui('swagger', cache_timeout=0), name='DocumentacaoV2')

]
