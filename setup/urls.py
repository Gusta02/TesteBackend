from django.contrib import admin
from django.urls import path,include
from banco.views import ConsultaContaBancariaViewSet, ConsultaUserViewset, ContaBancariaViewSet, TransacaoViewSet, UsuarioViewSet, ConsultaSaldoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('usuarios', UsuarioViewSet, basename='Usuarios')
router.register('contaBancaria', ContaBancariaViewSet, basename='ContaBancaria')
router.register('transacao', TransacaoViewSet, basename='Transacao')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('SaldoBancario/<int:pk>/Saldo/', ConsultaSaldoViewSet.as_view()),
    path('Usuario/<int:pk>/Tipo/', ConsultaUserViewset.as_view()),
    path('Banco/Contabancaria/<int:pk>/', ConsultaContaBancariaViewSet.as_view())

]